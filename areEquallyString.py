def areEquallyString(yourLeft, yourRight, friendsLeft, friendsRight):

    if (yourLeft == friendsRight) and (yourRight == friendsLeft):

        return True
    elif (yourRight == friendsRight) and (yourLeft == friendsLeft):

        return True
    else:

        return False

if __name__ == '__main__':

    print(areEquallyString(10, 15, 15, 10))