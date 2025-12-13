# ===============================
# 練習：天氣播報員
# 功能：讓使用者選擇要修改一週中的哪一天天氣
# ===============================

# 建立一週的天氣預報清單（index 0 ~ 6 代表星期一到星期日）
weather = ["晴天", "多雲", "雨天", "晴天", "多雲", "雷陣雨", "晴天"]

# 先印出目前的天氣預報
print(weather)

# 使用 while True 建立無限迴圈，直到使用者輸入正確為止
while True:
    # 要求使用者輸入要修改的星期（1~7）
    day = input("請輸入要修改的星期數字(1~7)：")

    # 檢查輸入是否為「數字」，使用 isdigit() 方法
    # isdigit() 回傳 True 如果字串中的所有字符都是數字
    if not day.isdigit():
        # 如果不是數字，提示使用者並重新輸入
        print("請輸入數字編號")
        # 使用 continue 跳過本次迴圈，回到 while 重新輸入
        continue

    # 把字串轉成整數以便進行數值比較
    day = int(day)

    # 檢查輸入的數字範圍是否在 1 到 7 之間
    if day < 1 or day > 7:
        # 如果範圍不正確，提示錯誤並要求重新輸入
        print("輸入錯誤查無此星期，請重新輸入")
        # 使用 continue 跳過本次迴圈，回到 while 重新輸入
        continue

    # 如果能走到這裡，代表輸入正確（是數字且在 1~7 範圍內）
    # 使用 break 跳出 while 迴圈
    break

# 確認訊息：告訴使用者他選的是星期幾
print(f"您要修改的星期是 {day}")

# 因為清單 index 從 0 開始，但使用者輸入的是 1~7
# 所以需要將使用者的輸入減去 1 來對應正確的 index
index = day - 1

# 顯示原本該天的天氣
print(f"原本的天氣是 {weather[index]}")

# 要求使用者輸入新的天氣內容
new_weather = input("請輸入新的天氣：")

# 修改清單中指定位置的天氣內容
# 使用 index 作為索引，將新天氣寫入清單
weather[index] = new_weather

# 顯示修改後的結果
print(f"修改後的天氣是 {new_weather}")

# 印出整個更新後的天氣預報清單
print(weather)
