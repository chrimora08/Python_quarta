def temp_media(dati):
    somma = 0
    for citta in dati:
        somma += citta["temp"]

    return somma / len(dati)

def filtra_citta(dati, nome):
    lista_variazioni = []
    for citta in dati:
        if citta["citta"] == nome:
            lista_variazioni.append(citta["temp"])

    return lista_variazioni

def temp_per_citta(dati):
    diz = {}
    for citta in dati:
        if citta["citta"] in diz:
            diz[citta["citta"]] = citta["temp"]
        else:
            diz[citta["citta"]] = citta["temp"]

    return diz
    
def carica_regioni(nome_file):
    diz = {}
    file = open(nome_file)
    righe = file.readlines()
    file.close()

    for riga in righe:
        r = riga.split(";")
        diz[r[0]] = r[1][:-1]

    return diz

def main():
    dati = [
        {"citta": "Milano", "temp": 12},
        {"citta": "Roma", "temp": 18},
        {"citta": "Milano", "temp": 14},
        {"citta": "Napoli", "temp": 20},
        {"citta": "Roma", "temp": 17},
        {"citta": "Napoli", "temp": 22},
        {"citta": "Milano", "temp": 10}
    ]

    temperatura = temp_media(dati)
    print(f"La temperatura media vale: {temperatura}")

    citta = input("Inserisci il nome della città su cui calcolare le variazioni: ")
    print(f"Le variazioni di {citta} sono {filtra_citta(dati, citta)}")

    list_temp_per_citta = temp_per_citta(dati)
    print(f"Le temperature per ogni città sono: {list_temp_per_citta}")

    diz_citta_regioni = carica_regioni("regioni.txt")
    print(f"Dizionario citta: regione ==> {diz_citta_regioni}")
    

if __name__ == "__main__":
    main()