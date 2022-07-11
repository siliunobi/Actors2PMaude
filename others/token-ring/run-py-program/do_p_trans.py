'''
Do p-trans
Other python programs may invoke function process_file_p(filename, module_name), where 3 maude files are in path INPUT_FOLDER_P which abide by the maude grammar and according 3 module names are the same name of filename. 
The function will generate 2 p-trans file of file 1 and file 2 in the path OUTPUT_FOLDER_P with the same name.
2022.7.9 21:18 +0800
'''
from __future__ import print_function
import os
import sys
import re
from run_lib import *

INPUT_FOLDER_P = "input-modules"
OUTPUT_FOLDER_P = "p-output"


'''
Process file and generate p-trans file in OUTPUT_FOLDER_P as required
Input: 
	filename: a list, filename for file 1-3;
	module_name: a list, the same name module name of the filename
Output: no return value, but generate required p-trans file in OUTPUT_FOLDER_P
'''
def process_file_p(filename, module_name):
	# 1. create output folder, get file pointers
	if not os.path.exists(OUTPUT_FOLDER_P):
		os.makedirs(OUTPUT_FOLDER_P)
	frp = []  # file read pointers
	for fn in filename:
		fr = open(os.path.join(INPUT_FOLDER_P, fn),"r")
		frp.append(fr)
	# file1 write pointer
	fwp = open(os.path.join(OUTPUT_FOLDER_P, filename[0]),"w")
	fwp2 = open(os.path.join(OUTPUT_FOLDER_P, filename[1]),"w")
	
	# 2. get tpls info from file 3
	ftxt3 = frp[2].readlines()
	rname2delta_sort, tpls = get_tpls_info(ftxt3)
	rname2tpls = {}
	for item in tpls:
		rname2tpls[item[0]] = item
	'''
	print("process_file_p_2")
	print(rname2delta_sort)
	print(rname2tpls)
	'''
	
	# 3. rewrite file 1, analyze lines one by one
	ftxt1 = frp[0].readlines()  # text for file 1
	module_flag = False
	i = 0
	while i < len(ftxt1):
		line = ftxt1[i]
		if line.startswith("mod %s is" % module_name[0]):
			# case 1: find target module, add lines around module declaration
			module_flag = True  # in target module now
			addline = "load ../input-modules/" + filename[2]
			fwp.write("%s\n" % addline)
			fwp.write("load ../sampling-lib\n\n")
			fwp.write("%s" % line)
			addline = "  inc " + module_name[2] + " ."
			fwp.write("%s\n" % addline)
			fwp.write("  inc SAMPLING-LIB .\n")
		elif module_flag and is_start_within_list(line, ["rl", "crl"]):
			# case 2: find rule target module
			rule, i = extract_rule_info(ftxt1,i)
			#fwp.write("  --- %s - %s - %d\n" % (rule.type, rule.name, i))
			rewrite_rule_p(fwp, rule, rname2delta_sort, rname2tpls)
		elif line.startswith("endm"):
			# case 3: a module ends, clear module flag
			module_flag = False
			fwp.write("%s" % line)
		else:
			# case default: line with no need for process
			fwp.write("%s" % line)
		i += 1
		
	# 4. rewrite file 2
	ftxt2 = frp[1].readlines()  # text for file 2
	importation = ["inc", "including", "pr", "protecting", "ex", "extending"]
	generate_init_file_p(fwp2, ftxt2, importation, rname2tpls['init'])
	
	# close file
	for fp in frp:
		fp.close()
	fwp.close()
	fwp2.close()


