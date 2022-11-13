from carta import Carta
from mesa import Mesa       


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

    def verificarCombinacionyCarta(self,c,comb):

        combinacionesValidas = list()

        print("Carta a verificar: ", c.getPalo(), c.getValor())

        #print('Tamaño del vector', len(comb))

        for i in range(len(comb)):


            #Si es de tipo Carta
            if type(comb[i]) is Carta:
                #print("Carta en la mesa: ", comb[i].getPalo(), comb[i].getValor())
                if c.getValor() + comb[i].getValor() == 15:
                    combinacionesValidas.append(comb[i])


            #Si es de tipo lista
            if type(comb[i]) == list:
                for j in range (len(comb[i])):
                    #print("Carta en la mesa: ")
                    sum = 0
                    for k in range (len(comb[i][j])):
                        sum = sum + comb[i][j][k].getValor()
                        #print(comb[i][j][k].getPalo(), comb[i][j][k].getValor())
                    if sum + c.getValor() == 15:
                        combinacionesValidas.append(comb[i])

        print("Combinaciones validas: ", len(combinacionesValidas))
        
        for i in range(len(combinacionesValidas)):
            if type(combinacionesValidas[i]) is Carta:
                print("Carta en la mesa: ", combinacionesValidas[i].getPalo(), combinacionesValidas[i].getValor())
            if type(combinacionesValidas[i]) == list:
                for j in range (len(combinacionesValidas[i])):
                    print("Carta en la mesa: ")
                    for k in range (len(combinacionesValidas[i][j])):
                        print(combinacionesValidas[i][j][k].getPalo(), combinacionesValidas[i][j][k].getValor())
    
                        
        return combinacionesValidas


    def recogerCartas(self):

        c1 = self.miMano[0] #Carta 1
        c2 = self.miMano[1] #Carta 2
        c3 = self.miMano[2] #Carta 3

        comb = self.combinacionesMesa()

        tirarc1 = True
        posibilidadesConC1 = self.verificarCombinacionyCarta(c1,comb)
        if len(posibilidadesConC1) == 0:
            tirarc1 = False

        tirarc2 = True
        posibilidadesConC2 = self.verificarCombinacionyCarta(c2,comb)
        if len(posibilidadesConC2) == 0:
            tirarc2 = False


        tirarc3 = True
        posibilidadesConC3 = self.verificarCombinacionyCarta(c3,comb)
        if len(posibilidadesConC3) == 0:
            tirarc3 = False


        if tirarc1 == False and tirarc2 == False and tirarc3 == False:
            print("No hay combinaciones posibles, se debe tirar una carta del mazo")
            #Tirar una carta del mazo a la mesa

            return False





    def combinacionesMesa(self):
        #Combinaciones posibles de las cartas en la mesa
        combinaciones = list(list())

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

