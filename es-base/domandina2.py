l = ["ciao", "python", "casa"]

for parola in l:
    if parola[0] == "c":
        print(parola)

#################################

string = l[0]

for i in l[1:]:
    string = string + " " + i

print(string)