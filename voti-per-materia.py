# Un dizionario associa nomi di materie a liste di voti.
# Funzioni per: (a) calcolare la media, (b) trovare materia con media più alta, 
# (c) aggiungere un voto a una materia.
def calcola_media(lista_voti):
    if len(lista_voti) == 0:
        return 0
    
    somma = 0
    for voto in lista_voti:
        somma = somma + voto
    
    media = somma / len(lista_voti)
    return media

def materia_media_piu_alta(diz_voti):
    materia_max = ""
    media_max = 0
    
    for materia in diz_voti:
        media = calcola_media(diz_voti[materia])
        if media > media_max:
            media_max = media
            materia_max = materia
    
    return materia_max

def aggiungi_voto(nome_materia, voto, diz_voti):
    if nome_materia in diz_voti:
        diz_voti[nome_materia].append(voto)
    else:
        print(f"Materia '{nome_materia}' non trovata!")

def main():
    voti_materie = {
        "Matematica": [6, 7, 5, 8, 7],
        "Italiano": [7, 8, 7, 6],
        "Inglese": [8, 8, 9, 7, 8],
        "Informatica": [9, 8, 9, 10, 8]
    }
    
    for materia in voti_materie:
        media = calcola_media(voti_materie[materia])
        print(f"- {materia}: {media:.2f}")
    
    print(f"\nMateria con media più alta: {materia_media_piu_alta(voti_materie)}")
        
    aggiungi_voto("Matematica", 9, voti_materie)
    print(f"Nuova media Matematica: {calcola_media(voti_materie['Matematica']):.2f}")

if __name__ == "__main__":
    main()