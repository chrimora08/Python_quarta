presenze = {
    "Marco": ["2024-01-10", "2024-01-11", "2024-01-12", "2024-01-15"],
    "Sara": ["2024-01-10", "2024-01-12", "2024-01-15", "2024-01-16", "2024-01-17"],
    "Luca": ["2024-01-10", "2024-01-11"],
    "Elena": ["2024-01-10", "2024-01-11", "2024-01-12", "2024-01-15", "2024-01-16"]
}

def conta(nome):
    return len(presenze.get(nome, []))

def piu_presenti():
    return max(presenze, key=lambda x: len(presenze[x]))

def presenti(data):
    return [nome for nome, date in presenze.items() if data in date]

print("Marco:", conta("Marco"), "presenze")
print("Più presente:", piu_presenti())
print("Presenti il 2024-01-12:", presenti("2024-01-12"))