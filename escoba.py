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
        


class Persona:
    
    #Lista con cartas que tengo en la mano
    miMano = list()

    #Lista de las cartas que hay en la mesa
    m = list()

    #Lista con cartas que ya tengo recogidas
    misCartasRecogidas = list()

    #Constructor de clase Persona
    def __init__(self, name):
        self.nombre = name  #Nombre persona

    #Debe recibir las 3 cartas en la mano
    def recibeCartas(self,c):
        self.miMano = c

    #Como recojo las cartas??

    def recogerCartas(self):

        c1 = self.miMano[0] #Carta 1
        c2 = self.miMano[1] #Carta 2
        c3 = self.miMano[2] #Carta 3

        self.combinacionesMesa()





    def combinacionesMesa(self):
        #Combinaciones posibles de las cartas en la mesa
        combinaciones = list()

        #Combinaciones de 1 carta
        combinaciones.append(self.m[0]) #Agrego la primera carta de la mesa A
        combinaciones.append(self.m[1]) #Agrego la segunda carta de la mesa B
        combinaciones.append(self.m[2]) #Agrego la tercera carta de la mesa C
        combinaciones.append(self.m[3]) #Agrego la cuarta carta de la mesa D

        #Combinaciones de 2 cartas
        for i in range(0,3):
            for j in range(0,4):
                if i != j and i < j:
                    if self.m[i].getValor() + self.m[j].getValor() < 15:
                        aux = list()
                        aux.append([self.m[i],self.m[j]])
                        combinaciones.append(aux)

        #Combinaciones de 3 cartas
        for i in range(0,3):
            for j in range(0,4):
                for k in range(0,4):
                    if i != j and i != k and j != k and i < j and j < k:
                        if self.m[i].getValor() + self.m[j].getValor() + self.m[k].getValor() < 15:
                            aux = list()
                            aux.append([self.m[i],self.m[j],self.m[k]])
                            combinaciones.append(aux)

        #Combinaciones de 4 cartas
        
        if self.m[0].getValor() + self.m[1].getValor() + self.m[2].getValor() + self.m[3].getValor() < 15:
            aux = list()
            aux.append([self.m[0],self.m[1],self.m[2],self.m[3]])
            combinaciones.append(aux)
        
        print("Combinaciones posibles: ", len(combinaciones))
        return combinaciones
  

    def verMesa(self,mesa):
        self.m = mesa


 
        

if __name__ == '__main__':
    m = Mesa()
    #print(m.numeroCartasMesa())
    Per1 = Persona("Pato")
    Per1.recibeCartas(m.saca3cartasMazo())
    Per1.verMesa(m.getCartasMesa())
    Per1.recogerCartas()
    

    
    