import random
import turtle
import time


delay = 0.09

score = 0
High_Score = 0

wr = turtle.Screen()
wr.title("Wise Snake")
wr.bgcolor("white")
wr.setup(width=600,height=600)
wr.tracer(0)

snake_head = turtle.Turtle()
snake_head.speed(0)
snake_head.color("red")
snake_head.shape("square")
snake_head.penup()
snake_head.setpos(0,0)
snake_head.snake_dir = "stop"

food = turtle.Turtle()
food.speed(0)
food.color("green")
food.shape("circle")
food.penup()
food.setpos(0,100)

tim = turtle.Turtle()
tim.color ("green")
tim.shape("arrow")
tim.hideturtle()

tim.width(3)
tim.penup()
tim.setpos(-300,300)
tim.pendown()
for x in range(4):
    tim.forward(600)
    tim.right(90)

pen = turtle.Turtle()
pen.shape("square")
pen.color("violet")
pen.hideturtle()
pen.penup()
pen.setpos(0,200)
pen.write("Score : 0 High_Score :0", align = "center", font = ("Courier", 24, "normal"))

parts = []

def die():
    
    time.sleep(0.8)
    snake_head.setpos(0,0)
    snake_head.snake_dir = "stop"
    for part in parts:
        part.goto(1000,1000)
    parts.clear()
def food_spawn():
    colors = ["black","purple","orange","blue","green","aqua","violet","grey"]
    x = random.randrange(-290,290)
    y = random.randrange(-290,290)
    random_colour = random.randrange(0,len(colors))
    food.color(colors[random_colour])
    snake_head.color(colors[random_colour])
    food.setpos(x,y)

def go_up():
    if snake_head.snake_dir != "down":
        snake_head.snake_dir = "up"

def go_down():
    if snake_head.snake_dir != "up":
        snake_head.snake_dir = "down"

def go_right():
    if snake_head.snake_dir != "left":
        snake_head.snake_dir = "right"

def go_left():
    if snake_head.snake_dir != "right":
        snake_head.snake_dir = "left"

def hack():
    snake_head.snake_dir = "rotate"

def move():
    if snake_head.snake_dir == "up":
        snake_head.setheading(90)
        snake_head.forward(20)       
    if snake_head.snake_dir == "down":
        snake_head.setheading(90)        
        snake_head.backward(20)
    if snake_head.snake_dir == "left":
        snake_head.setheading(180)
        snake_head.forward(20)
    if snake_head.snake_dir == "right":
        snake_head.setheading(180)
        snake_head.backward(20)
    if snake_head.snake_dir == "rotate":
        snake_head.left(20)

wr.listen()
wr.onkeypress(go_up, "Up")
wr.onkeypress(go_down, "Down")
wr.onkeypress(go_right, "Right")
wr.onkeypress(go_left, "Left")
wr.onkeypress(hack, "z")

while True:
    
    wr.update()
    move()

    if score > High_Score:
        High_Score = score
    pen.clear()
    pen.write("Score : {} High_Score : {}".format(score,High_Score), align="Center" , font=("corier", 24, "normal"))
    if snake_head.distance(food) <20 :
        food_spawn()
        score += 10
        delay -= 0.001
        
        body = turtle.Turtle()
        body.speed(0)
        body.color("red")
        body.shape("square")
        body.penup()
        parts.append(body)

    for index in range(len(parts)-1,0,-1):
        x = parts[index-1].xcor()
        y = parts[index-1].ycor()
        parts[index].goto(x,y)
    
    
    for part in parts:
        if snake_head.distance(part) <10 :
            die()
            score = 0
            delay = 0.09

    if len(parts) > 0:
        x = snake_head.xcor()
        y = snake_head.ycor()
        parts[0].goto(x,y)
    if snake_head.xcor() > 285 or snake_head.ycor() > 285 or snake_head.xcor() < -285 or snake_head.ycor() < -285 :
        die()
        score = 0
        delay = 0.09
    time.sleep(delay)

wr.mainloop()
