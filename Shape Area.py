class Shape_Area(object):

    def __init__(self):
        pass

    def shapeArea(self, n):

        # Creamos el Array Base de N.
        array_Base = []

        # Creamos el Array Base de N-1
        array_Base_2 = []

        intResult = 0

        if n == 1:
            intResult = 1
            return intResult
        else:

            # Ingresamos los Valores del Array Base de N.
            for i in range(n):
                array_Base.append(n)

            print(array_Base)

            # Ingresamos los Valores del Array Base de N - 1.
            for i in range(n-1):
                array_Base_2.append(n-1)

            print(array_Base_2)

            # Sumamos los Elementos de los Arrays.
            for i in range(len(array_Base)):
                intResult += array_Base[i]

            for i in range(len(array_Base_2)):
                intResult += array_Base_2[i]

        print("Resultado: ",intResult)

if __name__ == '__main__':
    sa = Shape_Area()
    sa.shapeArea(4)