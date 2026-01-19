#Un dizionario associa nomi di playlist a liste di titoli di canzoni. Scrivere funzioni per:
#(a) contare le canzoni totali, (b) cercare in quale playlist si trova una canzone, (c) unire due playlist in una nuova.
def contaCanzoni(diz):
    cont = 0
    for playlist in diz.values():
        cont += len(playlist)

    return cont

def cercarePlaylist(canz, diz):
    list = []
    for playlist in diz:
        for canzone in diz[playlist]:
            if canzone == canz:
                list.append(playlist)

    return list

def unirePlaylist(list1, list2, diz):
    diz_new = {}
    for a in list1.values():
        for b in list2.values():
            if b == a:
                diz_new[list2] = b

    return diz_new

def main():    
    playlist = {
    "Rock": ["Bohemian Rhapsody", "Stairway to Heaven", "Hotel California"],
    "Pop": ["Thriller", "Like a Prayer", "Billie Jean"],
    "Relax": ["Hotel California", "Imagine", "Let It Be"]
    }

    print(f"Le canzoni in totale sono: {contaCanzoni(playlist)}")
    canzone = input("Inserisci una canzone da cercare: ")
    print(f"La canzone si trova nella playlist {cercarePlaylist(canzone, playlist)}")
    print("Playlist disponibili: ")
    for genere in playlist:
        print(genere)

    playlist1 = input("Inserisci la playlist 1 da unire: ")
    playlist2 = input("Inserisci la playlist 2 da unire: ")

    playlist_new = unirePlaylist(playlist1, playlist2, playlist)
    print(f"Dizionario con playlist unite: {playlist_new}")

if __name__ == "__main__":
    main()