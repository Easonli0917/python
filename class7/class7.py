# 質數檢查程式
# 要求使用者輸入一個數字
輸入數字 = int(input("請輸入一個數字： "))

# 檢查輸入的數字是否小於 2
# 小於 2 的數字都不是質數
if 輸入數字 < 2:
    print("不是質數")
else:
    # 先假設輸入的數字是質數
    是不是質數 = True

    # 用迴圈從 2 檢查到 輸入數字 - 1
    # 看是否有其他數字能整除輸入數字
    for 測試數字 in range(2, 輸入數字):
        # 如果輸入數字能被其他數字整除
        if 輸入數字 % 測試數字 == 0:
            # 那它就不是質數
            是不是質數 = False
            # 提早結束迴圈，不用再檢查了
            break

    # 根據檢查結果輸出
    if 是不是質數:
        print("是質數！")
    else:
        print("不是質數！")
# while.......else
# 當迴圈正常結束時,執行else區塊的程式
# example:
i = 0
while i < 5:
    print(i)
    i += 1
else:
    print("while迴圈正常結束")
# 第三次看到else
# else在try......except...finally也會出現,功能是沒有發生意外時會執行else區塊的程式
# else在 if....elif.....else也會出現,功能是當前面的條件當不成立時會執行else區塊的程式

# 倒數計時器
import time

倒數計時的秒數 = int(input("請輸入倒數計時的秒數:"))
while 倒數計時的秒數 > 0:
    print(f"倒數計時:{倒數計時的秒數}秒")
    time.sleep(1)
    倒數計時的秒數 -= 1
else:
    print("倒數計時的秒數")
# 迴圈的break可以用來跳出所屬的迴圈
# 所以判斷break屬哪個迴圈時注意縮排
# 例如:
for i in range(5):
    for j in range(5):
        if i == 2 and j == 2:
            break
        print(f"i:{i},j:{j}")
# 這裡的break只會跳出for迴圈
# 外層的for迴圈還是會執行


# 這是飲料的名字，放在一個列表裡面
飲料清單 = ["蘋果汁", "柳橙汁", "葡萄汁", "系統關閉"]

# 讓我們一直問客人想喝什麼，直到他們說關閉
while True:
    print("請選擇你想喝的飲料：")

    # 用一個小小的數字來幫每個飲料編號，1開始數
    for 編號, 飲料名稱 in enumerate(飲料清單, 1):
        print(f"{編號}. {飲料名稱}")

    # 請客人輸入他們想要的飲料編號
    客人選擇 = input("請輸入編號：")

    # 先檢查看看，客人輸入的是不是數字
    if 客人選擇.isdigit():
        選擇號碼 = int(客人選擇)  # 把字變成數字

        # 檢查數字是不是在1到4的範圍裡
        if 1 <= 選擇號碼 <= 4:

            # 如果選擇的是4，也就是系統關閉
            if 選擇號碼 == 4:
                print("~~系統關閉~~")
                break  # 停止問問題，結束程式

            else:
                # 客人選的是1~3的飲料，就告訴他們點的是什麼
                print(f"您點的商品是{飲料清單[選擇號碼 - 1]}")

        else:
            # 如果數字不在1~4，就告訴客人輸入錯誤
            print("輸入錯誤查無此果汁，請重新輸入")

    else:
        # 如果不是數字，也告訴客人輸入錯誤
        print("輸入錯誤查無此果汁，請重新輸入")


# continue
# 迴圈的 continue 可以用來跳過當前的迴圈，繼續執行下一次的迴圈
# 例如：
for i in range(5):
    if i == 2:
        continue
    print(i)

# 這裡的 continue 會跳過 i = 2 的那次迴圈，直接執行 i = 3 的那次迴圈
# 所以輸出的結果是 0, 1, 3, 4

# continue 也可以用在 while 迴圈中
# 例如：
i = 0
while i < 5:
    if i == 2:
        continue
    print(i)
    i += 1

# continue 也要判斷所屬的迴圈，所以要注意縮排


# 輸入要跳繩的次數
jump = int(input("請輸入要跳繩的次數："))

# 跳繩
for i in range(1, jump + 1):
    if i % 10 == 0:
        print("休息一下")
        continue
    print("第" + str(i) + "次跳繩")
