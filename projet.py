import turtle

screen = turtle.Screen()
screen.title("Spirale colorée")
screen.bgcolor("white")
screen.setup(600, 600)

t = turtle.Turtle()
t.speed(0)
t.width(2)

couleurs = ["red", "orange", "yellow", "green", "cyan", "blue", "purple", "magenta"]

for i in range(200):
    t.color(couleurs[i % len(couleurs)])  # change de couleur à chaque tour
    t.forward(i * 1.5)                    # avance de plus en plus
    t.left(59)                            # angle pour créer la spirale

t.hideturtle()
screen.mainloop()