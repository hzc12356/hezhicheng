# 方法：当成字符串处理，不怕数字很大
num = input("请输入一个自然数：")
s = 0
for c in num:
    s += int(c)
print("各位数字之和 =", s)
