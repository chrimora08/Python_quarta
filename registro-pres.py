# Un dizionario associa nomi di studenti a liste di date in cui erano presenti.
# Funzioni per: (a) contare le presenze, (b) trovare chi ha più presenze, 
# (c) trovare chi era presente in una certa data.
def conta_presenze(nome_studente, diz_presenze):
    if nome_studente in diz_presenze:
        return len(diz_presenze[nome_studente])
    else:
        return 0

def studente_piu_presente(diz_presenze):
    studente_max = ""
    presenze_max = 0
    
    for studente in diz_presenze:
        num_presenze = len(diz_presenze[studente])
        if num_presenze > presenze_max:
            presenze_max = num_presenze
            studente_max = studente
    
    return studente_max

def presenti_in_data(data, diz_presenze):
    studenti_presenti = []
    
    for studente in diz_presenze:
        if data in diz_presenze[studente]:
            studenti_presenti.append(studente)
    
    return studenti_presenti

def main():
    presenze = {
        "Marco": ["2024-01-10", "2024-01-11", "2024-01-12", "2024-01-15"],
        "Sara": ["2024-01-10", "2024-01-12", "2024-01-15", "2024-01-16", "2024-01-17"],
        "Luca": ["2024-01-10", "2024-01-11"],
        "Elena": ["2024-01-10", "2024-01-11", "2024-01-12", "2024-01-15", "2024-01-16"]
    }
    
    print("(a) Presenze di tutti gli studenti:")
    for alunno in presenze:
        num_presenze = conta_presenze(alunno, presenze)
        print(f"   {alunno}: {num_presenze} presenze")
    
    print("\n(b) Studente più presente:", studente_piu_presente(presenze))
    print("\n(c) Presenti il 2024-01-12:", presenti_in_data("2024-01-12", presenze))

if __name__ == "__main__":
    main()