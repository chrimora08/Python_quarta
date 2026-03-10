class Nodo:
    """Nodo autoreferenziale per albero binario."""

    def __init__(self, valore, sx=None, dx=None):
        self.valore = valore
        self.sx = sx
        self.dx = dx

    def inserisci(self, valore):
        if valore < self.valore:
            if self.sx is None:
                self.sx = Nodo(valore)
            else:
                self.sx.inserisci(valore)
        else:
            if self.dx is None:
                self.dx = Nodo(valore)
            else:
                self.dx.inserisci(valore)

    def cerca(self, valore):
        if valore == self.valore:
            return True
        if valore < self.valore:
            nodo_successivo = self.sx
        else:
            nodo_successivo = self.dx
        if nodo_successivo is None:
            return False
        
        return nodo_successivo.cerca(valore)

    def __str__(self):
        return f"Nodo({self.valore}, sx={self.sx}, dx={self.dx})"

root = Nodo(5)
for v in [3, 7, 1, 4, 6, 8]:
    root.inserisci(v)

print(root)
print(root.cerca(4))  
print(root.cerca(9))   