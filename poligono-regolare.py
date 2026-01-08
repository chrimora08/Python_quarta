import turtle

def poligono(lati, lunghezza):
    t = turtle.Turtle()
    t.speed(3)
    
    angolo = 360 / lati
    for _ in range(lati):
        t.forward(lunghezza)
        t.left(angolo)
    
    turtle.done()
