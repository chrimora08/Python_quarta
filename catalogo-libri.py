def main():    
    libri = [
        {"titolo": "Il nome della rosa", "autore": "Umberto Eco", "anno": 1980, "prezzo": 15.50},
        {"titolo": "1984", "autore": "George Orwell", "anno": 1949, "prezzo": 12.00},
        {"titolo": "Il pendolo di Foucault", "autore": "Umberto Eco", "anno": 1988, "prezzo": 18.00},
        {"titolo": "Fahrenheit 451", "autore": "Ray Bradbury", "anno": 1953, "prezzo": 11.50},
        {"titolo": "Il mondo nuovo", "autore": "Aldous Huxley", "anno": 1932, "prezzo": 13.00}
    ]

    print("Libri di Eco:", [l["titolo"] for l in cerca_autore("Eco")])
    print("Prezzo medio:", round(media_prezzi(), 2))
    recente = libro_recente()
    print(f"Più recente: {recente['titolo']} ({recente['anno']})")

def cerca_autore(autore):
    return [libro for libro in libri if autore.lower() in libro["autore"].lower()]

def media_prezzi():
    prezzi = [libro["prezzo"] for libro in libri]
    return sum(prezzi) / len(prezzi)

def libro_recente():
    return max(libri, key=lambda x: x["anno"])

if __name__ == "__main__":
    main()