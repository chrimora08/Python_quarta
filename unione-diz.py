# Dati due dizionari, crearne uno nuovo che contenga tutte le chiavi. 
# Se una chiave è presente in entrambi, sommare i valori.
vendite_gennaio = {"mele": 120, "pere": 85, "arance": 200}
vendite_febbraio = {"mele": 95, "banane": 150, "arance": 180}

vendite_tot = {}

for prod in vendite_gennaio:
    vendite_tot[prod] = vendite_gennaio[prod]

for prod in vendite_febbraio:
    if prod in vendite_tot:
        vendite_tot[prod] = vendite_tot[prod] + vendite_febbraio[prod]
    else:
        vendite_tot[prod] = vendite_febbraio[prod]

print(vendite_tot)