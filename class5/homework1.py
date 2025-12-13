# 使用 turtle 繪制旋轉正方形的程式
# 匯入 turtle 模組並取別名為 t
import turtle as t

# 設定烏龜的速度為最快
t.speed(0)
# 設定烏龜的形狀
t.shape("turtle")
# 設定烏龜的顏色為綠色
t.color("green")
# 抬起筆，不描畫只移動位置
t.penup()
# 外層迴圈，重複 100 次旋轉正方形
for i in range(100):
    # 內層迴圈，每次繪制 8 個方向
    for a in range(8):
        # 向前移動 100 步
        t.forward(100)
        # 打印烏龜的形狀
        t.stamp()
        # 向左轉 180 度（反方向）
        t.left(180)
        # 向前移動 100 步
        t.forward(100)
        # 向左轉 180 度（反方向）
        t.left(180)
        # 向右轉 45 度
        t.right(45)
    # 完成一次迴圈後，清除畫布
    t.clear()
# 保持視窗
t.done()
