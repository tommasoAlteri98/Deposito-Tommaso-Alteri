from abc import ABC, abstractmethod

class Impiegato(ABC):
    def __init__(self, nome, cognome, stipendio_base):
        self.nome = nome
        self.cognome = cognome
        self.stipendio_base = stipendio_base

    @abstractmethod
    def calcola_stipendio(self):
        pass

class ImpiegatoFisso(Impiegato):
    def calcola_stipendio(self):
        return self.stipendio_base

class ImpiegatoAProvvigione(Impiegato):
    def __init__(self, nome, cognome, stipendio_base, vendite):
        super().__init__(nome, cognome, stipendio_base)
        self.vendite = vendite

    def calcola_stipendio(self):
        bonus = 0.25 * self.vendite  #(se prende un quarto delle vendite)
        return self.stipendio_base + bonus

def stampa_informazioni_impiegati(impiegati):
    for impiegato in impiegati:
        stipendio = impiegato.calcola_stipendio()
        print("Nome: " + impiegato.nome + " " + impiegato.cognome)
        print("Stipendio Mensile: €" + str(stipendio))
        print("----------------------")
        
impiegato1 = ImpiegatoFisso("tommy", "deTommy", 1500)
impiegato2 = ImpiegatoAProvvigione("Flavio", "deFlavi", 1500, 5000)

impiegati = []
impiegati.append(impiegato1)
impiegati.append(impiegato2)

stampa_informazioni_impiegati(impiegati)