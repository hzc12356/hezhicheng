# 输入并转int
a1 = int(input("请输入首项："))
q = int(input("请输入公比(≠1，<36)："))
n = int(input("请输入项数n："))

s = a1 * (q**n - 1) / (q - 1)
# 关键：用int()转为整数
s = int(s)
print("前n项和 =", s)
