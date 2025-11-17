import math

n = int(input("Inserisci il numero fino a dove vuoi arrivare: "))
somma = 0

if n >= 0:
    for i in range(1, 2 * n + 1, 2):
        somma += i

radice_intera = math.isqrt(somma)
print(f"La somma è: {somma}, Quadrato perfetto: {radice_intera** 2 == somma}")
  