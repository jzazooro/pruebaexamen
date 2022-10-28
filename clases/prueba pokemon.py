class Nodo(object):

    info,sig=None,None

def main():
    aux=Nodo()
    aux.info='Primer Nodo'
    palabra=input('La palabra\n>>>')
    naux=aux
    while(palabra!=''):
        nodo=Nodo()
        nodo.info=palabra
        naux.sig=nodo
        naux=nodo
        palabra=input('La palabra\n>>>')

    while(aux is not None):
        print(aux.info)
        aux=aux.sig


if __name__=='__main__':
    main()