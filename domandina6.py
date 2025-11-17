def oscuraPassword(stringa):
    stringa = stringa[0] + ("*" * (len(stringa) - 1))
    return stringa
    
def main():
    list = ["Cane", "Mamma", "Ciao"]
    l = []
    for i in list:
        parola_oscurata = oscuraPassword(i)
        print(parola_oscurata)
        l.append(parola_oscurata)
    print(l)

if __name__ == "__main__":
    main()