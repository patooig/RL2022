
class Carta:

    valor = 0
    palo = ''
    #Se defice palo y valor de la carta
    def __init__(self, p, v):
        self.palo= p 
        self.valor = v

    #Carta es jugable o no (esta en la mano)
    def jugable(self, opec_p, opec_v):
        if(self.palo == opec_p) or (self.valor == opec_v):
            return True

    def printMe(self):
        print(self.palo, self.valor)

    #Retorna el valor de la carta
    def getValor(self):
        return self.valor

    #Retorna el palo de la carta
    def getPalo(self):
        return self.palo
