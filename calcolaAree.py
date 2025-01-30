lista_aree = []

def calcola_area(datiCalcolo) :
  def wrapper(*args, **kwargs) :
    totale = datiCalcolo(*args, **kwargs)
    lista_aree.append(totale) 
    return totale   
  return wrapper

@calcola_area
def quadrato(l) :
  return l * l

@calcola_area
def triangolo(b, a) :
  return (b * a) / 2

@calcola_area
def rettangolo(a, b) :
  return a * b

quadrato(2)
triangolo (3, 2)
rettangolo (5, 5)

print(lista_aree)