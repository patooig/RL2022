
import random
from tkinter import SEL


class Carta:

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


class Mesa:
    
    todasCartas = list() #Todas las cartas
    cardsMesa = list()

    def __init__(self):
        self.build()
        self.revolverCartas()
        self.dimelo()
        self.dimecartasmesa()
 
        

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
            self.todasCartas.append(card)


    def revolverCartas(self):
        random.shuffle(self.todasCartas)

    def cartasMesa(self):
        for i in range(0,4):
            self.cardsMesa.append(self.todasCartas.pop())
        
    def dimelo(self):
        contador = 0    
        for c in self.todasCartas:
            carta = c
            carta.printMe()
            contador = contador + 1
        print(contador)

    def dimecartasmesa(self):
        self.cartasMesa()
        for c in self.cardsMesa:
            carta = c
            carta.printMe()

    def saca3Cartas(self):
        l = list()
        for i in range(0,3):
            l.append(self.todasCartas.pop())
        return l
        


class Persona:
    
    #Lista con cartas que tengo en la mano
    miMano = list()

    #Lista con cartas que ya tengo recogidas
    misCartasRecogidas = list()


    def __init__(self, name):

        #Nombre persona
        self.nombre = name

    def recibeCartas(self,c):
        #Debe recibir las 3 cartas en la mano
        for i in c:
            self.miMano.append(i)

    def recogeCartas(self):
        self.misCartasRecogidas.append()


        
    


        

if __name__ == '__main__':
    m = Mesa()
    m.dimelo()
    Per1 = Persona("Pato")
    Per1.recibeCartas(m.saca3Cartas())
    
    