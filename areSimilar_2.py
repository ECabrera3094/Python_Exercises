def areSimilar(A, B):

    print("SUM: ", sum([a!=b for a,b in zip(A,B)])) 

    print("Sorted: ", sorted(A), " & ", sorted(B))

    print(True and 2)

    return sorted(A)==sorted(B) and sum([a!=b for a,b in zip(A,B)]) <= 2

if __name__ == '__main__':
    print(areSimilar([1,2,3], [2,1,3]))
    print("XXXXXXXXXXXXXXXXXXXXXXXXXX")

    print(areSimilar([1,2,3], [1,2,3]))
    print("XXXXXXXXXXXXXXXXXXXXXXXXXX")