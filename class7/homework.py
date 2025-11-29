開始數 = int(input("請輸入開始整數: "))
結束數 = int(input("請輸入結束整數: "))

for 數字 in range(開始數, 結束數 + 1):
    if 數字 > 1:
        是質數 = True
        for 除數 in range(2, int(數字**0.5) + 1):
            if 數字 % 除數 == 0:
                是質數 = False
                break
        if 是質數:
            print(數字)
