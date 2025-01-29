while True :
    numero = int(input("Inserisci un numero: "))
    
    for i in range(numero, -1, -1): 
        print(i)
        
        ripetizione = input("Ripetere tutto il ciclo(Rispondi con S o N)").lower()
        if ripetizione != "S":
            print("Ciclo chiuso!")
            break