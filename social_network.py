class Rete():
    def __init__(self):
        self.utenti = []

    def iscrivi_utente(self, utente):
        self.utenti.append(utente)

    def __str__(self):
        return f"N° utenti: {len(self.utenti)}"

    def aggiungi_amicizia(self, utente1, utente2):
        if (utente1 in self.utenti) and (utente2 in self.utenti):
            if utente2 not in utente1.amici:
                utente1.aggiungi_amico(utente2)
                utente2.aggiungi_amico(utente1)
            else:
                print(f"Errore: {utente1.nome} e {utente2.nome} sono già amici")
        else:
            print("Errore: almeno uno dei 2 utenti non è iscritto")

    def rimuovi_amicizia(self, utente1, utente2):
        if utente1 in utente2.amici:
            utente1.amici.remove(utente2)
            utente2.amici.remove(utente1)
            print(f"Amicizia tra {utente1.nome} e {utente2.nome} rimossa")
        else:
            print("Errore: questi utenti non sono amici")

    def rimuovi_utente(self, utente):
        if utente in self.utenti:
            for amico in utente.amici[:]:
                self.rimuovi_amicizia(utente, amico)
            self.utenti.remove(utente)
            print(f"Utente {utente.nome} rimosso dalla rete")
        else:
            print("Errore: utente non trovato")

    def cerca_utente(self, nome):
        for utente in self.utenti:
            if utente.nome.lower() == nome.lower():
                return utente
        return None

    def amici_in_comune(self, utente1, utente2):
        return [amico for amico in utente1.amici if amico in utente2.amici]

    def suggerisci_amici(self, utente):
        suggeriti = []
        for amico in utente.amici:
            for amico_di_amico in amico.amici:
                if (amico_di_amico != utente and
                        amico_di_amico not in utente.amici and
                        amico_di_amico not in suggeriti):
                    suggeriti.append(amico_di_amico)
        return suggeriti

    def mostra_utenti(self):
        if not self.utenti:
            print("Nessun utente iscritto")
        else:
            print("Utenti iscritti alla rete:")
            for utente in self.utenti:
                print(f"  - {utente}")


class Utente():
    def __init__(self, nome):
        self.nome = nome
        self.amici = []

    def aggiungi_amico(self, utente):
        self.amici.append(utente)

    def __str__(self):
        lista_nomi = [amico.nome for amico in self.amici]
        return f"{self.nome} ha come amici: {lista_nomi}"

    def __repr__(self):
        return self.nome


def main():
    social_network = Rete()

    luca = Utente("Luca")
    mario = Utente("Mario")
    lucia = Utente("Lucia")
    anna = Utente("Anna")

    social_network.iscrivi_utente(luca)
    social_network.iscrivi_utente(mario)
    social_network.iscrivi_utente(lucia)
    social_network.iscrivi_utente(anna)

    social_network.mostra_utenti()

    social_network.aggiungi_amicizia(luca, lucia)
    social_network.aggiungi_amicizia(mario, lucia)
    social_network.aggiungi_amicizia(mario, anna)
    social_network.aggiungi_amicizia(luca, lucia) 

    print(luca)
    print(mario)
    print(lucia)
    print(anna)

    in_comune = social_network.amici_in_comune(luca, mario)
    print(f"Amici in comune tra Luca e Mario: {[u.nome for u in in_comune]}")

    suggeriti = social_network.suggerisci_amici(luca)
    print(f"Amici suggeriti per Luca: {[u.nome for u in suggeriti]}")

    trovato = social_network.cerca_utente("Mario")
    print(f"Ricerca 'Mario': {trovato}")
    non_trovato = social_network.cerca_utente("Giorgio")
    print(f"Ricerca 'Giorgio': {non_trovato}")

    social_network.rimuovi_amicizia(luca, lucia)
    print(luca)
    print(lucia)

    social_network.rimuovi_utente(mario)
    print(social_network)
    social_network.mostra_utenti()
    print(lucia)
    print(anna)


if __name__ == "__main__":
    main()