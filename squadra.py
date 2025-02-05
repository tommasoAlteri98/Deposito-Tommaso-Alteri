class MembroSquadra :
    def __init__(self, nome, eta) :
        self.nome = nome
        self.eta = eta
        
    def descrivi(self) :
        print(f"Nome: {self.nome}, Età: {self.eta} anni")

class Giocatore(MembroSquadra) :
    def __init__(self, nome, eta, ruolo, numero_maglia) :
        super().__init__(nome, eta)
        self.ruolo = ruolo
        self.numero_maglia = numero_maglia
    
    def descrivi(self) :
        super().descrivi()
        print(f"Ruolo: {self.ruolo}, Numero di maglia: {self.numero_maglia}") 
    
    def gioca_partita(self) :
        print(f"Il giocatore {self.nome} sta giocando")

class Allenatore(MembroSquadra) :
    def __init__(self, nome, eta, anni_esperienza) :
        super().__init__(nome, eta)
        self.anni_esperienza = anni_esperienza
    
    def descrivi(self) :
        super().descrivi()
        print("Anni di esperienza: " + str(self.anni_esperienza)) 
    
    def dirige_allenamento(self) :
        print(f"L'allenatore {self.nome} sta svolgendo l'allenamento")
        
class Assistente(MembroSquadra) :
    def __init__(self, nome, eta, specializzazione) :
        super().__init__(nome, eta)
        self.specializzazione = specializzazione
    
    def descrivi(self) :
        super().descrivi()
        print(f"L'assistente {self.nome} svolge in squadra il seguente compito: {self.specializzazione}") 
    
    def supporta_team(self) :
        print(f"L'assistente {self.nome} lavora per il team")

class Squadra :
    def __init__(self) :
        self.listaSquadra = []
        
    def aggiungi_giocatore(self, giocatore) :
        self.listaSquadra.append(giocatore)
    
    def aggiungi_allenatore(self, allenatore) :
        self.listaSquadra.append(allenatore)
    
    def aggiungi_assistente(self, assistente) :
        self.listaSquadra.append(assistente)
        
    def stampa_squadra(self) :
        for squadra in self.listaSquadra:
            print(squadra.descrivi())

Lazio = Squadra()
Roma = Squadra()
Inter = Squadra()
Juventus = Squadra()

Rovella = Giocatore("Rovella", 24, "Centrocampista", 6 )
DeRossi = Giocatore("DeRossi", 40, "Centrocampista", 16 )
Provedel = Giocatore("Provedel", 27, "Portiere", 90 )
Totti = Giocatore("Totti", 45, "Attacante", 10 )
Bonucci = Giocatore("Bonucci", 33, "Difensore", 19 )

Allegri = Allenatore("Allegri", 55, 15)
Baroni = Allenatore("Baroni", 55, 4)
Ranieri = Allenatore("Ranieri", 22, 67)

Farris = Assistente("Farris", 56, "Assistente")
Martusciello = Assistente("Martusciello", 58, "Vice")

Lazio.aggiungi_giocatore(Rovella)
Lazio.aggiungi_giocatore(Provedel)
Lazio.aggiungi_allenatore(Baroni)
Lazio.aggiungi_assistente(Martusciello)

Roma.aggiungi_giocatore(Totti)
Roma.aggiungi_giocatore(DeRossi)
Roma.aggiungi_allenatore(Ranieri)

Juventus.aggiungi_giocatore(Bonucci)
Juventus.aggiungi_allenatore(Allegri)

Inter.aggiungi_assistente(Farris)

Allegri.descrivi()
Lazio.stampa_squadra()