import turtle

def sposta(x, y):
    turtle.penup
    turtle.goto(x, y)
    turtle.pendown

def poligono(lati, lunghezza):
    t = turtle.Turtle()
    t.speed(3)
    
    angolo = 360 / lati
    for _ in range(lati):
        t.forward(lunghezza)
        t.left(angolo)
    
    turtle.done()

def main():
    sposta(100, 200)
    poligono(4, 100)
    sposta(-100, 100)
    poligono(5, 100)

if __name__ == "__main__":
    main()