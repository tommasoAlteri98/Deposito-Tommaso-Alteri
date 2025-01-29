nome = "nomePredefinito"
pw = "passwordPredefinita"
booleanControl = False

nomeimput = input("inserisci il nome")
pwimput = input("inserisci la pw")
if nomeimput == nome and pwimput == pw :
    print("Benvenuto nel sito! Dati di accesso confermati")
    booleanControl = True
    
    if (booleanControl):
     scelta = input("scegli tra opzione A e opzione B")
     if scelta == "a" or scelta=="A": input("Quale è il tuo colore preferito?")
     elif scelta == "b" or scelta=="B": input("Quale è il tuo animale preferito?")
     else : print ("Errore. Errore. Errore!!")
    
elif nomeimput == nome and pwimput != pw :
    print("password errata")
elif nomeimput != nome and pwimput == pw :
    print("nome utente errato")
elif nomeimput != nome and pwimput != pw :
    print("entrambi i dati errati")