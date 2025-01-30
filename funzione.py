import random

def indovino() : 
    return random.randint(1, 100)

def indovinello() : 
    indovinare = indovino()
    print("Gioco dell'indovinello: Indovina il numero casuale da 1 a 100. Per terminare il gioco azzecca il numeroo digita ESCI")

    while True :
       inserito = input("Inserisci qua il tuo numero scelto o digita ESCI per terminare")
       if inserito.lower() == "esci" :
        print("Gioco terminato. Peccato: il numero estratto era " ,indovinare)
        break
    
       inserito = int(inserito)
    
       if inserito > indovinare :
         print("Il numero da indovinare è più basso del numero scelto")
       elif inserito < indovinare :
         print("Il numero da indovinare è più alto del numero scelto")
       else :
         print("Complimenti hai indovinato il numero. Hai vinto!!!")
         break
indovinello()