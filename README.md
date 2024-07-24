Classes:

Snake: This class represents the snake itself.
It has an __init__ method that initializes the snake's segments using the X_POSITIONS list and sets the head as the first segment.
It has methods like create_snake to build the initial segments, add_segment to grow the snake, extend to call add_segment when eating food, move to move all segments based on the previous segment's position, and directional methods (Up, Down, Left, Right) to update the head's direction.
Food: This class represents the food item the snake eats.
It inherits from the Turtle class and overrides some properties like shape, color, and speed.
It has an __init__ method that sets up the food's appearance and calls refresh to place it in a random location.
It has a refresh method that generates random X and Y coordinates within boundaries and moves the food to that new location.
Scoreboard: This class represents the scoreboard that displays the current score.
It inherits from the Turtle class and hides itself (hideturtle).
It has an __init__ method that sets up the score variable and its initial position on the screen.
It has methods like update_Scoreboard to display the current score and increase_Score to update the score when the snake eats food.
Main File:

This file imports the Snake, Food, and Scoreboard classes and creates instances of each: snake, food, and scoreboard.
It sets up the game screen using the turtle library and defines constants for alignment and font used in the scoreboard.
The main loop (while game_on) handles the game logic:
Updates the screen (screen.update()) after each snake movement.
Introduces a delay (time.sleep(0.2)) between moves for smoother gameplay.
Calls the snake.move() method twice for a faster initial movement (optional).
Checks for collision with food and triggers appropriate actions (food.refresh(), snake.extend(), scoreboard.increase_score()).
Checks for collision with walls and triggers game over (game_on = False, scoreboard displays "Game Over").
Checks for collision with the snake's own body and triggers game over (similar to wall collision).
