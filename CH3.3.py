lst = list(map(int, input("请输入若干整数，空格隔开：").split()))
res = 1
for num in lst:
    res *= num
print("连乘结果：", res)
