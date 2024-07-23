from turtle import Turtle
class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.num = 0
        self.penup()  # Levantar el bolígrafo para que la tortuga no dibuje mientras se mueve
        self.goto(0, 280)
        self.color("white")
        self.hideturtle()
        self.crearScoreboard()

    def crearScoreboard(self):
        self.write(f"Score : {self.num}",False,"center",font=('Arial', 12, 'normal'))