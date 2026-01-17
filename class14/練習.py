水果 = {"蘋果": 25, "香蕉": 20, "橘子": 30}


def edit():
    新水果 = input("請輸入你要新增的水果名稱:")
    新價格 = input(f"請輸入{新水果}的價格")
    水果[新水果] = 新價格
    print(新水果, "以新增，價格", 新價格)


def add():
    新水果 = input("請輸入你要修改的水果名稱:")
    新價格 = input(f"請輸入{新水果}的新價格")
    水果[新水果] = 新價格
    print(新水果, "以修改為", 新價格, "元")


def delete():
    新水果 = input("請輸入你要刪除的水果名稱:")
    del 水果[新水果]
    print(新水果, "以刪除")


while True:
    print("目前水果價格")
    for key in 水果:
        print(key, ":", 水果[key], "元")
    print("1.新增水果價格")
    print("2.修改水果價格")
    print("3.刪除水果")
    print("4.離開")
    選擇 = input("請選擇功能(1~4): ")
    if 選擇 == "1":
        edit()
    elif 選擇 == "2":
        add()
    elif 選擇 == "3":
        delete()
    elif 選擇 == "4":
        print("感謝使用水果店價格諮詢系統")
        break
    else:
        print("請輸入正確的選項")


水果 = {"蘋果": 25, "香蕉": 20, "橘子": 30}


def edit():
    """修改水果價格"""
    新水果 = input("請輸入你要新增的水果名稱:")
    新價格 = input(f"請輸入{新水果}的價格")
    水果[新水果] = 新價格
    print(新水果, "以新增，價格", 新價格)


def add():
    """新增水果價格"""
    新水果 = input("請輸入你要修改的水果名稱:")
    新價格 = input(f"請輸入{新水果}的新價格")
    水果[新水果] = 新價格
    print(新水果, "以修改為", 新價格, "元")


def delete():
    """刪除水果"""
    新水果 = input("請輸入你要刪除的水果名稱:")
    del 水果[新水果]
    print(新水果, "以刪除")


功能清單 = [add, edit, delete]

while True:
    print("目前水果價格")
    for key in 水果:
        print(key, ":", 水果[key], "元")
    for i, 功能 in enumerate(功能清單, start=1):
        print(f"{i}. {功能.__doc__}")
    print(f"{len(功能清單)+1}. 離開系統")

    選擇 = int(input("請選擇功能(1~4): "))
    if 選擇 == (len(功能清單) + 1):
        print("感謝使用水果店價格查詢系統")
        break
    else:
        功能清單[選擇 - 1]()
    print("=" * 26)
