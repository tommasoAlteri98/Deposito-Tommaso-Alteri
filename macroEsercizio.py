numero = int(input("Inserisci un numero positivo"))

while numero <= 0 :
    print("Devi inserire un numero POSITIVO, non ti sbagliare!!!!!")
    numero = int(input("Inserisci un numero positivo"))
    
totaleSommaNumPari = 0
for n in range(2, numero+1, 2) :
    totaleSommaNumPari += n
print("La somma dei numeri pari da 2 fino al numero scelto è " ,totaleSommaNumPari)

print("L'elenco dei numeri dispari da 1 fino al numero scelto è: ")
for n in range(1, numero+1, 2) :
    print(n)
    
numeroPrimo = True
for n in range(2, int(numero ** 0.5) + 1) :
    if numero % n == 0 :
        numeroPrimo = False
        break
if numeroPrimo == False :
    print("Il numero scelto non è un numero primo")
else :
    print("Il numero scelto è un numero primo")