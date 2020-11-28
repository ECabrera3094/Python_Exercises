class Check_Palindrome(object):

    def __init__(self):
        pass

    def checkPalindrome(self, inputString):

        # Invertimos la Cadena original.
        newString = inputString[::-1]

        # Invertimos la Cadena original.
        # newString = "".join(reversed(inputString))

        if inputString == newString:
            return True
        else:
            return False


if __name__ == '__main__':
    cp = Check_Palindrome()
    cp.checkPalindrome("Emiliano")