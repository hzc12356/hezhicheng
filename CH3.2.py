lst = list(map(int, input("请输入若干整数，空格隔开：").split()))
new_lst = sorted(lst, reverse=True)
print("降序新列表：", new_lst)
