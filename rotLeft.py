def rotLeft(a, d):

    return a[d:] + a[:d]


    for i in range(d):
        temp = a[0]
        print("Temp: ", temp)
        for j in range(len(a) - 1):
            a[j] = a[j + 1]
            print("a[j] :", a[j])
        a[len(a) - 1] = temp
        print(" a[len(a) - 1] = temp", a[len(a) - 1])

    return a

if __name__ == '__main__':
    print(rotLeft([1,2,3,4,5], 4))
    #print(rotLeft([41, 73, 89, 7 ,10, 1, 59, 58, 84, 77, 77, 97, 58, 1 ,86, 58, 26, 10 ,86 ,51], 10))

    