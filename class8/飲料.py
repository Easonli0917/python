# 飲料販賣機程式
# 建立飲料列表
juice_list = ["蘋果汁", "柳橙汁", "葡萄汁", "可樂", "系統關閉"]

# 使用 while True 建立無限迴圈，直到使用者選擇系統關閉
while True:
    # 使用 for 迴圈逐一顯示飲料列表，搭配編號
    for index in range(len(juice_list)):
        print(f"{index + 1}. {juice_list[index]}")
    # 要求使用者輸入飲料編號
    choice = int(input("請輸入編號:"))
    # 檢查輸入的編號是否有效（1 到列表長度之間）
    if choice < 1 or choice > len(juice_list):
        print("輸入錯誤查無此果汁，請重新輸入")
        # 使用 continue 跳過本次迴圈，重新顯示菜單
        continue
    # 檢查使用者是否選擇系統關閉選項
    if choice == len(juice_list):
        print("~~系統關閉~~")
        # 使用 break 跳出 while 迴圈，結束程式
        break
    # 顯示使用者選擇的飲料（choice - 1 是因為列表索引從 0 開始）
    print(f"您點的商品是{juice_list[choice - 1]}")
