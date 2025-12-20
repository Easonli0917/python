# 🎉 我的超市購物清單管家 🎉
# 功能：建立一個購物清單管理系統，支援新增、修改、刪除等操作

# 建立一個空的購物清單
shopping_list = []

# 使用 while True 建立無限迴圈，直到使用者選擇離開
while True:
    # 顯示目前的購物清單
    print("\n🛒 目前清單:", shopping_list)
    # 顯示選單選項
    print("你想做什麼？")
    print("1. 新增東西")
    print("2. 修改東西")
    print("3. 刪除東西")
    print("4. 離開")

    # 要求使用者輸入選擇
    choice = input("輸入 1~4: ")

    # 功能 1：新增東西
    if choice == "1":
        # 要求使用者輸入要新增的東西
        item = input("要新增什麼東西？ ")
        # 詢問使用者是否要加到最後或插入某個位置
        print("a. 加到最後  b. 插入某個位置")
        add_choice = input("選 a 或 b: ")
        # 如果選擇 a，使用 append() 將東西加到清單最後
        if add_choice == "a":
            shopping_list.append(item)
            print(f"✅ {item} 已加入清單最後！")
        # 如果選擇 b，使用 insert() 將東西插入到指定位置
        elif add_choice == "b":
            pos = int(input("要插入到第幾個位置？(從0開始) "))
            shopping_list.insert(pos, item)
            print(f"✅ {item} 已插入第 {pos} 個位置！")
        # 如果選擇不是 a 或 b，提示錯誤
        else:
            print("❌ 選錯了！")

    # 功能 2：修改東西
    elif choice == "2":
        # 檢查清單是否為空
        if len(shopping_list) == 0:
            print("❌ 清單是空的，沒東西可以修改")
        else:
            # 使用 enumerate() 顯示清單中的每一項和其位置
            for i, it in enumerate(shopping_list):
                print(i, it)
            # 要求使用者輸入要修改的位置
            pos = int(input("要修改哪一個位置？ "))
            # 要求使用者輸入新的東西
            new_item = input("新的東西是什麼？ ")
            # 保存舊的東西用於顯示訊息
            old_item = shopping_list[pos]
            # 修改指定位置的元素
            shopping_list[pos] = new_item
            print(f"✏️ {old_item} 已改成 {new_item}！")

    # 功能 3：刪除東西
    elif choice == "3":
        # 檢查清單是否為空
        if len(shopping_list) == 0:
            print("❌ 清單是空的，沒東西可以刪除")
        else:
            # 提供兩種刪除方式：按名字或按位置
            print("a. 用名字刪除  b. 用位置刪除")
            del_choice = input("選 a 或 b: ")
            # 方式 a：按名字刪除
            if del_choice == "a":
                name = input("要刪掉哪個東西？ ")
                # 檢查該東西是否在清單中
                if name in shopping_list:
                    # 使用 remove() 刪除指定名字的東西
                    shopping_list.remove(name)
                    print(f"🗑️ {name} 已刪掉！")
                else:
                    print("❌ 沒有這個東西！")
            # 方式 b：按位置刪除
            elif del_choice == "b":
                pos = int(input("要刪掉哪一個位置？ "))
                # 使用 pop() 刪除指定位置的元素，並返回被刪除的值
                removed = shopping_list.pop(pos)
                print(f"🗑️ {removed} 已刪掉！")
            else:
                print("❌ 選錯了！")

    # 功能 4：離開程式
    elif choice == "4":
        print("👋 掰掰～")
        # 使用 break 跳出 while 迴圈，結束程式
        break

    # 如果輸入的選擇不在 1~4 之間
    else:
        print("❌ 請輸入 1~4 喔！")
