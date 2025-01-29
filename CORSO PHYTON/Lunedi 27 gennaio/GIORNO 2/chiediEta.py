eta = int(input ("Inserisci la tua eta"))
filmList = ["Harry Potter I","Toy Story","Wall-E","Hannibal Lecter","Dexter"]
if eta < 18:
    print("Mi dispiace ma non puoi vedere i film per over 18")
    print ("Puoi vedere i seguenti film:" + filmList[0] + ", "+ filmList[1] + ", "+ filmList[2] + ". ")
else :
    print("Hai più di 18 anni")
    print ("Puoi vedere i seguenti film: ")
    print(filmList)