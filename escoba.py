
import random


class Carta(object):
    #Se defice palo y valor de la carta
    def __init__(self, p, v):
        self.palo = p 
        self.valor = v

    #Carta es jugable o no (esta en la mano)
    def jugable(self, opec_p, opec_v):
        if(self.palo == opec_p) or (self.valor == opec_v):
            return True

    def printMe(self):
        print(self.palo, self.valor)


class Mesa(object):
    def __init__(self):
        self.cards = list()
        self.cards_disc = list()
        self.build()
        self.revolverCartas()
        self.dimelo()
        

    def build(self):

        #Palos disponibles en el juego : oro, basto, copa, espada
        #Genera los objetos carta
        cartas_oro = [Carta("ORO",i) for i in range(1,11)]
        cartas_bas = [Carta("BAS",i) for i in range(1,11)]
        cartas_cop = [Carta("COP",i) for i in range(1,11)]
        cartas_esp = [Carta("ESP",i) for i in range(1,11)]

        cartas_todas = cartas_oro + cartas_bas + cartas_cop + cartas_esp

        #Añade cartas a la lista, acá esta el mazo}

        
        for card in cartas_todas: 
            
            self.cards.append(card)


    def revolverCartas(self):
        random.shuffle(self.cards)

        
    def dimelo(self):
        contador = 0    
        for c in self.cards:
            carta = c
            carta.printMe()
            contador = contador + 1
        print(contador)
    

    #Retorna el mazo


if __name__ == '__main__':
    Mesa()