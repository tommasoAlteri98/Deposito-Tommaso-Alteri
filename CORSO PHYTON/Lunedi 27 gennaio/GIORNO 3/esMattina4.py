numeri = input("Inserisci qua i tuoi numeri")
lista = [int(numero) for numero in numeri.split()]

if len(lista) == 0 : print("Lista vuota")
else : 
    massimo = lista[0]
    for numero in lista :
        if numero > massimo :
            massimo = numero

    contatore = 0
    while contatore < len(lista) :
        contatore +=1
    
    print("Il numero max della lista inserita è " ,massimo)
    print("Il numero di elementi nella lista è " ,contatore)