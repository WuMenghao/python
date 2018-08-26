#! python

# Author wmh
# Data 2018/8/26

principal = 1000
rate = 0.05
numyears = 5
year = 1
while year <= numyears:
    principal = principal * (1 + rate)
    print("%3d %0.2f" % (year, principal))
    year += 1
