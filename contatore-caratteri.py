testo = "abracadabra"

diz = {}

for carattere in testo:
    if carattere in diz:
        diz[carattere] += 1
    else:
        diz[carattere] = 1

print(diz)  