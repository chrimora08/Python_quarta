file = open("./nomefile.csv", "r")
contenuto = file.readline()

for riga in contenuto:
    if riga[0] == "#":
        print(riga)

file.close()