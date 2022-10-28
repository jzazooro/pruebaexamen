class hashNodo(object):

    info , sig = None , None


class Hash(object):

    def __init__(self):
        self.tabla=[]
        self.tamanio=0

    def bernstein(self,cadena):
        '''Solo Funciona para cadenas de caracteres'''
        h=0
        for caracter in cadena:
            h = h *33 + ord(caracter)
        return h

    def crear_tabla(self,tamanio):
        self.tabla=[None]*tamanio
        self.tamanio=tamanio
        return self.tabla

    def __str__(self):
        return print(self.tabla)
    
    def cantidad_elementos(self):
        return self.tamanio-self.tabla.count(None)

    def funcion_hash(self,dato):
        '''Posicion del dato en la tabla'''
        return self.bernstein(str(dato))% self.tamanio
    
    def agregar(self,tabla,dato):
        '''Agrega un elemento a la tabla'''
        posicion=self.funcion_hash(dato)
        aux=hashNodo()
        aux.info=dato
        
        if(tabla[posicion] is None):
            tabla[posicion]=aux
            print(f'{aux.info} instertado con exito a la tabla')
            self.tabla=tabla
        else:
            aux2=tabla[posicion]
            while(aux2.sig!=None):
                aux2=aux2.sig            
            aux2.sig=aux
            print(f'Se ha adherido ({aux2.info}) a la cola con exito, su puntero apunta a ({aux2.sig.info}),\nel cual apunta a (None)')
            print(f'Ahora el nodo ({aux2.info}) apunta hacia ({aux2.sig.info})')
            self.tabla=tabla
    
    def buscar(self,buscado):
        '''Busca un elemento dentro de la tabla y devuelve sus datos'''
        dato= None
        posicion=self.funcion_hash(buscado)
        naux=self.tabla[posicion]
        if(naux is not None):
            while(naux is not None and dato is None):
                if(naux.info==buscado):
                    dato= naux.info
                else:
                    nodo=naux.sig
                    naux=nodo
        return dato
    
    def quitar(self,dato):
        '''Busca un elemento dentro de la tabla y lo elimina'''
        posicion=self.funcion_hash(dato)
        aux=self.tabla[posicion]
        aux0=None
        
        while(aux.info!=dato):
            aux0=aux
            aux=aux.sig
        aux0.sig=aux.sig




def main():
    hashing=Hash()
    n=int(input('Introduzca el tamaño de la tabla deseado: '))
    
    tabla_hash=(hashing.crear_tabla(n))
    nuevodato=input('Dato a añadir (None para salir)\n>>>')
    while(nuevodato!=''):
        hashing.agregar(tabla_hash,nuevodato)
        nuevodato=input('Dato a añadir (None para salir)\n>>>')
    
    print(tabla_hash.__str__())
    eliminar=input('Que dato desea eliminar\n>>>')
    hashing.quitar(eliminar)
    buscador=input('Que dato desea buscar\n>>>')
    resultado=hashing.buscar(buscador)
    print(resultado)


if __name__=='__main__':
    main()