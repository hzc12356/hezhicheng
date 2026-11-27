num = int(input("请输入100~999之间的一个整数："))
bai = num // 100
shi = num // 10 % 10
ge = num % 10
sum_cube = bai**3 + shi**3 + ge**3
print(f"各位数字立方和 = {sum_cube}")
