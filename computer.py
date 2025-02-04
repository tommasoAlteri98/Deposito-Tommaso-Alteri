class CPU :
    def __init__(self, modello, frequenza):
        self.modello = modello
        self.frequenza = frequenza
        print("Modello: " + modello + ", Frequenza: " +str(frequenza))
    
    def stampa_cpu(self):
        print("STAMPA CARATTERISTICHE XYZ CPU")
        
class Ram :
    def __init__(self, capacita):
        self.capacita = capacita
    
    def stampa_ram(self):
        print("STAMPA CARATTERISTICHE XYZ RAM")

class Computer(Ram, CPU):
    def __init__(self, modello, frequenza, capacita, marca):
        CPU.__init__(self, modello, frequenza)
        Ram.__init__(self, capacita)
        self.marca = marca
        print("Hai creato un computer della seguente marca: " + marca)
    
    def stampa_computer(self):
        print(f"Questo computer {self.marca} ha {self.capacita} GB di capacita RAM e una CPU modello {self.modello}")
    
    def metodo_stampa_cpu(self):
        self.stampa_cpu()
    
    def metodo_stampa_ram(self):
        self.stampa_ram()

computer1 = Computer("Apple iOs 21.0", 5.0, 15, "Apple")
computer1.stampa_computer()
computer1.metodo_stampa_cpu()
computer1.metodo_stampa_ram()