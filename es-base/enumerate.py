def main_0():
    lista = ["alice", "mario", "giovanni", "luca"]
    nome_max = None
    len_max = 0
    for nome in lista:
        if len(nome) > len_max:
            len_max = len(nome)
            nome_max = nome

    print(nome_max)

def main():
    lista = ["alice", "mario", "giovanni", "luca"]
    for i, nome in enumerate(lista):
        print(f"{i} - {nome}")

if __name__ == "__main__": #dunder == __ indica variabili private
    main()
