from functools import reduce

# 示例：包含多个集合的列表，也可以自己输入
set_list = [{1,2,3}, {3,4,5}, {5,6,7}]
# reduce逐个取并集
res = reduce(lambda a,b: a | b, set_list)
print("并集：", res)
