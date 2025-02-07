class UnitaMilitare:
    def __init__(self, nome, numero_soldati):
        self.nome = nome
        self.numero_soldati = numero_soldati

    def muovi(self):
        print("L'unità " + self.nome + "si sta muovendo.")

    def attacca(self):
        print("L'unità " + self.nome  + " sta sparando ai nemici.")

    def ritirata(self):
        print("L'unità " + self.nome + " sta scappando a gambe levate.")

class Artiglieria(UnitaMilitare):
    def __init__(self, nome, numero_soldati, numero_cannoni):
        super().__init__(nome, numero_soldati)
        self.numero_cannoni = numero_cannoni
 
    def calibra_artiglieria(self):
        print("L'unità " + self.nome + " sta calibrando l'artiglieria.")

class Fanteria(UnitaMilitare):
    def __init__(self, nome, numero_soldati):
        super().__init__(nome, numero_soldati)

    def costruisci_trincea(self):
        print("L'unità " + self.nome + " sta scavando una trincea.")

class Cavalleria(UnitaMilitare):
    def __init__(self, nome, numero_soldati, numero_cavalli):
        super().__init__(nome, numero_soldati)
        self.numero_cavalli = numero_cavalli

    def esplora_terreno(self):
        print("L'unità " + self.nome + " sta esplorando il terreno per raccogliere informazioni con i suoi" + str(self.numero_cavalli) + " cavalli.")

class SupportoLogistico(UnitaMilitare):
    def __init__(self, nome, numero_soldati):
        super().__init__(nome, numero_soldati)

    def rifornisci_unita(self):
        print("L'unità " + self.nome + "sta portando i rifornimenti alle altre unità.")

class Ricognizione(UnitaMilitare):
    def __init__(self, nome, numero_soldati):
        super().__init__(nome, numero_soldati)

    def conduci_ricognizione(self):
        print("L'unità " + self.nome + " sta conducendo missioni di ricognizione.")

class ControlloMilitare:
    def __init__(self):
        self.unitaMilitari = []

    def registra_unita(self, unita):
        self.unitaMilitari.append(unita)
        print("L'unità " + unita.nome + " è stata aggiunta alla lista.")

    def mostra_unita(self):
        if self.unitaMilitari == True:
            print("Unità registrate:")
            for unita in self.unitaMilitari:
                print("Nome: " + unita.nome +", Numero soldati: " + str(unita.numero_soldati))
        else:
            print("Non ci unità militari registrate.")

    def dettagli_unita(self, nome):
        for unita in self.unitaMilitari:
            if unita.nome == nome:
                print("Unità " + unita.nome +":")
                print("Numero soldati: " + str(unita.numero_soldati))
                return
        print("Unità con il nome " + nome + " non trovata.")
        
    
fanteria = Fanteria("Fanteria Gruppo 1", 150)
artiglieria = Artiglieria("Artiglieria Itachi", 40, 100)
cavalleria = Cavalleria("Cavalleria Loky", 30, 50)
supporto = SupportoLogistico("Supporto Logistico", 20)
ricognizione = Ricognizione("Ricognizione Rosso", 15)

controlloReparti = ControlloMilitare()

controlloReparti.registra_unita(fanteria)
controlloReparti.registra_unita(artiglieria)
controlloReparti.registra_unita(cavalleria)
controlloReparti.registra_unita(supporto)
controlloReparti.registra_unita(ricognizione)

controlloReparti.mostra_unita()

controlloReparti.dettagli_unita("Artiglieria Itachi")
controlloReparti.dettagli_unita("Cavalleria Loky")