'''
Generate file 2 as required in p-trans
Input: 
	fwp: file write pointer for file 2;
	lines: string list of file 2;
	imp_ls: list for importation reserved words;
	tp_init: the tuple of init
Output: no return value, but write p-trans init file in fwp file
'''
def generate_init_file_p(fwp, lines, imp_ls, tp_init):
	i = 0
	imp_ls.append("mod ")
	# find the insertion position
	insert_pos = -1
	while i < len(lines):
		if is_start_within_list(lines[i], imp_ls):
			insert_pos = i
		i += 1
	if insert_pos == -1:
		print("Error. Generate initial file failed.")
	# insert rule
	i = 0
	while i < len(lines):
		fwp.write(lines[i])
		if i == insert_pos:
			fwp.write("\n")
			fwp.write("  rl [delay-init-1] :\n")
			fwp.write("    { delay-init(@OBJS:Objects,@MSGS:Msgs,(@M:Msg :: @ML:MsgList)) @C:Config | @T:Float }\n")
			fwp.write("  =>\n")
			fwp.write("    { delay-init(@OBJS:Objects,@MSGS:Msgs,@ML:MsgList) @C:Config [@T:Float + (sample(%s)[rand]), @M:Msg] | @T:Float } .\n\n" % tp_init[1])
			fwp.write("  rl [delay-init-2] : delay-init(@OBJS:Objects,@MSGS:Msgs,nil) => null .\n\n")
		i += 1


'''
Rewrite rule as required in p-trans
Input:
	fwp: file write pointer;
	rule: a Rule instance;
	rname2delta_sort: map from rule name to preimage sort of delta function;
	rname2tpls: map from rule name to tpls tuples
Output: no return value, but write p-trans rule in fwp file
'''
def rewrite_rule_p(fwp, rule, rname2delta_sort, rname2tpls):
	if rule.name in rname2delta_sort:
		tp = rname2tpls[rule.name]
	# 1. rewrite rule. If rule in delta, write more
	fwp.write("  %s [%s] :\n  {\n" % (rule.type, rule.name))
	for item in rule.round_left:
		fwp.write("    %s\n" % item)
	for item in rule.angle_left:
		fwp.write("    %s\n" % item)
	fwp.write("    @OBJS:Objects @DMS:DMsgs | @T:Float\n  }\n")
	fwp.write("  =>\n  {\n")
	for item in rule.angle_right:
		fwp.write("    %s\n" % item)
	if rule.name in rname2delta_sort:
		fwp.write("    delay%s,sort(" % tp[2][5:-1])
		for item in rule.round_right:
			fwp.write(item + ' ')
		fwp.write("))\n")
	fwp.write("    @OBJS:Objects @DMS:DMsgs | @T:Float\n  }")
	if rule.type == "crl":
		fwp.write("\n  if %s .\n\n" % rule.condition)
	else:
		fwp.write(" .\n\n")
	# define delay-xxx
	if rule.name in rname2delta_sort:
		fwp.write("  op delay-%s : %s MsgList -> DTask .\n" % (rule.name, rname2delta_sort[rule.name]))
		fwp.write("  rl [delay-%s-1] :\n" % rule.name)
		fwp.write("    { delay%s,(@M:Msg :: @ML:MsgList)) @C:Config | @T:Float }\n" % tp[2][5:-1])
		fwp.write("  =>\n")
		fwp.write("    { delay%s,@ML:MsgList) @C:Config\n" % tp[2][5:-1])
		fwp.write("    [@T:Float + (%s[sample(%s)[rand]]), @M:Msg] | @T:Float } .\n" % (tp[2], tp[1]))
		fwp.write("  rl [delay-%s-2] : delay%s,nil) => null .\n\n" % (rule.name, tp[2][5:-1]))
	# 2. only <> in rule left
	if len(rule.round_left) == 0:
		if rule.type == "crl":
			fwp.write("  ceq objectEnabled(")
		else:
			fwp.write("  eq objectEnabled(")
		for item in rule.angle_left:
			fwp.write(item + ' ')
		fwp.write(")\n    = true")
		if rule.type == "crl":
			fwp.write(" if %s .\n\n" % rule.condition)
		else:
			fwp.write(" .\n\n")


