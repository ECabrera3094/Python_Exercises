def alternatingSums(a):
    
    listSums = [0, 0]

    for i in range (0, len(a)):
        if i % 2 == 0:
            listSums.insert(0, listSums[0]+a[i])
            listSums.pop(1)
        else:
            listSums.insert(1, listSums[1]+a[i])
            listSums.pop(2)

    return listSums

if __name__ == '__main__':
    print(alternatingSums([50,60,60,45,70]))
    print("XXXXXX")
    print(alternatingSums([180]))