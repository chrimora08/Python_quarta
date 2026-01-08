with open('testo.txt', 'r') as file:
    righe = file.readlines()

num_righe = len(righe)
num_parole = 0
num_caratteri_senza_spazi = 0

for riga in righe:
    parole = riga.split()
    num_parole += len(parole)
    num_caratteri_senza_spazi += len(riga.replace(" ", "").replace("\n", ""))

print("RISULTATI:")
print(f"Numero di righe: {num_righe}")
print(f"Numero di parole: {num_parole}")
print(f"Numero di caratteri (senza spazi): {num_caratteri_senza_spazi}")