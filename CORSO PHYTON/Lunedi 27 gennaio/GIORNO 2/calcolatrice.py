numeroUno = float(input("Inserisci il numero1"))
numeroDue = float(input("Inserisci il numero2"))
operazione = input("Inserisci una delle 4 operazioni").lower()

if operazione == "+" or operazione =="addizione" : risultato = numeroUno + numeroDue 
elif operazione == "-" or operazione =="sottrazione" : risultato = numeroUno - numeroDue
elif operazione == "x" or operazione =="moltiplicazione" : risultato = numeroUno * numeroDue
elif operazione == "/" or operazione =="divisione" : 
    if numeroDue == 0 :
        print("Impossibile dividere per 0")
    else : risultato = numeroUno / numeroDue
else : print("Operazione non valida")
print(risultato)