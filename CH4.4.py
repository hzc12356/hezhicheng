s = input("请输入字符串：")
freq = {}

for ch in s:
    if ch.isalnum():   # 判断是否字母或数字
        if ch in freq:
            freq[ch] += 1
        else:
            freq[ch] = 1

print("字母、数字频数字典：", freq)
