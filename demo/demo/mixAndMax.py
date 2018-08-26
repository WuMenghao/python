#! python

# Author wmh
# Data 2018/8/26

import sys


class MaxAndMin:
    argv = None

    def __init__(self, argv):
        self.argv = argv

    def getMaxnumAndMixnum(self):
        if len(self.argv) != 2:
            print("Please supply a filename")

        f = open(self.argv[1])
        lines = f.readlines()
        fvalues = [float(line) for line in lines]

        return max(fvalues), min(fvalues)


mn = MaxAndMin(sys.argv)
values = mn.getMaxnumAndMixnum()
print("The Maxnum value is ", values[0])
print("The Minnum value is ", values[1])
