# 使用 turtle 模組繪製圖形的程式
# 匯入 turtle 模組並取別名為 t
import turtle as t

# 設定烏龜的速度為最快
t.speed(-100)  # 設定最快速度
# 設定筆的粗度
t.pensize(10000000000000000000)
# 設定烏龜的形狀
t.shape("turtle")
# 設定烏龜的顏色為綠色
t.color("green")
# 向左轉 90 度
t.left(90)
# 向前移動 10000 步
t.forward(10000)
# 向左轉 90 度
t.left(90)
# 重複迴圈（注意：此程式有語法錯誤，應為 range 而非 inrange）
# for i in range(10000000):
#     t.forward(100000000)
#     t.left(180)
# 保持視窗
t.done()
