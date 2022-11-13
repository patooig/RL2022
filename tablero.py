from mesa import Mesa
from persona import Persona
        

if __name__ == '__main__':
    m = Mesa()
    #print(m.numeroCartasMesa())
    Per1 = Persona("Pato")

    Per2 = Persona("Ivonne")
    Per1.recibeCartas(m.saca3cartasMazo())
    Per1.verMesa(m.getCartasMesa())
    Per1.recogerCartas()
    nuevaMesa = Per1.actualizarMesa()
    m.printCartasMesa()
    

    
    