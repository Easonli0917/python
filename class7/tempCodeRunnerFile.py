# 輸入要跳繩的次數
jump = int(input("請輸入要跳繩的次數："))

# 跳繩
for i in range(1, jump + 1):
    if i % 10 == 0:
        print("休息一下")
        continue
    print("第" + str(i) + "次跳繩")
