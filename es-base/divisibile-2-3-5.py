#chiede un numero intero e lo stampa se è divisibile per 2, 3 o per 5

numero = int(input("Inserici un numero: "))

if(numero % 2 == 0):
    print(f"{numero} è divisibile per 2")

if(numero % 3 == 0):
    print(f"{numero} è divisibile per 3")

if(numero % 5 == 0):
    print(f"{numero} è divisibile per 5")