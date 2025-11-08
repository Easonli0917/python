try:
    F = float(input("請輸入華氏溫度："))
    c = (F - 32) * 5 / 9
    print(f"你輸入的溫度是華氏{F}度,是攝氏溫度是{c}度")
except:
    print("你輸入的不是數字")
