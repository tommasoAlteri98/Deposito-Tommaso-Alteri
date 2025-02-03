class Ristorante :
    def __init__(self, nomeRistorante, tipoCucina) :
        self.nomeRistorante = nomeRistorante
        self.tipoCucina = tipoCucina
        self.aperto = False
        self.menu = {}
    
    def DescriviRistorante(self) :
        print("Il ristorante " + self.nomeRistorante + " offre: " + self.tipoCucina)
        
    def ApriRistorante(self) :
        self.aperto = True
        print("Il ristorante " + self.nomeRistorante + " è stato aeprto!")
    
    def ChiudiRistorante(self) :
        self.aperto = False
        print("Il ristorante " + self.nomeRistorante + " è stato chiuso!")
    
    def StatoApertura(self) :
        if self.aperto == True :
            print("Il ristorante " + self.nomeRistorante + " è ora aeprto!")
        else :
             print("Il ristorante " + self.nomeRistorante + " è ora chiuso!")
    
    def AggiungiPiatto(self, piatto, prezzo) :
        self.menu[piatto] = prezzo
    
    def RimuoviPiatto(self, piatto) :
        if piatto in self.menu :
            del self.menu[piatto]
            print("Il piatto selezionato è stato rimosso dal Menu")
        else :
            print("Il piatto selezionato non è presente nel Menu")
    
    def MenuRistorante(self) :
        print(self.menu)


anvedi = Ristorante("Da cracco", "stellata")
anvedi.DescriviRistorante()
anvedi.ApriRistorante()
anvedi.ChiudiRistorante()
anvedi.AggiungiPiatto("carbonara", 12)
anvedi.MenuRistorante()
anvedi.AggiungiPiatto("cacio e pepe", 9)
anvedi.AggiungiPiatto("matriciana", 11)
anvedi.RimuoviPiatto("carbonara")
anvedi.MenuRistorante()