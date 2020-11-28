class Make_Array_Consecutive(object):

    def __init__(self):
        pass

    def makeArrayConsecutive2(self, statues):
        intMax = 0
        intMin = 20

        for i in range(0, len(statues)):
            intMin = min(intMin, statues[i])
            intMax = max(intMax, statues[i])
            print("i: ", i, " - Min: ", intMin, " - Max: ", intMax)

        return intMax - intMin - len(statues) + 1


if __name__ == '__main__':
    mac = Make_Array_Consecutive()
    print(mac.makeArrayConsecutive2([6,2,3,8]))