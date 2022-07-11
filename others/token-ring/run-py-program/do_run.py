'''
Doing the work of run.sh
2022.7.9 15:41 +0800
'''
from __future__ import print_function
import os
import sys
import re
import time
import do_p_trans
import do_m_trans
import do_call_pvesta

'''
Global flag for brief terminal display
0: All details, including P/M-trans, time, memory in terminal and result
10: Only info about calling pvesta in terminal and brief result 
2022.7.9 15:41 +0800
'''
global BRIEF_PRINT
BRIEF_PRINT = 10

'''
Get file and module name from sys.argv with smc mode
Input: smc: "off" or "on"
Output: 
	filename: the filename of the file
	module_name: the uppercase respective module name
'''
def get_file_module_name_smc(smc):
	if smc == "off":
		a = 3
	else:
		a = 4
	filename = sys.argv[4:4 + a]  # get filename
	module_name = []
	for fn in filename:  #get module name with uppercase
		mn = fn[0:-6].upper()
		module_name.append(mn)
	return filename, module_name


'''
Generate p-trans file by calling funciton in do_p_trans.py
Input: no parameter, but sys.argv are needed
Output: no return value, but generate p-trans files and print info on terminal
'''
def generate_p_trans_file():
	# No need to print. 2022.7.9 15:41 +0800
	if BRIEF_PRINT <= 0:
		print("Generating P-trans files")
	if sys.argv[3] == "-tr":
		# get filename, module name
		filename, module_name = get_file_module_name_smc("off")
	else:
		print("Parameter error . Failed.")
		sys.exit()
	do_p_trans.process_file_p(filename, module_name)
	# No need to print. 2022.7.9 15:41 +0800
	if BRIEF_PRINT <= 0:
		print("Generating P-trans files: success.")


'''
Generate m-trans file by calling funciton in do_p_trans.py
Input: no parameter, but sys.argv are needed
Output: no return value, but generate m-trans files and print info on terminal
'''
def generate_m_trans_file():
	# No need to print. 2022.7.9 15:41 +0800
	if BRIEF_PRINT <= 0:
		print("Generating M-trans files")
	if sys.argv[3] == "-tr":
		# get filename, module name
		filename, module_name = get_file_module_name_smc("on")
	else:
		print("Parameter error. Failed.")
		sys.exit()
	do_m_trans.process_file_m(filename, module_name)
	# No need to print. 2022.7.9 15:41 +0800
	if BRIEF_PRINT <= 0:
		print("Generating M-trans files: success.")


'''
Call pvesta
Input: no parameter, but sys.argv are needed
Output: no return value, but pvesta results are stored in file result.txt
'''
def call_pvesta():
	print("Calling PVeStA")
	if sys.argv[8] == "-pv":
		para = sys.argv[9:13]
	else:
		print("Parameter error. Failed.")
		sys.exit()
	if len(sys.argv) >=14 and sys.argv[13].startswith("-moni"):
		if len(sys.argv) >=15 and sys.argv[14].startswith("-mlog"):
			err_code = do_call_pvesta.call_pvesta_with_monitor(para, 1)
		else:
			err_code = do_call_pvesta.call_pvesta_with_monitor(para, 0)
	else:
		err_code = do_call_pvesta.call_pvesta(para)
	if err_code == 0:
		print("Calling PVeStA: success.")


'''
Get time now as ms from epoch
Output: ms from epoch
'''
def get_timestamp():
	return time.time()


if __name__ == "__main__":
	# No need to print. 2022.7.9 15:41 +0800
	if BRIEF_PRINT <= 0:
		print("Actors2PMaude starts")
	ts1 = get_timestamp()  # timestamp1
	if sys.argv[1] == "-smc":
		smc = sys.argv[2]
	else:
		print("Parameter error. Failed.")
	if smc == "off":
		# smc off
		generate_p_trans_file()
		ts2 = get_timestamp()  # timestamp2
		# No need to print. 2022.7.9 15:41 +0800
		if BRIEF_PRINT <= 0:
			print("P-trans time used: %f" % (ts2 - ts1))
	elif smc == "pm":
		# do p-trans and m-trans, for debugging
		generate_p_trans_file()
		ts2 = get_timestamp()  # timestamp2
		generate_m_trans_file()
		ts3 = get_timestamp()  # timestamp3
	elif smc == "on":
		# smc on
		generate_p_trans_file()
		ts2 = get_timestamp()  # timestamp2
		generate_m_trans_file()
		ts3 = get_timestamp()  # timestamp3
		call_pvesta()
		ts4 = get_timestamp()  # timestamp4
		# No need to print. 2022.7.9 15:41 +0800
		if BRIEF_PRINT <= 0:
			print("Analysis done (see also result.txt):")
			wrp = open(do_call_pvesta.OUTFILE, "a")
			wrp.write("P-trans time used: %f seconds\n" % (ts2 - ts1))
			wrp.write("M-trans time used: %f seconds\n" % (ts3 - ts2))
			wrp.write("PVeStA time used: %f seconds\n" % (ts4 - ts3))
			wrp.write("Total time used: %f seconds\n" % (ts4 - ts1))
			wrp.close()
			wrp = open(do_call_pvesta.OUTFILE, "r")
			for line in wrp:
				print("%s" % line, end = "")
			wrp.close()
	else:
		print("smc mode error. Failed.")


