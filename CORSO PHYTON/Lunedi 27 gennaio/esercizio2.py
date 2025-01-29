scelta = int(input("inserisce un numero da 1 a 4"))

nome="Tom"

if (scelta==1) : 
    print("modalita aggiungi")
    nomeaggiunto = input() 
    nome += nomeaggiunto
    print(nome)
elif (scelta==2) : 
    print("modalita modifica")
    nome = input()
    print(nome)
elif (scelta==3) : 
    print("modalita elimina")
    nome = ""
else : print("valore non valido")