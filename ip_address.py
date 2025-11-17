ip = input("Inserisci un indirizzo Ip ->")

ottetti_str = ip.split(".")
print(ottetti_str)

ottetti = []

for s in ottetti_str:
    ottetti.append(int(s))

for l in ottetti:
    n = 8 - len(str(l))   
    bitfinale = ("0" * n) + str(l)
    if len(bitfinale)  != 8:
        bitfinal = "0" * n

    print(bin(int(bitfinale)))
