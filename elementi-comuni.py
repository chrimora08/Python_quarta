#Date due liste, restituire una nuova lista con gli elementi presenti in entrambe.
def elementiComuni(lista_a, lista_b):
    new_list = []

    for a in lista_a:
        for b in lista_b:
            if b == a:
                new_list.append(b)

    return new_list

def elementiComuni2(lista_a, lista_b):
    new_list = []

    for a in lista_a:
        if a in lista_b:
            new_list.append(a)

    return new_list

def main():
    lista_a = [1, 5, 8, 12, 15, 20]
    lista_b = [3, 5, 10, 12, 18, 20, 25]

    new_list = elementiComuni(lista_a, lista_b)
    new_list2 = elementiComuni2(lista_a, lista_b)

    print(new_list)
    print(new_list2)

if __name__ == "__main__":
    main()