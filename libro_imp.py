class Libro : 
    def __init__(self, titolo, autore, isbn) :
        self.titolo = titolo
        self.autore = autore
        self.isbn = isbn
        
    def descrizione(self) :
        isbnCod = str(self.isbn)
        stri = "Il libro intitolato "+ self.titolo +" scritto da "+ self.autore+" ha il seguente codice isbn: " +isbnCod
        return stri
        
