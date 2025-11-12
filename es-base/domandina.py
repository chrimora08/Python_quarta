###########################################

a = input("Inserisci una parola: ")
b = int(input("Inserisci un numero: "))

if len(a) > b:
    print(a[:-b] + "*" * b)

###########################################

c = input("Inserisci una parola: ")

if c == (c[::-1]):
    print("E' palindroma")

else:
    print("Non è palindroma")


###########################################

n = int(input("Inserisci un numero: "))

if n >= 0:
    for i in range(0, n + 1, 1):
        print(f"Quadrato di {i}: {i * i}")

###########################################

