# Classe base Veicolo
class Veicolo:
    def __init__(self, marca, modello, anno) :
        self._marca = marca
        self._modello = modello
        self._anno = anno
        self._accensione = False

    def accendi(self) :
        self._accensione = True
        print("Il mezzo " + self._marca + " " + self._modello + " è stato acceso.")

    def spegni(self) :
        self._accensione = False
        print("Il mezzo " + self._marca + " " + self._modello + " è stato spento.")

class Auto(Veicolo) :
    def __init__(self, marca, modello, anno, numero_porte) :
        super().__init__(marca, modello, anno)
        self._numero_porte = numero_porte

    def suona_clacson(self) :
        print("La macchina " + self._marca + " " + self._modello + " sta suonando il clacson!!!")

class Furgone(Veicolo):
    def __init__(self, marca, modello, anno, capacità_carico) :
        super().__init__(marca, modello, anno)
        self._capacità_carico = capacità_carico

    def carica(self) :
        print("Il furgone " + self._marca + " " + self._modello + " sta caricando la mercanzia.")

    def scarica(self) :
        print("Il furgone " + self._marca + " " + self._modello + " sta scaricando la merce.")

class Motocicletta(Veicolo) :
    def __init__(self, marca, modello, anno, tipo) :
        super().__init__(marca, modello, anno)
        self._tipo = tipo

    def esegui_wheelie(self) :
        if self._tipo == "sportiva" :
            print(self._marca + " " + self._modello + " esegue un wheelie!")
        else:
            print(self._marca + " " + self._modello + " non è sportiva, quindi non può fare un wheelie.")

class GestoreParcoVeicoli :
    def __init__(self) :
        self._veicoli = [] 
        
    def aggiungi_veicolo(self, veicolo) :
        self._veicoli.append(veicolo)
        print(veicolo._marca + " " + veicolo._modello + " è stato aggiunto al parco veicoli.")

    def rimuovi_veicolo(self, marca, modello) :
        for veicolo in self._veicoli :
            if veicolo._marca == marca and veicolo._modello == modello :
                self._veicoli.remove(veicolo)
                print(veicolo._marca + " " + veicolo._modello + " è stato rimosso dal parco veicoli.")
                return
        print("Il veicolo selezionato non è stato trovato nel parco veicoli.")

    