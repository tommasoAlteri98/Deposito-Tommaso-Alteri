#problemi con il calcolo del profitto riga 41 e 42!!!!!!!!!!!

class Prodotto :
    def __init__(self, nome, costo_produzione, prezzo_vendita) :
        self.nome = nome
        self.costo_produzione = costo_produzione
        self.prezzo_vendita = prezzo_vendita
    
    def calcola_profitto(self) :
        return self.prezzo_vendita - self.costo_produzione

class Elettronica(Prodotto) :
    def __init__(self, nome, costo_produzione, prezzo_vendita, garanzia, marca) :
        self.nome = nome
        self.costo_produzione = costo_produzione
        self.prezzo_vendita = prezzo_vendita
        self.garanzia = garanzia
        self.marca = marca
        
class Abbigliamento(Prodotto) :
    def __init__(self, nome, costo_produzione, prezzo_vendita, materiale, marca) :
        self.nome = nome
        self.costo_produzione = costo_produzione
        self.prezzo_vendita = prezzo_vendita
        self.materiale = materiale
        self.marca = marca

class Fabbrica :
    def __init__(self) :
        self.inventario = {}
    
    def aggiungi_prodotto(self, nome_prodotto, quantita) :
        if nome_prodotto in self.inventario :
            self.inventario[nome_prodotto]['quantita'] += quantita
        else :
            self.inventario[nome_prodotto] = {'prodotto' : nome_prodotto, 'quantita' : quantita}
            print("Aggiunti " + str(quantita) + " di " + nome_prodotto)
    
    def vendi_prodotto(self, nome_prodotto, quantita) :
        if nome_prodotto in self.inventario :
            prodotto = self.inventario[nome_prodotto]['prodotto']
            disponibilita = self.inventario[nome_prodotto]['quantita']
            if disponibilita >= quantita :
                self.inventario[nome_prodotto]["quantita"] -= quantita
                profitto = prodotto.calcola_profitto() * quantita
                print("Hai realizzato " + str(profitto) + " di profitto vendendo " + str(quantita) + " di " + nome_prodotto)
        else :
            print("Ogetto terminato")
        
    def restituisci_prodotto(self, nome_prodotto, quantita) :
        if nome_prodotto in self.inventario :
            self.inventario[nome_prodotto]['quantita'] += quantita
            print("Hai restituito " + str(quantita) + " di " + nome_prodotto)
        else :
            print("Il prodotto " + nome_prodotto + " non è presente nell'inventario")

tel = Elettronica("Tel A", 200, 300, "2 anni", "Marca A")
tel2 = Elettronica("Tel B", 300, 400, "1 anni", "Marca B")
giacca = Abbigliamento("Felpa", 50, 120, "cotone", "Nike")
fab = Fabbrica()

fab.aggiungi_prodotto("Tel A", 5)
fab.aggiungi_prodotto("Tel B", 12)
fab.aggiungi_prodotto("Felpa", 3)
fab.vendi_prodotto("Tel A", 2)
fab.restituisci_prodotto("Tel A", 1)