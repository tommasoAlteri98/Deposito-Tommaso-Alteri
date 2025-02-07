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

    