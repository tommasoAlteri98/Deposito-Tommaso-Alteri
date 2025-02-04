import libro_imp

class Libreria :
    def __init__(self) :
        self.listaLibri = []
        
    def aggiungi_libro(self, libro) :
        self.listaLibri.append(libro)
        
    def rimuovi_libro(self, isbn) :
        for libro in self.listaLibri :
            if libro.isbn == isbn :
                self.listaLibri.remove(libro)
                print("Hai rimosso il libro con ISBN: " ,isbn)
                
    
    def cerca_per_titolo(self, titolo) :
        listaTrovata = []
        for libro in self.listaLibri :
            if libro.titolo == titolo :
                listaTrovata.append(libro)
                print(libro.descrizione())
        
    
    def mostra_catalogo(self) :
        for libro in self.listaLibri :
            print("Titolo: ",libro.titolo)
            print("Autore: ",libro.autore)
            print("ISBN: ",libro.isbn)
            print("-------------------")
        
            
libro1 = libro_imp.Libro("Harry Potter 1", "J.K.Rowling", "1430")
libro2 = libro_imp.Libro("Harry Potter 2", "J.K.Rowling", "1431")
libro3 = libro_imp.Libro("I simpson", "Matt Groening", "3456")

libreria = Libreria()
libreria.aggiungi_libro(libro1)
libreria.aggiungi_libro(libro2)
libreria.aggiungi_libro(libro3)
libreria.mostra_catalogo()
libreria.rimuovi_libro("3456")
libreria.mostra_catalogo()
libreria.cerca_per_titolo("Harry Potter 1")

            
            
   

