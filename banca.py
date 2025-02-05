class ContoBancario :
    def __init__(self, titolare, saldo) : #saldo iniziale = 0.0??
        self.__titolare = titolare
        self.__saldo = saldo
    
    def get_titolare(self) :
        return self.__titolare

    
    def get_saldo(self) :
        return self.__saldo
    
    def deposita(self, importo) :
        if importo > 0 :
            self.__saldo += importo
            print("E' stata deposita sul conto una cifra pari a " ,importo)
        else :
            print("La cifra da depositare deve essere positiva")
    
    def preleva(self, importo) :
        if importo > 0 and self.__saldo >= importo :
            print("Hai prelevato " ,importo)
        elif importo <= 0 :
            print("L'importo selezionato deve essere maggiore di 0")
        else :
            print("Per effettuare un prelievo devi avere saldo maggiore di 0")
    
    def visualizza_saldo(self) :
        print("Il saldo attuale è pari a euro: " ,self.__saldo)
    
    def set_titolare(self, titolare) :
        if titolare and titolare != " " :
            self.__titolare = titolare
        else :
            print("Il titolare non può essere una stringa vuota")
    
banca1 = ContoBancario("Tommy", 10000)
banca1.visualizza_saldo()
banca1.deposita(500)
banca1.visualizza_saldo()
banca1.deposita(-1)
banca1.preleva(50)

banca1.set_titolare("Elisa")
print("Il nuovo titolare del conto è " ,banca1.get_titolare())