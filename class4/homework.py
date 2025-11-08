a = int(input("請輸入身高(公分):"))
b = int(input("請輸重量(公斤):"))
i = b / ((a / 100) ** 2)
if i < 18.5:
    print(f"你的BMI值為:{i}")
    print("體重過輕")
elif i >= 25:
    print(f"你的BMI值為:{i}")
    print("體重過重")
else:
    print(f"你的BMI值為:{i}")
    print("體重正常")
