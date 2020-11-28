def sockMerchant(n, ar):
    # Obtenemos una Lista con CADA UNO de los Valores del Arreglo.
    set_Elements = list(set(ar))

    
    int_Final = 0

    for i in range(len(set_Elements)):
        int_Signal = 0
        for j in range(len(ar)):
            if (set_Elements[i] == ar[j]):
                print("> :", set_Elements[i],  ar[j])
                int_Signal += 1

        if (int_Signal % 2 == 0):
            int_Final += int_Signal // 2
        elif (int_Signal % 2 != 0):
            int_Final += (int_Signal - 1) // 2

    return int_Final



if __name__ == '__main__':
    print(sockMerchant(9, [10,20,20,10,10,30,50,10,20]))