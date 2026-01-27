import turtle
import random

class Quadrato():
    def _init_(self, lato, x, y, colore):
        self.lato = lato
        self.x = x
        self.y = y
        self.colore = colore
    
    def _str_(self):
        return f"Quadrato [lato={self.lato}, pos=({self.x},{self.y}), colore={self.colore}]"
    
    def perimetro(self):
        return 4 * self.lato
    
    def area(self):
        return self.lato ** 2
    
    def disegna(self):
        turtle.penup()
        turtle.goto(self.x, self.y)
        turtle.pendown()
        
        turtle.fillcolor(self.colore)
        turtle.pencolor(self.colore)
        
        turtle.begin_fill()
        for _ in range(4):
            turtle.forward(self.lato)
            turtle.left(90)
        turtle.end_fill()
        
        turtle.penup()


def genera_colore_casuale():
    r = random.random()
    g = random.random()
    b = random.random()
    return (r, g, b)


def main():
    turtle.setup(800, 600)
    turtle.speed(0) 
    turtle.hideturtle()
    turtle.colormode(1.0) 
    
    print("=== disegno 100 qua ===")
    for i in range(100):
        lato = random.randint(10, 60) 
        x = random.randint(-350, 350)  
        y = random.randint(-250, 250)  
        colore = genera_colore_casuale() 
        
        quadrato = Quadrato(lato, x, y, colore)
        quadrato.disegna()
        
        if (i + 1) % 20 == 0:
            print(f"Disegnati {i + 1} quadrati...")
    
    print("\n✓ Completato! 100 quadrati disegnati.")
    print("Clicca sulla finestra per chiudere.")
    
    turtle.done()


if __name__ == "__main__":
    main()