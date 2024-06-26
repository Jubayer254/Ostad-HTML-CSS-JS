import turtle as t
import random as rand

game_start = False

t.bgcolor("green")

# SNAKE
snake = t.Turtle()
snake.shape("square")
snake.color("red")
snake.speed(0)
snake.penup()
snake.hideturtle()

# LEAF
leaf = t.Turtle()
leaf_shape = ((0,0), (14,2), (18, 6), (20,20), (6, 18), (2, 14))
t.register_shape('leaf', leaf_shape)
leaf.shape('leaf')
leaf.color(76/255, 47/255, 16/255)
leaf.penup()
leaf.hideturtle()

# START
text = t.Turtle()
text.write("Press SPACE to Start", align='center', font=('Arial', 16, 'bold'))
text.hideturtle()

# SCORE
show_score = t.Turtle()
show_score.penup()
show_score.hideturtle()

def outside_window():
    left_wall = -t.window_width()/2
    right_wall = t.window_width()/2
    top_wall =  t.window_height()/2
    bottom_wall = -t.window_height()/2
    (x, y) = snake.pos()
    return x < left_wall or x > right_wall or y < bottom_wall or y > top_wall

def game_over():
    snake.color('yellow')
    leaf.color('yellow')
    t.penup()
    t.hideturtle()
    t.write("Game Over", align='center', font=('Arial', 30, 'bold'))

def display_score(current_score):
    show_score.clear()
    x = (t.window_width() / 2) - 50
    y = (t.window_height() / 2) - 100
    show_score.setpos(x, y)
    show_score.write(str(current_score), align='right', font=('Arial', 40, 'bold'))

def place_leaf():
    leaf.hideturtle()
    leaf.setx(rand.randint(-200, 200))
    leaf.sety(rand.randint(-200, 200))
    leaf.showturtle()

def start_game():
    global game_start
    if game_start:
        return
    game_start = True
    text.clear()
    snake_speed = 2
    snake_len = 3
    score = 0
    snake.shapesize(1, snake_len, 1)
    snake.showturtle()
    display_score(score)
    place_leaf()
    while True:
        snake.forward(snake_speed)
        if snake.distance(leaf) < 20:
            place_leaf()
            snake_len = snake_len + 1
            snake.shapesize(1, snake_len, 1)
            snake_speed = snake_speed + 1
            score = score + 5
            display_score(score)
        if outside_window():
            game_over()
            break

def move_up():
    if snake.heading() == 0 or snake.heading() == 180:
        snake.setheading(90)

def move_down():
    if snake.heading() == 0 or snake.heading() == 180:
        snake.setheading(270)

def move_left():
    if snake.heading() == 90 or snake.heading() == 270:
        snake.setheading(180)

def move_right():
    if snake.heading() == 90 or snake.heading() == 270:
        snake.setheading(0)

t.onkey(start_game, 'space')
t.onkey(move_up, 'Up')
t.onkey(move_down, 'Down')
t.onkey(move_left, 'Left')
t.onkey(move_right, 'Right')

t.listen()
t.mainloop()