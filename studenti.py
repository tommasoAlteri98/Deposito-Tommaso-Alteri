class Persona:
    def __init__(self, nome, eta):
        self.__nome = nome
        self.__eta = eta

    def get_nome(self):
        return self.__nome

    def get_eta(self):
        return self.__eta
    
    def set_nome(self, nome):
        self.__nome = nome

    def set_eta(self, eta):
        self.__eta = eta

    def presentazione(self):
        str = "Ciao, mi chiamo " + self.__nome + " e ho " + str(self.__eta) + " anni."
        return str

class Studente(Persona):
    def __init__(self, nome, eta, voti):
        super().__init__(nome, eta)  
        self.__voti = voti  

    def calcola_media(self):
        if len(self.__voti) != 0:
            return sum(self.__voti) / len(self.__voti) 
        else :
            return 0 
            
    def presentazione(self):
        media = str(self.calcola_media())
        nome = self.get_nome()
        eta = str(self.get_eta())
        return "Ciao, sono " + nome + " e ho " + eta + " anni. La mia media dei voti è " + media

class Professore(Persona):
    def __init__(self, nome, eta, materia):
        super().__init__(nome, eta)
        self.__materia = materia  

    def presentazione(self):
        nome = self.get_nome()
        eta = str(self.get_eta())
        materia = self.__materia
        stri = "Ciao, sono " + nome + ", ho " + eta + " anni e insegno " + materia
        return stri

studente1 = Studente("Mirko", 17, [8, 9, 7, 10, 8, 7.5])
professore1 = Professore("Bistoncini", 55, "Matematica")


studente1.set_nome("Tommaso")
studente1.set_eta(26)
professore1.set_nome("Mirko")
professore1.set_eta("29")
print(studente1.presentazione()) 
print(professore1.presentazione())  