#In python tutto è un oggetto
import math
import turtle

class Punto():
    #costruttore
    def __init__(self, x, y): #self = this in java
        #attributi
        self.x = x
        self.y = y

    def __str__(self):
        return f"({self.x}, {self.y})"
    
    def distanza_origine(self):
        #ritorna la distanza 
        return math.sqrt(self.x**2 + self.y**2)
    
    def scambia_coordinate(self):
        b = Punto(self.y, self.x)
        return b

    def disegna(self):
        t = turtle.Turtle()
        t.speed(0.5)

        t.penup()
        t.goto(self.x, self.y)
        t.pendown()

        t.screen.mainloop()

    def distanza(self, x2, y2):
        return math.sqrt((self.x - self.y) + (x2 - y2))

def main():
    a = Punto(200, 100)
    print(a)
    print(f"Il punto dista {a.distanza_origine()} dall'origine")
    print(f"Cordinate al contrario: {a.scambia_coordinate()}")
    a.disegna()
    dis = a.distanza(300, 200)
    print(f"La distanza è di: {dis}")

if __name__ == "__main__":
    main()