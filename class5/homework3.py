n = input("請輸入一個數字:")
t = input("請再輸入一個數字:")
th = input("請再輸入一個數字:")
n = int(n)
t = int(t)
th = int(th)
for i in range(1, th + 1):
    if i % n == 0 or i % t == 0:
        print(i)
