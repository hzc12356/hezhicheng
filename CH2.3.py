# 输入列表
lst = list(map(int, input("请输入若干整数，空格分隔：").split()))

# 排序（内置sorted，生成新列表）
sorted_lst = sorted(lst)
# 最大值
max_val = max(lst)
# 均值：总和 / 元素个数
avg_val = sum(lst) / len(lst)

print("排序后的列表：", sorted_lst)
print("最大值：", max_val)
print("均值：", avg_val)

