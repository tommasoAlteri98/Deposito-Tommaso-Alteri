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

    def lista_veicoli(self) :
        if len(self._veicoli) == 0:
            print("Non ci sono veicoli nel parco.")
        else:
            print("Elenco dei veicoli nel parco:")
            for veicolo in self._veicoli :
                print(veicolo._marca + " " + veicolo._modello + "(" + str(veicolo._anno) +")")

auto = Auto("FIAT", "Punto", 2002, 3)
auto2 = Auto("Lamborghini", "Hurracan", 2020, 2)
auto3 = Auto("FIAT", "Panda", 2023, 5)
furgoncino = Furgone("Mercedes", "Sprinter", 2021, 1500)
moto = Motocicletta("Yamaha", "R1", 2022, "sportiva")
moto2 = Motocicletta("Honda", "ModX", 2018, "normale")

gestore_parco_veicooli = GestoreParcoVeicoli()

gestore_parco_veicooli.aggiungi_veicolo(auto)
gestore_parco_veicooli.aggiungi_veicolo(auto2)
gestore_parco_veicooli.aggiungi_veicolo(auto3)
gestore_parco_veicooli.aggiungi_veicolo(furgoncino)
gestore_parco_veicooli.aggiungi_veicolo(moto)

gestore_parco_veicooli.lista_veicoli()

auto.accendi()
auto.suona_clacson()

furgoncino.carica()
furgoncino.scarica()
 
moto.esegui_wheelie()
moto2.esegui_wheelie()

gestore_parco_veicooli.rimuovi_veicolo("Toyota", "Hybrid")
gestore_parco_veicooli.lista_veicoli()
gestore_parco_veicooli.rimuovi_veicolo("FIAT", "Punto")
gestore_parco_veicooli.lista_veicoli()