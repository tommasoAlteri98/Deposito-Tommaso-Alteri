from abc import ABC, abstractmethod #import abc

class Impiegato(ABC): #impiegatobase
    def __init__(self, nome, cognome, stipendio_base):
        self.nome = nome
        self.cognome = cognome
        self.stipendio_base = stipendio_base

    @abstractmethod
    def calcola_stipendio(self):
        pass

class ImpiegatoFisso(Impiegato): #derivato di impiegato con stipendio fisso
    def __init__(self, nome, cognome, stipendio_base):
        self.nome = nome
        self.cognome = cognome
        self.stipendio_base = stipendio_base
    
    def calcola_stipendio(self):
        return self.stipendio_base

class ImpiegatoAProvvigione(Impiegato): #derivato di impiegato con stipendio fisso + % vendite 
    def __init__(self, nome, cognome, stipendio_base, vendite):
        super().__init__(nome, cognome, stipendio_base)
        self.vendite = vendite

    def calcola_stipendio(self):
        bonus = 0.25 * self.vendite  #(se prende un quarto delle vendite)
        return self.stipendio_base + bonus

def stampa_informazioni_impiegati(impiegati): #ciclo in impiegati
    for impiegato in impiegati:
        stipendio = impiegato.calcola_stipendio()
        print("Nome: " + impiegato.nome + " " + impiegato.cognome)
        print("Stipendio Mensile: €" + str(stipendio))
        print("----------------------")
         
impiegato1 = ImpiegatoFisso("tommy", "deTommy", 1500) #istanze della classe
impiegato2 = ImpiegatoAProvvigione("Flavio", "deFlavi", 1500, 5000)

impiegati = [] #lista vuota
impiegati.append(impiegato1)
impiegati.append(impiegato2)

stampa_informazioni_impiegati(impiegati) #richiamo metodo per stampare dalla lista dove ho appena pusahto le istanze