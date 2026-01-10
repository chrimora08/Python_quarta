studenti_voti = {
    "Marco": 7,
    "Sara": 8,
    "Luca": 6,
    "Elena": 8,
    "Paolo": 7,
    "Giulia": 8,
    "Andrea": 6,
    "Chiara": 7
}

voto = {}
for v in studenti_voti.values():
    if v in voto:
        voto[v] += 1
    else:
        voto[v] = 1

voto_frequente = 0
volte_massime = 0

for v in voto:
    if voto[v] > volte_massime:
        volte_massime = voto[v]
        voto_frequente = v

print(f"Il voto più frequente è: {voto_frequente}")