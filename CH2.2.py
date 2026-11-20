# 输入两个集合，以逗号分隔数字
s1 = set(map(int, input("请输入第一个集合元素，用逗号隔开：").split(',')))
s2 = set(map(int, input("请输入第二个集合元素，用逗号隔开：").split(',')))

jiaoji = s1 & s2
bingji = s1 | s2
chaji1 = s1 - s2  # s1有、s2没有
chaji2 = s2 - s1  # s2有、s1没有

print("交集：", jiaoji)
print("并集：", bingji)
print("s1 - s2 差集：", chaji1)
print("s2 - s1 差集：", chaji2)
