#chiede quanti bit si vogliono usare
#chiede un numero binario gestito come stringa
#poi aggiunge tanti numeri quanti ne servono per arrivare dal numero binario ai bit

bit = int(input("Inserisci un numero di bit da usare -> "))
nBit = input("Inserisci un numero binario -> ")

n = bit - len(nBit)
bitfinale = ("0" * n) + nBit

print(bitfinale)