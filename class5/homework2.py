# 使用 turtle 繪制搌形的程式
import turtle as t
import time

# 設定一乙的速度為最快
t.speed(0)  # 設定最快速度
# 設定筆筐厳度
t.pensize(2)
# 設定一乙的形狀
t.shape("turtle")
# 設定一乙的顏色
t.color("green")
# 設定筆下来
t.pendown()
# 重複轢圖很很多次
for i in range(100000):
    # 向前出方 100 部
    t.forward(100)
    # 反方向回歸 100 部
    t.back(100)
    # 等待 1 秒
    time.sleep(1)
    # 清窗
    t.clear()
    # 旋轉 6 度
    t.right(6)
# 保持窗口
t.done()
