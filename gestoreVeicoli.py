# Classe base Veicolo
class Veicolo:
    def __init__(self, marca, modello, anno):
        self._marca = marca
        self._modello = modello
        self._anno = anno
        self._accensione = False

    def accendi(self):
        self._accensione = True
        print("La macchina " + self._marca + self._modello + " è stato accesa.")

    def spegni(self):
        self._accensione = False
        print("La macchina " + self._marca + self._modello + " è stato spenta.")

class Auto(Veicolo):
    def __init__(self, marca, modello, anno, numero_porte):
        super().__init__(marca, modello, anno)
        self._numero_porte = numero_porte

    def suona_clacson(self):
        print("La macchina " + self._marca + self._modello + " sta suonando il clacson!!!")

class Furgone(Veicolo):
    def __init__(self, marca, modello, anno, capacità_carico):
        super().__init__(marca, modello, anno)
        self._capacità_carico = capacità_carico

    def carica(self):
        print("La macchina " + self._marca + self._modello + " sta caricando la mercanzia.")

    def scarica(self):
        print("La macchina " + self._marca + self._modello + " sta scaricando la merce.")
