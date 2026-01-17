def hello(name: str = "Singular") -> None:
    """
    打招呼用的函式

    參數:
    name: str - 姓名

    回傳: None

    範例:
    hello("Alice")  # Hello, Alice!
    """
    print(f"Hello, {name}!")


# 顯示函式說明
print(hello.__doc__)
"""
說明寫在這裡
"""
hello.__doc__

# 檔案讀寫
# 判斷檔案是否存在 - 使用 os.path.isfile() 函式
import os

# 相對路徑代表相對於目前的工作目錄的路徑
# 絕對路徑代表完整的路徑
if os.path.isfile("class17/hw.py"):
    # C:\Users\User\Desktop\python_test\class17\hw.py
    print("檔案存在！")
else:
    print("檔案不存在！")

# open() 開啟模式
# r - 讀取模式、檔案必須存在
# w - 寫入模式、檔案不存在會自動建立
# a - 附加模式、檔案不存在會自動建立
# r+ - 讀取與寫入模式、檔案必須存在
# w+ - 讀取與寫入模式、檔案不存在會自動建立
# a+ - 讀取與附加模式、檔案不存在會自動建立

# 讀取檔案 - 使用 open() 函式
# 例如：
file = open("class18/file_test.py", "r")
print(file.read())
file.close()

# 讀取檔案 - 使用 with open() as
# 例如：
with open("class18/file_test.py", "r") as file:
    print(file.read())

# 寫入檔案 - 使用 open() 函式
# 例如：
file = open("class18/file_test.py", "w")
file.write("print('write file test')")
file.close()


# 寫入檔案 - 使用 with open() as
# 例如：
with open("class18/file_test.py", "w") as file:
    file.write("print('Hello World!')")
