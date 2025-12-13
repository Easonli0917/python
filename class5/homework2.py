# 使用 turtle 繪制旋轉圖形的程式
# 匯入 turtle 模組並取別名為 t
import turtle as t

# 匯入 time 模組用於延遲
import time

# 設定烏龜的速度為最快
t.speed(0)
# 設定筆的粗度為 2
t.pensize(2)
# 設定烏龜的形狀
t.shape("turtle")
# 設定烏龜的顏色為綠色
t.color("green")
# 放下筆開始繪制
t.pendown()
# 重複迴圈 100000 次
for i in range(100000):
    # 向前移動 100 步
    t.forward(100)
    # 向後移動 100 步
    t.back(100)
    # 等待 1 秒
    time.sleep(1)
    # 清除畫布
    t.clear()
    # 向右轉 6 度
    t.right(6)
# 保持視窗
t.done()
