def arrayMaximalAdjacentDifference(inputArray):

    int_max = -2147483648

    for i in range(0, len(inputArray)-1):

        print("[i]: ", i)
        print("MAX: ", int_max)
        print("Array[i]: ",inputArray[i] , " \nArray[i+1]; ", inputArray[i+1])

        int_max = max( int_max, abs( inputArray[i] - inputArray[i+1] ) )
        
        print("NEW MAX: ", int_max)
        print("------------------------------------------")

    return int_max

if __name__ == '__main__':
    print(arrayMaximalAdjacentDifference([2,4,1,0]))