from turtle import Turtle

FONT = ("Courier", 24, "normal")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.pu()
        self.hideturtle()
        self.current_level = 0
        self.goto(-280, 260)
        self.write_board()

    def increase_level(self):
        self.current_level += 1
        self.write_board()

    def write_board(self):
        self.clear()
        self.write(f"Level: {self.current_level}", move=False, align='left', font=FONT)

    def game_over(self):
        self.clear()
        self.goto(0, 0)
        self.write("GAME OVER!", move=False, align='center', font=FONT)
