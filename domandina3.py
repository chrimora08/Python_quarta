l = ["mario", "luigi", "giovanni", "alice"]

nmax = 0
nomemax = ""

for nome in l:
    n = len(nome)
    if n > nmax:
        nmax = n
        nomemax = nome

print(nomemax)