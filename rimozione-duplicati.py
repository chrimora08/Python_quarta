def rimozioneDuplicati(elem):
    nuova_lista = []
    for nome in elem:
        if nome not in nuova_lista:
            nuova_lista.append(nome)
    return nuova_lista


def main():
    elementi = ["mela", "pera", "mela", "banana", "pera", "arancia", "mela"]

    elementi_senza_doppi = rimozioneDuplicati(elementi)

    print(elementi_senza_doppi)

if __name__ == "__main__":
    main()