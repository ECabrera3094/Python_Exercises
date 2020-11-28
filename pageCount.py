def pageCount(n, p):

    # n = longitud del array
    # p = pagina deseada.

    listEven = [ x for x in range(n+1) if x % 2 == 0]
    
    listOdd = [x for x in range (n+1) if x % 2 != 0]
    
    if len(listEven) > len(listOdd):
        listOdd.append(0)
    else:
        listEven.append(0)

    print("Pares: ", listEven)
    print("Impares: ", listOdd)
    
    listOfTuples = list( zip(listEven, listOdd) )

    print("> Lista de Tuplas: ", listOfTuples)
    print("> Len: ", len(listOfTuples))

    leftJump = 0

    for i in range(len(listOfTuples)):
        for j in range(2):
            print("[" , i , "][" , j , "]: ",  listOfTuples[i][j])
            if (p == listOfTuples[i][j]):
                print("\r AQUI")
                leftJump = i

    print("------------------------")
    
    rightJump = 0

    listOfTuples = listOfTuples[::-1]
    print("Nueva Lista: ", listOfTuples)

    for i in range(len(listOfTuples)):
        for j in range(2):
            print("[" , i , "][" , j , "]: ",  listOfTuples[i][j])
            if (p == listOfTuples[i][j]):
                print("\r AQUI")
                rightJump = i

    print("------------------------")

    print(leftJump, " -- ", rightJump)

    if leftJump > rightJump:
        return rightJump
    else:
        return leftJump

if __name__ == '__main__':
    print("Saltos: ", pageCount(6,5))