# MODULARITA': suddividere il codice in funzioni
COSTANTE = 3.14 # Variabile globale (dalle funzioni solo in lettura)

def primaLetteraMaiusc(stringa):
    """
    DOCSTRING:
    La funzione restituisce stringa cona la prima lettera maiuscola
    """
    s = stringa[0].upper() + stringa[1:].lower()
    return s

def media(lista):
    """
    La funzione restituisce la media dei valori e il numeor di elementi
    """
    somma = 0.
    for val in lista:
        somma += val 

    return somma  / len(lista), somma

def main():
    list = [8.3, 9.9, 3.4]
    parola = input("Inserisci una parola: ")
    print(primaLetteraMaiusc(parola))
    m, n = media(list)
    print(f"la media vale {m} mentre la somma dei voti vale {n}")

if __name__ == "__main__":
    main()