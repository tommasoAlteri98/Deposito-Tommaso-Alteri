class CartaDiCredito :
    def effettua_pagamento(self, importo) :
        print("Hai pagato tramite carta di credito la seguente cifra: " ,importo)
    
class PayPal :
    def effettua_pagamento(self, importo) :
        print("Hai pagato tramite PayPal la seguente cifra: " ,importo)

class BonificoBancario :
    def effettua_pagamento(self, importo) :
        print("Hai pagato tramite bonifico la seguente cifra: " ,importo)

class GestorePagamenti :
    def __init__(self, metodo_pagamento) :
        self.metodo_pagamento = metodo_pagamento
    
    def gestisci_pagamento(self, importo) :
        self.metodo_pagamento.effettua_pagamento(importo)

carta_di_credito = CartaDiCredito()
bonifico = BonificoBancario()
paypal = PayPal()

gestore1 = GestorePagamenti(carta_di_credito).gestisci_pagamento(1000)

gestore1 = GestorePagamenti(bonifico).gestisci_pagamento(100)

gestore1 = GestorePagamenti(paypal).gestisci_pagamento(50)

        