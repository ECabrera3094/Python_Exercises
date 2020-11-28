class Adjacent_Elements_Products(object):

    def __init__(self):
        pass

    def adjacentElementsProduct(self, inputArray):
        # Almacenaremos los Productos del Array.
        array_Product = []

        for i in range(0, len(inputArray) - 1): # El -1 es para NO Exceder el Lenght Original del Array.
            array_Product.append(inputArray[i] * inputArray[i+1])

        print(array_Product)

        # Inicializamos el Elemento Maximo como el Primer Elemento del Array de Productos.
        int_Max = array_Product[0]

        # buscamos el Producto MAS Grande.
        for i in range(0, len(array_Product)):
            # Si el producto del Array es Mayor a MAX, este tomara su Valor; sino MAX continua siendo el MISMO.
            if array_Product[i] > int_Max:
                int_Max = array_Product[i]

        return int_Max

if __name__ == '__main__':
    aep = Adjacent_Elements_Products()
    print(aep.adjacentElementsProduct([-23,4,-3,8,-12]))