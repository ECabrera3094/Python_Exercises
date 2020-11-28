def allLongestStrings(inputArray):
    
    if len(inputArray) <= 10:
        if len(inputArray) == 1:
            return inputArray
        else:
            # Encontramos la Cadena MAS Larga.
            intLongest = 0
            for i in range(0, len(inputArray)):
                if len(inputArray[i]) >= intLongest:
                    intLongest = len(inputArray[i])
            
            #return intLongest
            # Almacenamos las Cadenas MAS Largas
            listLongestStrings = []
            for i in range(0, len(inputArray)):
                if len(inputArray[i]) == intLongest:
                    listLongestStrings.append(inputArray[i])

            return listLongestStrings
    else:
        pass

if __name__ == '__main__':
    print( allLongestStrings(["ab", "kkkkkkkk", "aaaaaaa", "ada", "kkkkkkkk"]) )