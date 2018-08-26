#! python

# Author wmh
# Data 2018/8/26

# 序列表示索引为非负整数的有序集合，包括字符串、列表和元祖

str = "Hello welcome to python"
lis = [0, 1, 2, 3, 4, 5]
ran = (1, "哈哈", 2.0, lis)

print(str[0:5])             # 返回切片
print(max(lis))             # 最大值
print(ran[1])               # 返回元素
print(all(lis))             # 检查所有项是否为true
print(any(lis))             # 检查任意项是否为true
