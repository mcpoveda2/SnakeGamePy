from turtle import Turtle

ALIGNMENT = "center"
FONT = ('Arial', 12, 'normal')
COLOR = "white"

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.num = 0
        self.penup()  # Levantar el bolígrafo para que la tortuga no dibuje mientras se mueve
        self.goto(0, 280)
        self.color(COLOR)
        self.hideturtle()
        self.crearScoreboard()

    def crearScoreboard(self):
        self.write(f"Score : {self.num}",False,ALIGNMENT ,font= FONT)

    def gameOver(self):
        self.goto(0, 0)
        self.write(f"GAME OVER", False, ALIGNMENT, font=FONT)


    def increseScore(self):
        self.num += 1
        self.clear()
        self.crearScoreboard()