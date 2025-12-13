# 使用 turtle 模組繪製圓形印章圖案的程式
# 匯入 turtle 模組並取別名為 t
import turtle as t

# 設定烏龜的顏色為紅色
t.color("red")
# 設定烏龜的形狀
t.shape("turtle")
# 使用 for 迴圈重複 120 次
for i in range(120):
    # 向前移動 20 步
    t.forward(20)
    # 打印烏龜的形狀（留下印記）
    t.stamp()
    # 向右轉 8 度
    t.right(8)
# 保持視窗
t.done()
# 更新畫面顯示
t.tracer()
