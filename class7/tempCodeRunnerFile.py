# 跳繩模擬程式
# 要求使用者輸入要跳繩的總次數
jump = int(input("請輸入要跳繩的次數："))

# 使用 for 迴圈模擬跳繩過程
for i in range(1, jump + 1):
    # 檢查是否達到 10 的倍數（每跳 10 次就休息一下）
    if i % 10 == 0:
        # 打印休息訊息
        print("休息一下")
        # 使用 continue 跳過本次迴圈的其他程式碼
        continue
    # 打印當前跳繩的次數
    print("第" + str(i) + "次跳繩")

# call by value
# 在「基本型別」下，傳遞參數時會採用 call by value 的方式

a = 1
b = a  # 將 a 的值指定給 b
b = 2
print(a, b)


# call by reference
a = [1, 2, 3]
b = a  # 記憶體指向同一個位置，所以改 b 會影響 a
b[0] = 2
print(a, b)


a = [1, 2, 3]
b = a.copy()  # 複製一份新的物件，但內層資料不會共用記憶體位置
b[0] = 2
print(a, b)
