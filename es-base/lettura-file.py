file = open("./dati.csv", "r")   #oggetto file
righe = file.readlines()         #lista di stringhe che contiene righe del file
print(righe)

file.close()

i = 0

for element in righe:
    prima_riga = righe[i]
    titolo1, titolo2, titolo3 = prima_riga[:-1].split(",")

    print(titolo1 + titolo2 + titolo3)

    i += 1


