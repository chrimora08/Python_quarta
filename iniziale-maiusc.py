#Crea un programma che chiede all'tente il suo nome e lo stampa sempre con l'iniziale maiuscola

nome = input("Inserisci il tuo nome: ")
nome = nome[0].upper() + nome[1:]

print(nome)

