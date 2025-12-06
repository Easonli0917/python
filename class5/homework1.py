# 使用 turtle 秒轉不同方向的正方形繪制程式
import turtle as t

# 設定一亟为最快速度
t.speed(0)
# 設定一亟的形狀
t.shape("turtle")
# 設定一亟的顏色
t.color("green")
# 一亟不描画，只走位置
t.penup()
# 外輫轡迴圈，重複 100 次
for i in range(100):
    # 內輫迴圈，每次二乙方向相關8次
    for a in range(8):
        # 向前出方 100 部
        t.forward(100)
        # 打印一乙的形狀
        t.stamp()
        # 反方向（轉 180 度）
        t.left(180)
        # 向前出方 100 部
        t.forward(100)
        # 反方向（轥 180 度）
        t.left(180)
        # 旋轉 45 度
        t.right(45)
    # 這一轢完成後，清佐畫布
    t.clear()
# 保持窗口
t.done()
