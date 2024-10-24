# a121_catch_a_turtle.py
#-----import statements-----
from os import terminal_size
import turtle as t
import random
#-----game configuration----
terrapagosFillColor = "indigo"
terrapagosSize = 3
terrapagosShape = "turtle"
score = 0
timer = 30
#one thousand = 1 second
counterInterval = 1000   
timerUp = False
wn = t.Screen()
wn.bgcolor("black")
color = ["red", "orange", "yellow", "green", "blue", "gold", "DeepSkyBlue", "chocolate", "chartreuse", "AntiqueWhite", "aquamarine"]

#-----initialize turtle-----
terrapagos = t.Turtle()
terrapagos.fillcolor(terrapagosFillColor)
terrapagos.shape(terrapagosShape)
terrapagos.shapesize(terrapagosSize)
terrapagos.speed(0)
terrapagos.teleport(-100, 100)

scorer = t.Turtle()
scorer.shapesize(0.000001)
scorer.color("white")

counter =  t.Turtle()
counter.shapesize(0.000001)
counter.color("white")

#-----game functions--------
def countdown():
  global timer, timerUp
  counter.clear()
  counter.teleport(-370, 310)
  if timer <= 0:
    counter.write("Time's Up", font=("Calibri", 20, "normal"))
    exit()
  else:
    counter.write("Timer: " + str(timer), font=("Calibri", 20, "normal"))
    timer -= 1
    counter.getscreen().ontimer(countdown, counterInterval)

def updateDisplay():
    global score
    scorer.teleport(0, 0)
    scorer.clear()
    scorer.showturtle()
    scorer.teleport(0, -2)
    scorer.color("black")
    scorer.write(score, font=("Calibri", 23, "bold"), align = "center")
    scorer.color("white")
    scorer.teleport(0, 0)
    scorer.write(score, font=("Calibri", 20, "normal"), align = "center")
    scorer.hideturtle()


def terrapagosClicked(x, y):
    global score
    global terrapagosSize
    score += 1
    terrapagos.shapesize(terrapagosSize)
    terrapagos.color(random.choice(color))
    terrapagos.stamp()
    terrapagos.color("indigo")
    updateDisplay()
    terrapagos.teleport(random.randint(-400, 350), random.randint(-300, 300))
    terrapagosSize -= 0.2
    if terrapagosSize <= 0.5:
      terrapagosSize = 3 
terrapagos.onclick(terrapagosClicked)

#-----events----------------

wn.ontimer(countdown, counterInterval)
wn.mainloop()
