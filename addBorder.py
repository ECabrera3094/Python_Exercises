def addBorder(picture):
    
    # La Cantidad de * que se van a Agregar,
    intAsterisk = len(picture[0])

    # Ingreso de * en la Posicion CERO.
    picture.insert(0, (intAsterisk+2) * '*')
    
    # Obtenemos la Nueva Longitud del Arreglo.
    intLastPosition = len(picture)

    # Ingreso de * en la ULTIMA Posicion.
    picture.insert(intLastPosition, (intAsterisk+2) * '*')

    for i in range(1, len(picture)-1):

        picture[i] = '*' + picture[i] + '*'

    return picture

if __name__ == '__main__':
    print(addBorder(["abc", "ded"]))