from carta import Carta
import random


class Mesa:
#hola
    cartasMazo = list() #Todas las cartas
    cartasMesa = list() #Cartas en la mesa

    def __init__(self):
        self.build()
        self.revolverCartas()
        self.darCartasMesa()
        self.printCartasMesa()
 
        

    def build(self):

        #Palos disponibles en el juego : oro, basto, copa, espada
        #Genera los objetos carta
        cartas_oro = [Carta("ORO",i) for i in range(1,11)]
        cartas_bas = [Carta("BAS",i) for i in range(1,11)]
        cartas_cop = [Carta("COP",i) for i in range(1,11)]
        cartas_esp = [Carta("ESP",i) for i in range(1,11)]

        cartas_todas = cartas_oro + cartas_bas + cartas_cop + cartas_esp

        #Agrega las cartas a la lista de cartas del mazo
        self.cartasMazo = cartas_todas
        
        

    #Ordena las cartas aleatoriamente en la lista
    def revolverCartas(self):
        random.shuffle(self.cartasMazo)

    #Agrega cartas a la mesa
    def darCartasMesa(self):
        for i in range(0,4):
            self.cartasMesa.append(self.cartasMazo.pop())


    #Retorna el numero de cartas boca arriba en la mesa.
    def numeroCartasMesa(self):
        contador = len(self.cartasMesa)
        return contador

    #Imprime en consola las cartas que estan en la mesa
    def printCartasMesa(self):
        for i in range(len(self.cartasMesa)):
            carta = self.cartasMesa[i]
            carta.printMe()

    #Sacar 3 cartas del mazo.
    def saca3cartasMazo(self):
        l = list()
        for i in range(0,3):
            l.append(self.cartasMazo.pop())
        return l

    #Retorna lista de cartas en la mesa.
    def getCartasMesa(self):
        return self.cartasMesa

    def setMesa(self,mesa):
        self.cartasMesa = mesa