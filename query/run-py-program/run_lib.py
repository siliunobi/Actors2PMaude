'''
Library used for Actors2pmaude
2022.7.9 21:18 +0800
'''
from __future__ import print_function
import os
import sys
import re


'''
Object Rule
'''
class Rule:
	def __init__(self, tp):
		self.type = tp
		self.name = ""
		self.round_left = []  # round bracket at left
		self.round_right = []  # round bracket / others at right
		self.angle_left = []  # angle bracket at left
		self.angle_right = []  # angle bracket at right
		self.condition = ""  # conditions for crl
	def show(self):
		print(self.type + " - " + self.name)
		if self.type == "crl":
			print("condition:")
			print(self.condition)
		print("left:")
		for item in self.round_left:
			print(item)
		for item in self.angle_left:
			print(item)
		print("right:")
		for item in self.round_right:
			print(item)
		for item in self.angle_right:
			print(item)


'''
Get the shortest string from index pos,
	where the string begins with char s, ends with char t
	and has the same number of s and t.
Input:
	text: string text;
	pos: start position;
	s: start char;
	t: terminal char
Output:
	output1: shortest string described above;
	right: the index number denoting the last position of output1 in input1
For example, get_text_between("12[[][]][]", 1, '[', ']') = ("[[][]]", 7)
'''
def get_text_between(text, pos, s, t):
	cnt = 0
	i = pos
	left = 0
	right = len(text)
	while i < len(text):
		if text[i] == s:
			if cnt == 0:
				left = i
			cnt += 1
		elif text[i] == t and (t != '>' or text[i-1] != '-'):  # there is "|->" in text, need except it
			cnt -= 1
			if cnt == 0:
				right = i
				break
		i += 1
	return text[left:right + 1], right


'''
Get a statement from lines[i]
Input:
	lines: string list;
	i: start line index
Output:
	stmt: a statment begin at lines[i];
	j: the index of the last line of the statement
'''
def get_stmt_from(lines, i):
	j = i
	while not is_end_with_dot(lines[j]):
		j += 1
	stmt = ""
	for k in range(i, j + 1):
		stmt += lines[k][0:-1].strip()
		if k != j:
			stmt += ' '
	return stmt, j


'''
Judge whether a line end with ".",
	space after last char is omitted
Input: line: a line text, which is string
Output: True - this line ends with "."; otherwise, False
Fixed at 2022.7.9 21:18 +0800
'''
def is_end_with_dot(line):
	line = line.strip()
	if line=="":
		return False
	if line[-1] == '.':
		return True
	return False


'''
Judge whether a line start with any string in start_list,
	space before first char is omitted
Input:
	line: a line text, which is string;
	start_list: expected start string
Output: True - this line starts with a string in start_list; otherwise, False
'''
def is_start_within_list(line, start_list):
	i = 0
	while(i < len(line)):
		for st in start_list:
			if line.startswith(st,i):
				return True
		if line[i] != ' ' and line[i] != '\t':
			break
		i += 1
	return False


