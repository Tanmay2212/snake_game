from turtle import Turtle
import random


class Food(Turtle):

    def __init__(self, screen):
        super().__init__()
        self.shape("turtle")
        self.penup()
        self.shapesize(stretch_len=0.5, stretch_wid=0.5)
        self.color("deepskyblue")
        self.speed("fastest")
        self.refresh()

    def refresh(self):
        x_food_position = random.randint(-280 ,280)
        y_food_position = random.randint(-280 ,280)
        self.goto(x_food_position, y_food_position)



    
