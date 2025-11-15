b = input("請輸你要的箭頭大小:")
b = int(b)
for i in range(b):
    print(" " * (b - i - 1) + "*" * (2 * i + 1))
for i in range(b):
    print(" " * (b - 1) + "*" * 1)
