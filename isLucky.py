def isLucky(n):
    
    if (n >= 10) and (n <= 1000000):

        # Convertimos el Int en Lista.
        listNumber = list(map(int, str(n)))
        
        print(listNumber)

        # Verificamos que sea PAR la Lista. 
        if len(listNumber) % 2 == 0:
            # Definimos las Listas donde se almacenaran los Numeros.
            listLeft = []
            listRight = []

            # Definimos la Mitad de la Lista de Numeros.
            intHalf = len(listNumber)//2

            for i in range(0, intHalf):
                listLeft.append(listNumber[i])

            for i in range(intHalf, len(listNumber)):
                listRight.append(listNumber[i])

            print("Izquierda; ", listLeft)
            print("DERECHA: ", listRight)

            # Realizamos la Suma de cada Lista y Comparamos.
            intLeftResult = 0
            intRightResult = 0

            for i in range(0, len(listLeft)):
                intLeftResult += listLeft[i]

            for i in range(0, len(listRight)):
                intRightResult += listRight[i]

            print("Resultado Izquierda: ", intLeftResult)
            print("Resultado Derecha: ", intRightResult)

            if (intLeftResult == intRightResult):
                return True
            else:
                return False

        else:
            return False
    else: 
        return False

if __name__ == '__main__':
    print(isLucky(239017))