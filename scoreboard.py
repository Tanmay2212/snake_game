from turtle import Turtle
ALIGNMENT = "center"
FONT =("courier" ,24 ,"normal")

class Scoreboard(Turtle):

    def __init__(self, screen):
        super().__init__()
        self.score = 0
        self.penup()
        self.color("darkorchid")
        self.goto(0, 260)
        self.hideturtle()

    def update_Scoreboard(self):
        self.write(f"score: {self.score}", align=ALIGNMENT, font=FONT)


    def increase_Score(self):
        self.score += 1
        self.clear()  # Clear previous score if needed
        self.update_Scoreboard()
