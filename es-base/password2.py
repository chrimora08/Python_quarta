##L'utente inserisce in input una password 
##Il programma stampa la password oscurata da * tranne prima ed ultima lettera

password = input("Inserisci la tua password: ")
password_blanked = password[0] + "*" * (len(password) - 2) + password[-1]
print(f"Password inserita: {password_blanked}")