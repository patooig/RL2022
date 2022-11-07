
import random


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
    
    cartasMazo = list() #Todas las cartas
    cartasMesa = list()

    def __init__(self):
        self.build()
        self.revolverCartas()
        self.numeroCartasMesa()
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
            self.cartasMazo.append(card)

    #Ordena las cartas aleatoriamente en la lista
    def revolverCartas(self):
        random.shuffle(self.cartasMazo)

    #Agrega cartas a la mesa
    def dar4CartasMesa(self):
        for i in range(0,4):
            self.cartasMesa.append(self.cartasMazo.pop())


    #Retorna el numero de cartas boca arriba en la mesa.
    def numeroCartasMesa(self):
        contador = len(self.dar4CartasMesa)
        return contador

    #Imprime en consola las cartas que estan en la mesa
    def dimecartasmesa(self):
        self.dar4CartasMesa()
        for c in self.dar4CartasMesa:
            carta = c
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

    #Como recojo las cartas??
    def recogeCartas(self):

        #Tomamos cada carta
        c1 = self.miMano.pop()
        c2 = self.miMano.pop()
        c3 = self.miMano.pop()

        self.calcularSuma1a1(cc1 = c1)
        self.calcularSuma1a1(cc1 = c2)
        self.calcularSuma1a1(cc1 = c3)
        
        #Combinaciones con la primera carta


    def calcularSuma1a1(cc1):
        


        return 1







        
    


        

if __name__ == '__main__':
    m = Mesa()
    print(m.numeroCartasMesa())
    Per1 = Persona("Pato")
    Per1.recibeCartas(m.saca3cartasMazo())
    

    
    