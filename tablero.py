from mesa import Mesa
from persona import Persona
        

if __name__ == '__main__':
    m = Mesa()
    #print(m.numeroCartasMesa())
    Per1 = Persona("Pato")
    Per2 = Persona("Ivonne")

    '''Per1.recibeCartas(m.saca3cartasMazo())

    Per2.recibeCartas(m.saca3cartasMazo())

    print('Cartas de Pato en mano: ', end='')
    Per1.getNumCartasMano() 
    print()   
    Per1.recogerCartas()

    Per2.verMesa(m.getCartasMesa())
    Per2.recogerCartas()
    Per2.getNumCartasMano()
    m.'''
       

    while m.getNumCartasMazo() >= 0:
        Per1.verMesa(m.getCartasMesa())
        
        Per1.recogerCartas()
    
        nuevaMesa = Per1.actualizarMesa()
        m.printCartasMesa()

        m.setMesa(nuevaMesa)
    
        Per2.verMesa(m.getCartasMesa())
        Per2.recogerCartas()
        nuevaMesa = Per2.actualizarMesa()
        m.setMesa(nuevaMesa)
        print('IMPRIMO MESA')
        m.printCartasMesa()
        print('Quedan ', m.getNumCartasMazo(), ' cartas en el mazo')

        print('Pato tiene ', len(Per1.miMano), ' cartas en la mano')
        print('Ivonne tiene ', len(Per2.miMano), ' cartas en la mano')



        if Per1.getNumCartasMano() == 0 and Per2.getNumCartasMano() == 0:
            if m.getNumCartasMazo() == 0:
                print('entro')
                break #Termina el juego

            Per1.recibeCartas(m.saca3cartasMazo())
            Per2.recibeCartas(m.saca3cartasMazo())
    

    print()
    print('Pato tiene ',Per1.getNumCartasRecogidas()) 
    print()
    print('Ivonne tiene ',Per2.getNumCartasRecogidas()) 
    
    