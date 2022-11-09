
import random


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

    #Retornoa el palo de la carta
    def getPalo(self):
        return self.palo


class Mesa:
    
    cartasMazo = list() #Todas las cartas
    cartasMesa = list() #Cartas por repartir

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

        #Añade cartas a la lista, acá esta el mazo}
        for card in cartas_todas: 
            self.cartasMazo.append(card)

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
        


class Persona:
    
    #Lista con cartas que tengo en la mano
    miMano = list()

    #Lista de las cartas que hay en la mesa
    m = Mesa().cartasMesa

    #Lista con cartas que ya tengo recogidas
    misCartasRecogidas = list()

    #Constructor de clase Persona
    def __init__(self, name):
        self.nombre = name  #Nombre persona

    #Debe recibir las 3 cartas en la mano
    def recibeCartas(self,c):
        for i in c:
            self.miMano.append(i)

    #Como recojo las cartas??
    def recogeCartas(self):

        #Tomamos cada carta
        c1 = self.miMano.pop()
        #c2 = self.miMano.pop()
        #c3 = self.miMano.pop()

    
        #print(list(combinations))

        #self.calcularSuma1a1(cc1 = c2)
        #self.calcularSuma1a1(cc1 = c3)
        
        #Combinaciones con la primera carta

    def verMesa(self,mesa):
        self.m = mesa






        
    


        

if __name__ == '__main__':
    m = Mesa()
    print(m.numeroCartasMesa())
    Per1 = Persona("Pato")
    
    Per1.recibeCartas(m.saca3cartasMazo())
    Per1.verMesa(m)
    Per1.recogeCartas()
    

    
    