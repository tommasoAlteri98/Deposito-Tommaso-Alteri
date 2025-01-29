numeri = input("Inserisci uno o più numeri") #in stringa
numeri = [int(num) for num in numeri.split()] 
for numero in numeri: print(f"Il quadrato di {numero} è {numero ** 2}")