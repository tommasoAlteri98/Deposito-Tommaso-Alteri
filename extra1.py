while True :
    scegliInput = input("Stringa o Numero?").lower()
    if scegliInput == "stringa" :
        stringaInserita = input("Inserisci la stringa da stampare")
        print(stringaInserita)
    elif scegliInput == "numero" :
        numeroInserito = int(input("Inserisci un numero"))
        if numeroInserito == 0 :
            print("Hai inserito lo 0")
        elif numeroInserito % 2 == 0 :
            print("Numero pari")
        else :
            print("Numero dispari")
    else :
        print("Hai sbagliato ad inserire. Riprova con una STRINGA o un NUMERO!")
        continue
    
    proseguire = input("Vuoi ricominciare? Si/No").lower()
    if proseguire == "no" :
        print("AGG' FIRNT")
        break