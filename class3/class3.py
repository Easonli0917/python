# try except 錯誤處理
# 當程式在執行過程中,遇到錯誤時,可以不用停止程式,而是去執行except的內容
# 可以用冒號縮牌來區分裡面跟外面
try:
    n = int(input("請輸入一個數字:"))
    print(f"你輸入的數字是{n},再加一是{n+1}  ")
except ValueError:
    print("你輸入的不是數字喔")
except ZeroDivisionError:
    print("你輸入的數字不能是零")
except:
    print("發生其他錯誤")
else:
    print("沒有錯誤")
finally:
    print("不管怎樣都會顯示")

# 比較運算子
print(1 < 2)  # 小於
print(1 <= 2)  # 小於或等於
print(1 == 2)  # 等於
print(1 != 2)  # 不等於
print(1 >= 2)  # 大於或等於
print(1 > 2)  # 大於

# 邏輯運算子
# and 代表全部條件都要為真
print(True and False)
# or 代表全部條件都要為假
print(True or False)
# not 代表全部條件都要為假
print(not True)

# 優先順序
# 1 括號 ()
# 2 ** 指數
# 3 * / // % 乘 除 取商 取餘數
# 4 + - 加 減
# 5 < <= > >= == != 小 小等 大 大等 等於 不等於
# 6 not  非
# 7 and  且
# 8 or  或

# if 條件判斷
# if 後面是條件,如果條件為真,就會執行下面的語句
# 可以有多個elif,一旦條件為真,就會執行下面的語句
# else 後面是執行如果條件為假的語句
pwd = input("請輸入密碼:")
if pwd == "*****":
    print("密碼正確")
elif pwd == "happy":
    print("歡迎回來")
else:
    print("密碼錯誤")

# if elif else 使用時機
# 要一起執行時不能都用if
# 只要執行一個不能多個時用多個if
