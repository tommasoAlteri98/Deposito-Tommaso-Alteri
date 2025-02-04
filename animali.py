class Animale :
    def __init__(self, nome, eta) :
        self.nome = nome
        self.eta = eta
    
    def parla(self) :
        print(self.nome + " fa suono genrrico")
    
    def mostra_info(self):
        print("Nome: " + self.nome + ", Modello: " + str(self.eta))

class Cane(Animale) :
    def parla(self) :
        print(self.nome + " abbaia")

class Gatto(Animale) :
    def parla(self) :
        print(self.nome + " miagola")

class Lupo(Animale) :
    def parla(self) :
        print(self.nome + " ulula")
        
        
class Habitat :
    def __init__(self, habitat):
        self.habitat = habitat
            
    def mostra_zone(self):
        print(f"Zone dove vive :{','.join(self.habitat)} ")
            
class AnimaleSelvatico(Animale, Habitat):
    def __init__(self, nome, eta, habitat, erbivoro) :
        Animale.__init__(self, nome, eta)
        Habitat.__init__(self, habitat)
        self.habitat = habitat
        
    def mostra_info(self):
        super().mostra_info()
        self.mostra_zone()     
             
animale_generico = Animale("Animale genrrico", 22)
cane = Cane("Fido", 12)
gatto = Gatto("Gattuso", 15)
lupo = AnimaleSelvatico("Lucio", 14, ["caldo", "freddo", "molto" "freddo"],"carnivoro")

animale_generico.parla()
cane.parla()
gatto.parla()
cane.mostra_info()
lupo.mostra_info()
