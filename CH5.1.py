# 初始化计数
you = 0
liang = 0
zhong = 0
jige = 0
bujige = 0
count = 0

print("请输入成绩，输入-1结束（最多录入10个）：")
while count < 10:
    score = int(input())
    if score == -1:
        break
    # 判断等级
    if score >= 90:
        you += 1
    elif score >= 80:
        liang += 1
    elif score >= 70:
        zhong += 1
    elif score >= 60:
        jige += 1
    else:
        bujige += 1
    count += 1

print(f"优：{you}人")
print(f"良：{liang}人")
print(f"中：{zhong}人")
print(f"及格：{jige}人")
print(f"不及格：{bujige}人")
