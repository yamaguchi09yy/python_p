import turtle
import random

turtle.Screen().bgcolor("#b0c4de")  # 背景の色

snowflakes = []  # snowの座標を格納するリスト

# elsaのコード Turtleクラスのオブジェクトの設定
elsa = turtle.Turtle()
elsa.speed(3)  # 速さ
elsa.width(3) # 線の太さ
elsa.hideturtle() # 矢印を非表示
elsa.penup() # ペンを上げて移動
elsa.forward(90) # 90px進む
elsa.left(45) # 左に45度回転
elsa.pencolor("white") # ペンの色はwhite
elsa.pendown() # ペンを下してスタート

#　elsaのパターンを描く関数
def branch():
    for i in range(3): #外側のforを3回繰り返され、その中で内側のforを3回繰り返す
        for i in range(3):
            elsa.forward(30)
            elsa.backward(30)
            elsa.right(45)
        elsa.left(90)
        elsa.backward(30)
        elsa.left(45)
    elsa.right(90)
    elsa.forward(90)

for i in range(8): #branchを8回繰り返す
    branch()
    elsa.left(45)

# snowのコード Turtleクラスのオブジェクトの設定
snow = turtle.Turtle()
snow.hideturtle()

# snowを描くコード
for _ in range(10):  
    snow.color("#e0ffff")  # スタートの色
    snow.speed(0)  # 速さ

    while True:  # ランダムな位置に配置
        x = random.randint(-300, 300) # 範囲の整数値をランダムに取得
        y = random.randint(-300, 300)

        if all(abs(x - sx) >= 150 or abs(y - sy) >= 150 for sx, sy in snowflakes):  # 150px以上離れているか確認
            snowflakes.append((x, y)) #条件が満たされたらsnowflakesに追加します。
            break

    snow.penup()  # ペンを上げて移動
    snow.goto(x, y)  # ランダムな座標に移動
    snow.pendown()  # ペンを下してスタート

    for _ in range(10):  # 10回繰り返す
        for _ in range(2):  # 2回繰り返す
            snow.forward(20)  # 20px進む
            snow.right(60)  # 右に60度回転
            snow.forward(20)  # 20px進む
            snow.right(120)  # 右に120度回転
        snow.right(36)  # 右に36度回転

    snow.penup()  # 次の雪を配置する位置に移動

    
turtle.done()