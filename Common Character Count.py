def commonCharacterCount(s1, s2):
    
    # Construimos un Diccionario por cada String.
    dict_s1 = constructDict(s1)
    dict_s2 = constructDict(s2)

    #print("dict 1: ", dict_s1)
    #print("dict 2: ", dict_s2)

    # Obtenemos una lista de las LLAVES del previo Diccionario.
    dict_s1 = dict_s1.keys()
    dict_s2 = dict_s2.keys()
    
    intCommonCharCount = 0

    # Comparamos cada Elemento de las Listas de Llaves.
    for i in range(0, len(dict_s1)):
        for j in range(0, len(dict_s2)):
            if dict_s1[i] == dict_s2[j]:
                intCommonCharCount += 1

    return (intCommonCharCount)
    
    
def constructDict(myStr):
    dict_Str = {}
    for n in myStr:
        # Devolvemos una Lista con las Llaves del Diccionario que iremos Llenando en cada Iteracion.
        keys = dict_Str.keys()
        print("Keys:", keys)
        if n in keys:
           dict_Str[n] += 1
        else:
            dict_Str[n] = 1 
    return (dict_Str)


if __name__ == '__main__':
    print( commonCharacterCount("zzzz", "zzzzz") )
    print("xxxxxxxxxxxxxxxxxxxx")
    print( commonCharacterCount("aabcc", "abcce") )