def isIPv4Address(inputString):
    
    arrayIP = inputString.split(".")
    
    print("Array: ", arrayIP)

    intFlag = 0

    if len(arrayIP) == 4:
        for i in range(len(arrayIP)):

            # Verificamos que NO existan Elementos VACIOS.
            if len(arrayIP[i]) > 0:
                # Convertimos el Elemento de la Posicion (i) en Entero.
                intArrayIP = int(arrayIP[i])
                if (intArrayIP >= 0) and (intArrayIP <= 255):
                    intFlag += 1
            else:
                return False
    else:
        return False

    # FLAG.
    if intFlag == 4:
        return True
    else:
        return False

    

if __name__ == '__main__':
    print(isIPv4Address("172.16.254.1A"))
    #print(isIPv4Address("172.316.254.1"))
    #print(isIPv4Address(".254.255.0"))
    print(isIPv4Address("172.16.254.01"))
    #print(isIPv4Address("172.16.254.11111111111"))

    