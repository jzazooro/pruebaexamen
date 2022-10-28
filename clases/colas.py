class nodoCola(object):

    info , sig = None , None

class Cola(object):

    def __init__(self):
        self.frente , self.final = None, None
        self.tamanio=0
    
    def arribo(cola, dato):
        '''Arriba el dato final de la cola ( Añade el dato final de la cola )'''
        nodo = nodoCola()
        nodo.info = dato
        if cola.frente is None:
            cola.frente=nodo
        else:
            cola.final.sig=nodo
        cola.final = nodo
        cola.tamanio += 1

    def atencion(cola):
        '''Atiende el elemento en el frente de la cola y lo devuelve'''
        dato=cola.frente.info
        cola.frente=cola.frente.sig
        if cola.frente is None:
            cola.final=None
        cola.tamanio-=1
        return dato
    
    def cola_vacia(cola):
        return cola.frente is None

    def en_frente(cola):
        return cola.frente.info
    
    def tamamio(cola):
        return cola.tamanio
    
    def mover_al_final(cola):
        '''Mueve el primer elemento de la cola al final'''
        dato= cola.atencion()
        cola.arribo(dato)
        return dato






def main():
    cola=Cola()
    n1=input('Dato1: ')
    n2=input('Dato2: ')
    cola.arribo(n1)
    cola.arribo(n2)
    print(f'Creamos la cola y añadimos los datos {n1} y {n2} a la cola')
    print(f'Primer dato : {cola.en_frente()}')
    print(f'Movemos el dato {n1} al final de la cola')
    cola.mover_al_final()
    print(f'Nuevo primer dato de la cola {cola.en_frente()}')
    print(f'Tamanio de la cola : {cola.tamamio()}')
 
if __name__=='__main__':
    main()