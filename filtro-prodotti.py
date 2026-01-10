# Una lista contiene dizionari con chiavi nome, categoria, prezzo. 
# Scrivere una funzione che restituisca solo i prodotti di una certa categoria 
# con prezzo inferiore a un valore dato.
prodotti = [
    {"nome": "Laptop", "categoria": "elettronica", "prezzo": 899.99},
    {"nome": "Mouse", "categoria": "elettronica", "prezzo": 29.99},
    {"nome": "Scrivania", "categoria": "arredamento", "prezzo": 199.99},
    {"nome": "Tastiera", "categoria": "elettronica", "prezzo": 79.99},
    {"nome": "Sedia", "categoria": "arredamento", "prezzo": 149.99},
    {"nome": "Monitor", "categoria": "elettronica", "prezzo": 349.99}
]

prodotti_scelti = []
categoria = input("Scegli una categoria tra elettronica e arredamento: ")
prezzo = float(input("Scegli la soglia massima di prezzo: "))

for prodotto in prodotti:
    if prodotto["categoria"] == categoria and prodotto["prezzo"] <= prezzo:
        prodotti_scelti.append(prodotto)

for prodotto in prodotti_scelti:
    print(f"- {prodotto['nome']}: €{prodotto['prezzo']}")