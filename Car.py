import turtle
def main():
    wns = turtle.Screen()
    def banh_xe(bichthuy):
        bichthuy.shape("circle")
        bichthuy.shapesize(0.1,0.1)
        bichthuy.speed(10)
        bichthuy.pensize(5)
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

    wns.bgcolor("#1aff8c")

    def annyong(mauu):
        ngoc = turtle.Turtle()
        ngoc.color("#00e673")
        ngoc.penup()
        ngoc.forward(mauu)
        ngoc.pendown()
        ngoc.begin_fill()
        banh_xe(ngoc)
        ngoc.end_fill()

    annyong(-2*150)
    annyong(-1*150)
    annyong(0*150)
    annyong(1*150)

    thy = turtle.Turtle()
    thy.color("#00cc66")
    thy.penup()
    thy.forward(-3*150)
    thy.pendown()
    thy.begin_fill()
    banh_xe(thy)
    thy.end_fill()

    thuy = turtle.Turtle()
    thuy.color("#00cc66")
    thuy.penup()
    thuy.forward(2*150)
    thuy.pendown()
    thuy.begin_fill()
    banh_xe(thuy)
    thuy.end_fill()

    jordan = turtle.Turtle()
    jordan.color("#00b359")
    jordan.pensize(6)
    jordan.penup()
    jordan.left(90)
    jordan.forward(150)
    jordan.right(90)
    jordan.forward(-150)
    jordan.pendown()
    jordan.write("Can you see the movement of the car?", move=False, align="center", font =("TimesNewRoman",40,"bold"))
    wns.exitonclick()

main()
