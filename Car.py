import turtle
from math import pi

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

        def ve_tron(solieu, chieucao):
            for i in range(solieu):
                bichthuy.left(1)
                bichthuy.backward(chieucao)

        ve_hinh_tron(360, 0.5)
        ve_tron(90, 0.5)
        bichthuy.left(90)
        bichthuy.forward(40)
        bichthuy.right(90)
        ve_hinh_tron(180,2.5)
        bichthuy.right(90)
        bichthuy.forward(40)
        bichthuy.right(-90)
        ve_hinh_tron(360, 0.5)
        ve_tron(180, 0.5)
        bichthuy.left(90)
        bichthuy.forward((900/pi)-80-(360/pi))

    wns.bgcolor("#e6ffff")

    def annyong(mauu, yoona):
        ngoc = turtle.Turtle()
        ngoc.color(yoona)
        ngoc.penup()
        ngoc.forward(mauu)
        ngoc.pendown()
        ngoc.begin_fill()
        banh_xe(ngoc)
        ngoc.end_fill()

    annyong(-3 * 150, "#00cc7a")
    annyong(-2*150, "#00e600" )
    annyong(-1*150, "#00cc7a")
    annyong(0*150, "#00e600")
    annyong(1*150, "#00cc7a")
    annyong(2 * 150, "#00e600")
    annyong(-4*150, "#000080")
    annyong(3*150, "#000080" )

    def nut_that(brother):
        abcxyz = turtle.Turtle()
        abcxyz.color("#ffff00")
        abcxyz.shape("circle")
        abcxyz.shapesize(0.1, 0.1)
        abcxyz.pensize(6)
        abcxyz.penup()
        abcxyz.forward(brother)
        abcxyz.right(90)
        abcxyz.forward(35)
        abcxyz.pendown()
        abcxyz.dot()

    nut_that(-4*150-32)
    nut_that(4*150+31)

    conrua = turtle.Turtle()
    conrua.color("#ffff00")
    conrua.shape("circle")
    conrua.shapesize(0.1, 0.1)
    conrua.pensize(6)
    conrua.penup()
    conrua.forward(-4*150)
    conrua.pendown()
    conrua.forward(2*(4*150+30))

    def dau_cuoi_tuong_ung(chieu_rong, chu_cai):
        thy = turtle.Turtle()
        thy.color("#000099")
        thy.pensize(6)
        thy.penup()
        thy.forward(chieu_rong)
        thy.right(90)
        thy.forward(90)
        thy.pendown()
        thy.write(chu_cai, move=False, align="center", font=("TimesNewRoman", 40, "bold"))

    dau_cuoi_tuong_ung(-4*150-45,"A")
    dau_cuoi_tuong_ung(4*150+50, "B")

    jordan = turtle.Turtle()
    jordan.color("#660066")
    jordan.pensize(6)
    jordan.penup()
    jordan.left(90)
    jordan.forward(200)
    jordan.right(90)
    jordan.forward(0)
    jordan.pendown()
    jordan.write("Can you calculate the distance of AB ?", move=False, align="center", font =("TimesNewRoman",40,"bold"))



    wns.exitonclick()

main()
