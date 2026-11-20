lst = list(map(float, input("输入列表元素，逗号分隔：").split(',')))
lst_sorted = sorted(lst)  # 内置函数sorted排序
max_val = max(lst)
avg = sum(lst) / len(lst)

print("排序后的列表：", lst_sorted)
print("最大值：", max_val)
print("均值：", avg)
