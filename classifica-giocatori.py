giocatori = [
    {"nome": "Player1", "punteggio": 4500},
    {"nome": "Player2", "punteggio": 7200},
    {"nome": "Player3", "punteggio": 3100},
    {"nome": "Player4", "punteggio": 8900},
    {"nome": "Player5", "punteggio": 5600}
]

for i in range(len(giocatori)):
    for j in range(len(giocatori) - 1):
        if giocatori[j]["punteggio"] < giocatori[j + 1]["punteggio"]:
            temp = giocatori[j]
            giocatori[j] = giocatori[j + 1]
            giocatori[j + 1] = temp

print("CLASSIFICA:")
posizione = 1
for giocatore in giocatori:
    print(f"{posizione}. {giocatore['nome']} - {giocatore['punteggio']} punti")
    posizione = posizione + 1