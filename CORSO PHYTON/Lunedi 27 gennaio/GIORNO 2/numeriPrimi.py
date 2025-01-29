primi = 0
salvati = []

while primi < 5:
    num = int(input("Inserisci un numero"))
    if num > 1 :
        for i in range(2, num):
            if num % i == 0:
                print("Il numero scelto non è un numero primo")
                break
            else :
                primi += 1
                salvati.append(num)
                print("Il numero scelto è un numero primo")
    else :
        print("Il numero scelto non è un numero primo")
print(salvati)