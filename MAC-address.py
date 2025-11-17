def main():
    MAC = input("Inserisci un MAC address -> ")
    
    file = open("mac-vendors-export.csv", "r", encoding = 'utf-8')
    file.readline()
    
    for riga in file:
        if riga.split(",")[0] == MAC:
            print(riga.split(",")[1])
            file.close()
            return
    
    file.close()
    print(f"MAC {MAC} non trovato.")

if __name__ == "__main__":
    main()

#stampare anche la data di produzione