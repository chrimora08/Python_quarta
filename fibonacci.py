n = int(input("Quanti numeri della sequenza di Fibonacci vuoi? "))
a, b = 1, 1

if n > 2:
    print(f"{a} - {b}", end = " - ")
    for i in range(n - 2):
        a, b = a + b, a
        if i == n - 3:
            print(a)
        
        else:
            print(a, end = " - ")
        
elif n == 2:
    print(f"{a} - {b}")

elif n == 1:
    print(a)

else: 
    print("Numero non valido per la sequenza")