import random
secret = random.randint(1,100)  # 1~100随机数
max_times = 7   # 最多猜7次
for i in range(max_times):
    guess = int(input(f"请猜数字，你还有{max_times-i}次机会："))
    if guess == secret:
        print("恭喜你猜对了！")
        break
    elif guess > secret:
        print("太大了")
    else:
        print("太小了")
else:
    # for循环正常走完（没有break）才执行else
    print(f"次数用完，游戏结束！正确答案是：{secret}")
