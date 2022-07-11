'''
Read the pvesta output file
Only reserve result and running time
2022.7.10 20:41 +0800
'''
from __future__ import print_function
import sys


# name for reserved attribute in RP class
reserved_attr = ["result", "time"]
# name for print, accorded with the attribute name
reserved_field = ["Result:", "Running time:"]
SPACE = [' ', '\n', '\t']


class ResultPvesta:
    def __init__(self):
        self.model = ""
        self.formula = ""
        self.alpha = ""
        self.delta1 = ""
        self.samples = ""
        self.result = ""
        self.time = ""
        self.memory = ""

    def show(self):
        print("MFAD: %s, %s, %s, %s" %
              (self.model, self.formular, self.alpha, self.delta1))
        print("SRT: %s, %s, %s" % (self.samples, self.result, self.time))


'''
Read the output file of pvesta client
Input: no parameter, but pvesta output file CLIENT_OUTPUT neeeded
Output:
	rp: a ResultPvesta instance, containing info of pvesta output
'''


def read_client_output(pvesta_output):
    frp = open(pvesta_output, "r")
    rp_ls = []
    rp = ResultPvesta()
    lines = frp.readlines()
    for line in lines:
        if line.startswith("model:"):
            rp.model = get_text_until(line, SPACE, 6)
        elif line.startswith("formula:"):
            rp.formular = get_text_until(line, SPACE, 8)
        elif line.startswith("alpha:"):
            rp.alpha = get_text_until(line, SPACE, 6)
        elif line.startswith("delta1:"):
            rp.delta1 = get_text_until(line, SPACE, 7)
        elif line.startswith("samples generated ="):
            rp.samples = get_text_until(line, SPACE, 19)
        elif line.startswith("Result:"):
            rp.result = get_text_until(line, SPACE, 7)
        elif line.startswith("Running time:"):
            rp.time = get_text_until(line, ['s'], 13).strip()
        t = getattr(rp, "time")
        if t != "":
            rp_ls.append(rp)
            rp = ResultPvesta()
    frp.close()
    return rp_ls


'''
Get text from st_index to char in end_list without SPACE
Input:
	line: a string
	end_list: list of chars, denoting the char after extracted text
	st_index: the start index of line, default 0
Output:
	rt: string, extracted text from line[st_index] to any char in end_list without SPACE
'''


def get_text_until(line, end_list, st_index=0):
    i = st_index
    rt = ""
    while i < len(line):
        c = line[i]
        if c in end_list and rt != "":
            break
        elif c not in SPACE:
            rt = rt + c
        i += 1
    return rt


if __name__ == "__main__":
    file_path = sys.argv[1]
    # print("debug:", file_path)
    # get result list in file
    rp_ls = read_client_output(file_path)
    # rewrite file
    fp = open(file_path, "w")
    for rp in rp_ls:
        # rp.show()
        for i in range(len(reserved_attr)):
            fp.write(
                reserved_field[i] + ' ' +
                getattr(rp, reserved_attr[i]) + '\n')
        fp.write('\n')
    fp.close()
