#In python ci sono le colezioni 
#liste, touple, dizionari, set

#lISTE
#Creazione

l = [3, 3.14, 10, "ciao", True]

#stesse regole di indicizzazione e slicing dele stringe

print(f"l'ultimo elemento dela lista è: {l[-1]}")
print(l)
print(f"lista senza primo ed ultimo elemento: {l[1:-1]}")

l.append("NUOVO")

print(l)

l.pop()

print(l)