'''
Get tpls info from file 3
Input: lines: string list of file 3
Output:
	delta_sort_map: map from rule name "xxx" to preimage sort of "delta-xxx" (in other words, the string of sort before "->");
	tpls: list of tuples, as defined by "eq tpls =" in file 3
'''
def get_tpls_info(lines):
	# map from rule name "xxx" to preimage sort of "delta-xxx"
	delta_sort_map = {}
	# list of tpls
	tpls = []
	i = 0
	while i < len(lines):
		line = lines[i]
		if is_start_within_list(line, ["op delta-"]):
			# get delta function declaration
			decl_text, i = get_stmt_from(lines, i)
			p = decl_text.index('-')
			q = decl_text.index(':')
			rule_name = decl_text[p + 1:q].strip()
			p = decl_text.index("->", q)
			preimage_sort = decl_text[q + 1:p].strip()
			delta_sort_map[rule_name] = preimage_sort
		elif is_start_within_list(line, ["eq tpls"]):
			# get tpls
			tpls_text, i = get_stmt_from(lines, i)
			p = tpls_text.index('=')
			while tpls_text.find(";;", p) != -1:
				# for each tuple, like [xxx, yyy(, zzz)]
				tp_text, p = get_text_between(tpls_text, p, '[', ']')
				p += 2
				tp_text = tp_text.strip("[ ]") + '\n'
				cnt1 = 0  # round bracket cnt stack
				j = 0
				q = 1
				tp = []  # tuple
				while j < len(tp_text):
					# get each element in tuple [xxx, yyy(, zzz)]
					c = tp_text[j]
					if c == '\n' or (c == ',' and cnt1 ==0):
						# find a tuple element
						tp.append(tp_text[q:j].strip())
						q = j + 1
					elif c == '(':
						cnt1 += 1
					elif c == ')':
						cnt1 -= 1
					j += 1
				tpls.append(tuple(tp))
		i += 1
	
	# debuging info
	'''
	print(delta_sort_map)
	for item in tpls:
		print(item)
	'''
	return delta_sort_map, tpls


'''
Extract info of the rule start from line i in lines
Input: 
	lines: string list of file 1;
	i: start line index
Output:
	rule: an instance of class Rule;
	j: the line index of the last line of the rule statement
'''
def extract_rule_info(lines, i):
	# 1. get the rule text from line i
	rule_text, j = get_stmt_from(lines, i)
	
	# 2. extract info
	# 2.1 rule type
	if rule_text.startswith("rl"):
		rule_type = "rl"
	elif rule_text.startswith("crl"):
		rule_type = "crl"
	rule = Rule(rule_type)
	# 2.2 rule name
	name, i = get_text_between(rule_text, 2, '[', ']')
	rule.name = name.strip("[ ]")
	# 2.3 left of =>
	i += 1
	while not (rule_text[i] == '=' and rule_text[i+1] == '>'):
		if rule_text[i] == '(':
			bracket, i = get_text_between(rule_text, i, '(', ')')
			rule.round_left.append(bracket)
		elif rule_text[i] == '<':
			bracket, i = get_text_between(rule_text, i, '<', '>')
			rule.angle_left.append(bracket)
		i += 1
	if rule_text[i+1] == '>':
		i += 2
	else:
		print("Error: extract_rule_info failed. => not found.")
	# 2.4 right of =>
	'''
	# deprecated. Ask for () for anything not in <> at right
	while rule_text[i] != '.' and not (rule_text[i] == 'i' or rule_text[i+1] == 'f'):
		if rule_text[i] == '(':
			bracket, i = get_text_between(rule_text, i, '(', ')')
			rule.round_right.append(bracket)
		elif rule_text[i] == '<':
			bracket, i = get_text_between(rule_text, i, '<', '>')
			rule.angle_right.append(bracket)
		i += 1
	'''
	round_text = ""
	while rule_text[i] != '.' and not (rule_text[i] == 'i' and rule_text[i+1] == 'f'):
		c = rule_text[i]
		if c != '<':
			round_text += c
		else:
			bracket, i = get_text_between(rule_text, i, '<', '>')
			rule.angle_right.append(bracket)
		i += 1
	round_text.strip()
	if round_text != "":
		rule.round_right.append(round_text)
	
	# 2.5 condition for crl
	if rule.type == "crl":
		if rule_text[i] == 'i' and rule_text[i+1] == 'f':
			i += 3
			rule.condition = rule_text[i:-2]
		else:
			print("Error: extract_rule_info failed. \"if\" not found in crl.")
	
	# 3. debuging info: show rule
	'''
	print("--------")
	print(rule_text)
	print("RoundRight:%s!" % round_text)
	rule.show()
	'''
	return rule, j


