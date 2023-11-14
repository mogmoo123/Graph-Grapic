import turtle
import math as m

sd = 0
t = turtle.Pen()

class Funtions:
    def Inverse(k = 1000,leight_min = -200,leight_max = 200,color = 'black',speed = 1):
        
        t.color(color)
        t.up()
        t.goto(leight_min,int(k/leight_min))
        t.down()
        for i in range(leight_min,leight_max,speed):
            if(i != 0):
                #t.up()
                t.goto(i,int(k/i))#식 넣는곳
                #t.down()
                #t.dot(5)
            else:
                pass


    def f(pow = 2,leight_min = -10,leight_max = 10,color = 'black',speed = 1):

        t.color(color)
        t.up()
        t.goto(leight_min,int(m.pow(leight_min,pow)))
        t.down()
        for i in range(leight_min,leight_max,speed):
            #t.up()
            t.goto(i,int(m.pow(i,pow)))#식 넣는곳 
            #t.down()
            #t.dot(5)

    def sinf(leight_min = -200,leight_max = 200,weight = 10,k = 30,color = 'black',speed = 1):
        t.color(color)
        t.up()
        t.goto(leight_min,m.sin(leight_min/weight)*k)
        t.down()
        for i in range(leight_min,leight_max,speed):
            #t.up()
            t.goto(i,m.sin(i/weight)*k)
            ##t.down()
            #t.dot(5)

    def cosf(leight_min = -200,leight_max = 200,weight = 10,k = 30,color = 'black',speed = 1):
        t.color(color)
        t.up()
        t.goto(leight_min,m.cos(leight_min/weight)*k)
        t.down()
        for i in range(leight_min,leight_max,speed):
            #t.up()
            t.goto(i,m.cos(i/weight)*k)
            #t.down()
            #t.dot(5)

    def tanf(leight_min = -30,leight_max = 30,weight = 10,k = 100,color = 'black',speed = 1):
        t.color(color)
        t.up()
        t.goto(leight_min,m.tan(leight_min/weight)*k)
        t.down()
        for i in range(leight_min,leight_max,speed):
            #t.up()
            t.goto(i,m.tan(i/weight)*k)
            #t.down()
            #t.dot(5)

class DotsFuntions:
    def Inverse(k = 1000,leight_min = -200,leight_max = 200,color = 'black',interval = 1):
        
        t.color(color)
        t.up()
        t.goto(leight_min,int(k/leight_min))
        t.down()
        for i in range(leight_min,leight_max,interval):
            if(i != 0):
                #t.up()
                t.goto(i,int(k/i))#식 넣는곳
                #t.down()
                #t.dot(5)
            else:
                pass


    def f(pow = 2,leight_min = -10,leight_max = 10,color = 'black',interval = 1):

        t.color(color)
        t.up()
        t.goto(leight_min,int(m.pow(leight_min,pow)))
        t.down()
        for i in range(leight_min,leight_max,interval):
            t.up()
            t.goto(i,int(m.pow(i,pow)))#식 넣는곳 
            t.down()
            t.dot(5)

    def sinf(leight_min = -200,leight_max = 200,weight = 10,k = 30,color = 'black',interval = 1):
        t.color(color)
        t.up()
        t.goto(leight_min,m.sin(leight_min/weight)*k)
        t.down()
        for i in range(leight_min,leight_max,interval):
            t.up()
            t.goto(i,m.sin(i/weight)*k)
            t.down()
            t.dot(5)

    def cosf(leight_min = -200,leight_max = 200,weight = 10,k = 30,color = 'black',interval = 1):
        t.color(color)
        t.up()
        t.goto(leight_min,m.cos(leight_min/weight)*k)
        t.down()
        for i in range(leight_min,leight_max,interval):
            t.up()
            t.goto(i,m.cos(i/weight)*k)
            t.down()
            t.dot(5)

    def tanf(leight_min = -30,leight_max = 30,weight = 10,k = 100,color = 'black',interval = 1):
        t.color(color)
        t.up()
        t.goto(leight_min,m.tan(leight_min/weight)*k)
        t.down()
        for i in range(leight_min,leight_max,interval):
            t.up()
            t.goto(i,m.tan(i/weight)*k)
            t.down()
            t.dot(5)


def start(speed = 100):
    t.ht()
    turtle.title('Graph Graphics')
    t.speed(speed)
    t.color('red')
    t.fd(-200)
    t.fd(400)
    t.color('blue')
    t.up()
    t.goto(0,0)
    t.down()
    t.goto(0,200)
    t.goto(0,-200)
    turtle.setup(400,400)

def exitonclick():
    turtle.exitonclick()