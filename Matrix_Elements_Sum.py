class Matrix_Elements_Sum(object):

    def __int__(self):
        pass

    def matrixElementsSum(self, matrix):
        # Variable donde se Sumaran los valores de la Matriz.
        intSuma = 0

        # Verificamos las Dimensiones de la Matriz.
        if (len(matrix) >= 1) and (len(matrix) <= 5):
            # Filas.
            for i in range(len(matrix)):
                len_Colums = len(matrix[i]) # Longitud de las Columnas
                if (len_Colums >= 1) and (len_Colums <= 5):
                    # Columnas.
                    for j in range(len_Colums):
                        # Si es la Primer Fila, NO Requiere hacer Verificaciones.
                        if i == 0:
                            # Si Algun Elemento de Primer Renglon es Cero, en automatico, convierte el de Abajo en Cero.
                            if (matrix[i][j] == 0):
                                matrix[i+1][j] = 0
                            elif (matrix[i][j] >= 1) and (matrix[i][j] <= 10):
                                intSuma += matrix[i][j]
                        # El Resto de las Filas.
                        else:
                            if (matrix[i][j] >= 1) and (matrix[i][j] <= 10) and (matrix[i-1][j] >= 1):
                                intSuma += matrix[i][j]

        print("Suma: ", intSuma)



if __name__ == '__main__':

    mes = Matrix_Elements_Sum()

    matrix_2 = [[1, 0, 3],
                [0, 2, 1],
                [1, 2, 0]]

    mes.matrixElementsSum(matrix_2)

    matrix_3 = [[1, 1, 1, 0],
              [0, 5, 0, 1],
              [2, 1, 3, 10]]

    mes.matrixElementsSum(matrix_3)

    matrix_4 = [[1],
                [5],
                [0],
                [2]]

    mes.matrixElementsSum(matrix_4)