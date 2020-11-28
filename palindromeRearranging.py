def palindromeRearranging(inputString):
    odds=0
    myset=set(inputString)
    for i in myset:
        n=inputString.count(i)
        if n%2!=0:
            odds+=1
    return odds<=1