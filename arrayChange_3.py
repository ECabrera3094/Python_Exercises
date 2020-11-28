def arrayChange(inputArray):

    #i = 1

    intCount = 0

    for i in range(1, len(inputArray)):

        if inputArray[i] <= inputArray[i-1]:

            intDiference = inputArray[i-1] - inputArray[i]
            #print("[i-1]: ", inputArray[i-1], " & [i]: ", inputArray[i])
            #print("Diference: ", intDiference)
            inputArray[i] = inputArray[i] + intDiference + 1
            print("Array: ", inputArray)
            intCount += intDiference + 1
            print("Count: ", intCount)



if __name__ == '__main__':
    print(arrayChange([1,1,1]))
    print("XXXXXXXXXXXXXXXXXXXXXXXXX")
    print(arrayChange([-1000,0,-2,0]))
    print("XXXXXXXXXXXXXXXXXXXXXXXXX")
    print(arrayChange([2,3,3,5,5,5,4,12,12,10,15]))
    print("XXXXXXXXXXXXXXXXXXXXXXXXX")
    print(arrayChange([3122,-645,2616,13213,-8069]))