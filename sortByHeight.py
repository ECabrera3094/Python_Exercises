def sortByHeight(a):

    # Definimos la Lista que Almacenara las Alturas.
    listHeight = []

    # Trasladamos las Alturas a la Lista de Alturas.
    for i in range(0, len(a)):
        if a[i] != -1:
            listHeight.append(a[i])
    
    # ordenamos la Lista.
    listHeight.sort()

    # Reorganizamos las Alturas y los Arboles.
    for i in range(0, len(a)):
        if a[i] != -1:
            # Inseto la Altura de la Posicion CERO. 
            a.insert(i, listHeight[0])
            # Elimino la Siguiente Posicion que NO esta Ordenada.
            del a[i+1]
            # Elimino la Posicion CERO para Recorrer la Lista de Alturas Ordenadas.
            del listHeight[0]

    return a

if __name__ == '__main__':
    print(sortByHeight([-1,150,190,170,-1,-1,160,180]))
    print(sortByHeight([-1]))