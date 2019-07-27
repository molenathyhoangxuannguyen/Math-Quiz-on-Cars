import turtle

def main():

    wns = turtle.Screen()

    def banh_xe(bichthuy):
        bichthuy.shape("circle")
        bichthuy.shapesize(0.1,0.1)
        bichthuy.speed(10)
        bichthuy.pensize(6)

        def ve_hinh_tron(number,cao):
            for i in range(number):
                bichthuy.right(1)
                bichthuy.forward(cao)

        ve_hinh_tron(360, 0.5)

        def ve_tron(solieu, chieucao):
            for i in range(solieu):
                bichthuy.left(1)
                bichthuy.backward(chieucao)

        ve_tron(90, 0.5)
        bichthuy.left(90)
        bichthuy.forward(40)
        bichthuy.right(90)
        ve_hinh_tron(180,2.5)
        bichthuy.right(90)
        bichthuy.forward(40)
        bichthuy.left(90)
        ve_hinh_tron(360, 0.5)
        ve_tron(180, 0.5)
        bichthuy.left(90)
        bichthuy.forward(95)

    wns.bgcolor("#e6e6ff")

    def annyong(mauu, yoona):
        ngoc = turtle.Turtle()
        ngoc.color(yoona)
        ngoc.penup()
        ngoc.forward(mauu)
        ngoc.pendown()
        ngoc.begin_fill()
        banh_xe(ngoc)
        ngoc.end_fill()

    annyong(-3 * 150, "#0000ff")
    annyong(-2*150, "#0000ff" )
    annyong(-1*150, "#0000ff")
    annyong(0*150, "#0000ff")
    annyong(1*150, "#0000ff")
    annyong(2 * 150, "#0000ff")
    annyong(-4*150, "#000066")
    annyong(3*150, "#000066" )

    def nut_that(brother):
        abcxyz = turtle.Turtle()
        abcxyz.dot(6)
        abcxyz.pensize(6)
        abcxyz.penup()
        abcxyz.forward(brother)
        abcxyz.right(90)
        abcxyz.forward(40)
        abcxyz.pendown()
        abcxyz.stamp()

    nut_that(-4*150-40)
    nut_that(4*150+40)

    jordan = turtle.Turtle()
    jordan.color("#0000ff")
    jordan.pensize(6)
    jordan.penup()
    jordan.left(90)
    jordan.forward(200)
    jordan.right(90)
    jordan.forward(0)
    jordan.pendown()
    jordan.write("Can you calculate the distance of AB ?", move=False, align="center", font =("TimesNewRoman",40,"bold"))

    def dau_cuoi_tuong_ung(chieu_rong, chu_cai):
        thy = turtle.Turtle()
        thy.color("#0000ff")
        thy.pensize(6)
        thy.penup()
        thy.forward(chieu_rong)
        thy.right(90)
        thy.forward(50)
        thy.pendown()
        thy.write(chu_cai, move=False, align="center", font=("TimesNewRoman", 40, "bold"))

    dau_cuoi_tuong_ung(-4*150-40,"A")
    dau_cuoi_tuong_ung(4*150+40, "B")

    wns.exitonclick()

main()
