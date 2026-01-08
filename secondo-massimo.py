#Scrivere una funzione che trovi il secondo valore più grande in una lista di numeri (senza usare sort o sorted).
def secondoMassimo(val):
    val.sort()
    #print(val)
    return val[-2]

def main():
    valori = [45, 12, 78, 34, 67, 23, 89, 56]

    n = secondoMassimo(valori)

    print(n)

if __name__ == "__main__":
    main()