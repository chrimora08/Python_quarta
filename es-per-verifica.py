#Cercare i giochi di un genere specifico
#Visualizzare il gioco con il punteggio più alto
#Calcolare la media dei punteggi
#Trovare i giochi usciti dopo un certo anno
def cercaGiochiGenere(genere, diz):
    for videogioco in diz:
        if genere == videogioco[1]:
            print(videogioco)


def main():
    videogiochi = [
        {"titolo": "The Legend of Zelda", "genere": "Avventura", "anno": 2017, "punteggio": 9.7},
        {"titolo": "Super Mario Odyssey", "genere": "Platform", "anno": 2017, "punteggio": 9.6},
        {"titolo": "Elden Ring", "genere": "RPG", "anno": 2022, "punteggio": 9.5},
        {"titolo": "Portal 2", "genere": "Puzzle", "anno": 2011, "punteggio": 9.5},
        {"titolo": "Minecraft", "genere": "Sandbox", "anno": 2011, "punteggio": 9.0}
    ]

    scelta = int(input("Cosa vorresti fare:\n1) Cercare i giochi di un genere specifico\n2) Visualizzare il gioco con il punteggio più alto\n3) Calcolare la media dei punteggi\n4) Trovare i giochi usciti dopo un certo anno\nScelta: "))

    if scelta == 1:
        genere = input("Inserisci il genere per trovare i giochi di quel tipo: ")
        cercaGiochiGenere(genere, videogiochi)

if __name__ == "__main__":
    main()