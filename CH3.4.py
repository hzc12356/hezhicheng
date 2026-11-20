# 输入两个坐标列表，各2个整数
p1 = list(map(int, input("输入第一个点坐标 x1 y1：").split()))
p2 = list(map(int, input("输入第二个点坐标 x2 y2：").split()))
d = abs(p1[0] - p2[0]) + abs(p1[1] - p2[1])
print("曼哈顿距离：", d)
