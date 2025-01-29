name = "placeholder"
pw = "placeholder"
id = 0

if name == "placeholder" and id==0 and pw=="placeholder" :
    name = input("Inserisci il nome utente")
    pw = input("Inserisci la pw")
    id +=1
    
    if name == "placeholder" and id==0 and pw=="placeholder" :
        print("Errore")
    else:
        print("ti sei registrato")
else:
    print("Gia Registrato!!!")