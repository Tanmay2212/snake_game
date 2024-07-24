from turtle import Screen # Import the turtle library for graphics and screen for display over screen
from snake import Snake # Import the Snake class (likely defines snake behavior)
from food import  Food# Import the Food class (likely defines food behavior)
from scoreboard import Scoreboard# Import the Scoreboard class (likely handles score display)
import time# Import the time library for delays

# Define constants for screen size and formatting
ALIGNMENT = "center"
FONT =("courier" ,35 ,"normal")

# Create the game screen
screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("moccasin")
screen.title("The Snake Game")
screen.tracer(0)# Turn off automatic screen updates for smoother gameplay



x_position = [(0, 0), (-20, 0), (-40, 0)]  # Initialize starting snake position

segments = []

snake = Snake()
food = Food(Screen)
scoreboard = Scoreboard(screen)

screen.listen()
screen.onkey(snake.Up, "Up")
screen.onkey(snake.Down,"Down")
screen.onkey(snake.Left,"Left")
screen.onkey(snake.Right,"Right")



game_on = True

scoreboard = Scoreboard(screen)
scoreboard.update_Scoreboard()  # Display initial score (0)

while game_on:
    screen.update()  # Update screen after all segments move

    # Set a delay between moves for smoother gameplay
    time.sleep(0.2)

    snake.move()
    snake.move()


    #detect collision with food
    if snake.head.distance(food) < 20:
        food.refresh()# Place food in a new random location
        snake.extend()  # Increase snake length
        scoreboard.increase_score()  # Update score
#detect collision with wall
    if snake.head.xcor() > 290 or snake.head.xcor() < -290 or snake.head.ycor() > 290 or snake.head.ycor() < -290: 
        game_on =False
        # game over
        scoreboard.goto(0,0)
        scoreboard.write(f"game over", align= ALIGNMENT, font=FONT)
#detect collison with tail
    for segment in snake.segments[1:]:  # Skip the head segment
        #second way- shorteer plus function use
        if snake.head.distance(segment) < 15 :
            game_on =False
            scoreboard.goto(0,0)# Display game over message
            scoreboard.write(f"game over", align= ALIGNMENT, font=FONT)# Display game over message

        #one way - lengthy code 
        # if segment == snake.head:
        #     pass
        # elif snake.head.distance(segment) < 10 :
            
        #     game_on =False
        #     scoreboard.goto(0,0)
        #     scoreboard.write(f"game over", align= ALIGNMENT, font=FONT)
        
screen.exitonclick()
















