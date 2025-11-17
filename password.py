##L'utente inserisce in input una password 
##Il programma stampa la password oscurata da *

password = input("Inserisci la tua password: ")

password_blanked = "*" * len(password)

print(f"Password inserita: {password_blanked}")