
num = int(input("请输入一个3位正整数："))
if 100 <= num <= 999:
    hundred = num // 100
    ten = num // 10 % 10
    unit = num % 10
    total = hundred + ten + unit
    print(f"百位={hundred}，十位={ten}，个位={unit}，和={total}")
else:
    print("输入不是3位正整数！")