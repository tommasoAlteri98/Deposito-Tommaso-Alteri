while True :
    num1 = int(input("Inserisci il primo numero del tuo intervallo"))
    num2 = int(input("Inserisci il secondo numero del tuo intervallo"))
    cosaVuoiStampare = input("Cosa vuoi stampare? Primi/Non Primi/Entrambi").lower()
    numeriPrimi = []
    numeriNonPrimi = []
    
    for num in range(num1, num2 + 1) : 
        if num > 1 : 
            primo = True
            for n in range(2, num) :
                if num % n == 0 :
                    primo = False
                    break
            if primo == True:
                numeriPrimi.append(num)
            else :
                numeriNonPrimi.append(num)
    
    if cosaVuoiStampare == "primi" :
        print("I numeri primi nell'intervallo selezionato sono: " ,numeriPrimi)
    elif cosaVuoiStampare == "non primi" :
        print("I numeri non primi nell'intervallo selezionato sono: " ,numeriNonPrimi)
    elif cosaVuoiStampare == "entrambi" :
        print("I numeri primi nell'intervallo selezionato sono: " ,numeriPrimi)
        print("I numeri non primi nell'intervallo selezionato sono: " ,numeriNonPrimi)
    else :
        print("Scelta non valida")
        
    proseguire = input("Vuoi ricominciare? Si/No").lower()
    if proseguire == "no" :
        print("AGG' FIRNT")
        break