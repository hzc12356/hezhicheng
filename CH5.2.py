for num in range(1,10000):
    s = str(num)
    n = len(s)   # 获取数字位数
    total = 0
    for ch in s:
        digit = int(ch)
        total += digit ** n
    if total == num:
        print(num)
