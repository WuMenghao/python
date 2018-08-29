#! python

# Author wmh
# Data 2018/8/26

import basicoperations.virables

f1 = open("E:\\Data\\text\\file01.txt", "w+", encoding="utf-8")
print("Hello", file=f1)
f1.flush()
f1.close()
# while virables.year <= virables.numyears:
#     virables.principal = virables.principal * (1 + virables.rate)
#     f.write("%3d %0.2f" % (virables.year, virables.principal))
#     f.flush()
#     virables.year += 1
# f.close()

f2 = open("E:\\Data\\text\\file01.txt", "w+", encoding="utf-8")
line = f2.readline()
while line:
    print(line)
    line = f2.readline()
f2.close()