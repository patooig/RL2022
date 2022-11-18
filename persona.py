from random import randint
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

    #Retorna un arreglo con todas las combinaciones posibles de la mesa
    def verificarCombinacionyCarta(self,c,comb):

        combinacionesValidas = []

        print("Carta a verificar: ", c.getPalo(), c.getValor())


        for i in range(len(comb)):

            #Si es de tipo Carta
            if type(comb[i]) is Carta:
                #print("Carta en la mesa: ", comb[i].getPalo(), comb[i].getValor())
                if c.getValor() + comb[i].getValor() == 15:
                    combinacionesValidas.append(comb[i])


            #Si es de tipo lista
            if type(comb[i]) == list:
                sum = 0
                for j in range (len(comb[i])):
                    #print("Carta en la mesa: ")
                    if type(comb[i][j]) is Carta:
                        #print(comb[i][j].getPalo(), comb[i][j].getValor())
                        sum = sum + comb[i][j].getValor()
                    else:
                        for k in range (len(comb[i][j])):
                            sum = sum + comb[i][j][k].getValor()
                        #print(comb[i][j][k].getPalo(), comb[i][j][k].getValor())
                    if sum + c.getValor() == 15:
                        combinacionesValidas.append(comb[i])

        print("Combinaciones validas: ", len(combinacionesValidas))
        
        #Imprime las combinaciones validas
        '''for i in range(len(combinacionesValidas)):
            if type(combinacionesValidas[i]) is Carta:
                print("Carta en la mesa: ", combinacionesValidas[i].getPalo(), combinacionesValidas[i].getValor())
            if type(combinacionesValidas[i]) == list:
                for j in range (len(combinacionesValidas[i])):
                    print("Carta en la mesa: ")
                    for k in range (len(combinacionesValidas[i][j])):
                        print(combinacionesValidas[i][j][k].getPalo(), combinacionesValidas[i][j][k].getValor())
    '''            
        return combinacionesValidas


    def recogerCartas(self):

        #Verificar si hay cartas en la mesa
        crds = []
        tirar = []
        combinaciones = []

        for i in range (len(self.miMano)):
            crds.append(self.miMano[i])
            tirar.append(False)

        comb = self.combinacionesMesa()    

        for i in range(len(self.miMano)):

            combinaciones = self.verificarCombinacionyCarta(crds[i],comb)
            
            if len(combinaciones) > 0:
                tirar[i] = True
                self._actualizarMesayMano(crds[i],combinaciones)
                break

        '''for i in range(len(self.miMano)):
            if tirar[i] == True:
                self._actualizarMesayMano(crds[i],self.verificarCombinacionyCarta(crds[i],comb))
                break'''
    
        #Si no hay ninguna combinacion posible
        for i in range(len(self.miMano)):
            if tirar[i] == False:
                if len(self.miMano)-1 == i :
                    #Tirar una carta del mazo a la mesa LA ULTIMA
                    self.m.append(self.miMano.pop())
                
      

    def _actualizarMesayMano(self,card,vect):
        if len(vect) == 0:
            return False
        else :
            
            #Recoger cartas de la mesa
            tamC1 = len(vect)
            v = randint(0,tamC1-1)
            
              #Puede ser lista o carta (verificar)
            if type(vect[v]) is Carta:
                self.misCartasRecogidas.append(vect[v]) #Agrego carta a mis cartas recogidas
                self.misCartasRecogidas.append(card) #Agrego carta a mis cartas recogidas
                if self.m.count(vect[v]) == 1:
                    self.m.remove(vect[v])
                
                self.miMano.remove(card) #Elimino carta de mi mano
    
            
            if type(vect[v]) == list:
                for i in range(len(vect[v])):
                    for j in range(len(vect[v][i])):
                        self.misCartasRecogidas.append(vect[v][i][j])
                        if self.m.count(vect[v][i][j]) == 1:
                            self.m.remove(vect[v][i][j])
                self.miMano.remove(card) #Remuevo de la mano
                self.misCartasRecogidas.append(card) #Agrego a mis cartas recogidas

             #Remuevo de la mesa
            
            return True #Retorno True para indicar que se recogio la carta



    def actualizarMesa(self):
        return self.m


    def combinacionesMesa(self):
        #Combinaciones posibles de las cartas en la mesa
        combinaciones = []

        largo_m = len(self.m)

        #Combinaciones de 1 carta


        for i in range(largo_m):
            combinaciones.append(self.m[i])  #Agrego carta individuales a combinaciones
        
        #Combinaciones de 2 cartas
        for i in range(0,largo_m):
            for j in range(0,largo_m):
                if i != j and i < j:
                    if self.m[i].getValor() + self.m[j].getValor() < 15:
                        aux = list()
                        aux.append([self.m[i],self.m[j]])
                        combinaciones.append(aux)

        #Combinaciones de 3 cartas
        for i in range(0,largo_m):
            for j in range(0,largo_m):
                for k in range(0,largo_m):
                    if i != j and i != k and j != k and i < j and j < k:
                        if self.m[i].getValor() + self.m[j].getValor() + self.m[k].getValor() < 15:
                            aux = list()
                            aux.append([self.m[i],self.m[j],self.m[k]])
                            combinaciones.append(aux)

        #Combinaciones de 4 cartas

        for i in range(0,largo_m):
            for j in range(0,largo_m):
                for k in range(0,largo_m):
                    for l in range(0,largo_m):
                        if i != j and i != k and i != l and j != k and j != l and k != l and i < j and j < k and k < l:
                            if self.m[i].getValor() + self.m[j].getValor() + self.m[k].getValor() + self.m[l].getValor() < 15:
                                aux = list()
                                aux.append([self.m[i],self.m[j],self.m[k],self.m[l]])
                                combinaciones.append(aux)

    
        nn = 5
        while nn <= largo_m:  #Supongamos que hay 5 cartas en la mesa
            suma = 0   
            aux = list() 
            for i in range(0,nn):
                aux.append(self.m[i])
                suma = suma + self.m[i].getValor()
            if suma < 15:
                combinaciones.append(aux)  
            nn+=1 
        
        print("Combinaciones posibles: ", len(combinaciones))
        return combinaciones
  

    def verMesa(self,mesa):
        self.m = mesa


    def getNumCartasMano(self):
        return len(self.miMano)

    def getNumCartasRecogidas(self):
        return len(self.misCartasRecogidas)