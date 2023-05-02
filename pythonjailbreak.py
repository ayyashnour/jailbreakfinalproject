import turtle #used https://www.geeksforgeeks.org/create-breakout-game-using-python/ and
              #https://www.dropbox.com/sh/q0zvv7nntyndxmn/AAAkBQxhF1pPTiTabmg7XTowa?dl=0 for help with screen size and movemnts


screen = turtle.Screen()
screen.setup(width=800, height=600)
screen.tracer(0) 
screen.title('Jailbreak')
screen.bgpic('stuckinjail.gif')



ball = turtle.Turtle()
ball.shape('circle')
ball.color('orange')
ball.speed(0)
ball.up()
ball.dx = 7
ball.dy = 3

paddle = turtle.Turtle()
paddle.shape('square')
paddle.shapesize(1, 5) 
paddle.color('DarkOrange4')
paddle.up()
paddle.goto(0, -270)

score_dis = turtle.Turtle()
score_dis.color('black')
score_dis.up()
score_dis.hideturtle()
score_dis.goto(-250, 10)
score_dis.write('Days out of jail: 0', align='center', font=('Times', 30, 'normal'))

colors = ['CadetBlue4', 'CadetBlue4', 'CadetBlue3', 'CadetBlue3', 'CadetBlue1', 'CadetBlue1']
score = 0

def move_right():
    if paddle.xcor()<350:
        paddle.setx(paddle.xcor()+80)


def move_left():
    if paddle.xcor()>-350:
        paddle.setx(paddle.xcor()-80)


def border_limit():
    if ball.ycor() > 280:
        ball.dy = -ball.dy
    if ball.xcor() > 380:
        ball.dx = -ball.dx
        ball.goto(380, ball.ycor())
    if ball.xcor() < -380:
        ball.dx = -ball.dx
        ball.goto(-380, ball.ycor())

def paddle_check():
    paddle_left_edge = paddle.xcor() - 50
    paddle_right_edge = paddle.xcor() + 50
    
    if ball.ycor() <= -250 and ball.ycor() >= -260 and ball.dy < 0:
        if paddle_left_edge <= ball.xcor() <= paddle_right_edge:
            ball.dy *= -1


screen.listen()
screen.onkey(move_right, 'Right')
screen.onkey(move_left, 'Left')


x_list = [-330, -225, -120, -15, 90, 195, 300]
y_list = [285, 260, 235, 210, 185, 160]
brick_list = []


for i, y in enumerate(y_list):
    color = colors[i % 6]  
    for k in x_list:
        brick = turtle.Turtle()
        brick.shape('square')
        brick.shapesize(stretch_len=5, stretch_wid=1)
        brick.color(color)
        brick.up()
        brick.goto(k, y)
        brick_list.append(brick)
brick_count = len(brick_list)

score_dis.write("Days out of jail: " + str(score), align='center', font=('Times', 30, 'normal'))


while brick_count > 0:

    screen.update()
    ball.goto(ball.xcor()+ball.dx, ball.ycor()+ball.dy)
    

    border_limit()
    paddle_check()

  
    if ball.ycor() <-280:
        ball.goto(0,0)
        ball.dx *= -1
        if score>0:
            score -= 1
        score_dis.clear()
        score_dis.write("Days out of jail: " + str(score), align='center', font=('Times', 30, 'normal'))
        
  
    for brick in brick_list: #needed help with block collisions from the second source
        if ball.xcor() + 10 >= brick.xcor() - 60 and ball.xcor() - 10 <= brick.xcor() + 60:
            if ball.ycor() >= brick.ycor() - 20 and ball.ycor() <= brick.ycor() + 20:
                ball.dy *= -1
                brick.goto(1000, 1000)
                score += 1
                brick_count -= 1
                score_dis.clear()
                score_dis.write("Days out of jail: " + str(score), align='center', font=('Times', 30, 'normal'))

    if ball.ycor() < -300:
         ball.goto(0, 0)
         ball.dy = 0
         ball.dx = 0
         score_dis.clear()
         score_dis.goto(0, 0)
         score_dis.write("Game Over", align='center', font=('Times', 30, 'normal'))

    if brick_count == 0:
        ball.goto(0, 0)
        ball.dy = 0
        ball.dx = 0
        score_dis.clear()
        score_dis.goto(0, 0)
        score_dis.write("You're free!", align='center', font=('Times', 30, 'normal'))




screen.mainloop()


