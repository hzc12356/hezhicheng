# 输入，以空格分割
lstA = list(map(int, input("请输入列表A的整数，空格隔开：").split()))
lstB = list(map(int, input("请输入列表B的整数，空格隔开：").split()))
d = dict(zip(lstA, lstB))
print("生成的字典：", d)
