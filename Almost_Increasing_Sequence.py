class Almost_Increasing_Sequence(object):

    def __init__(self):
        pass

    def almostIncreasingSequence(self, sequence):

        for i in range(0, len(sequence)):
            newSequence = sequence.copy()
            newSequence.pop(i)
            intFlag = 0
            for j in range(0, len(newSequence) - 1):
                if newSequence[j] < newSequence[j + 1]:
                    print("i: ", i, " - Sequence: ", sequence, " - NewSequence", newSequence)
                    intFlag += 1
                    print("j: ", j, " - ", newSequence[j], "<", newSequence[j + 1], " - Flag: ", intFlag)
                    continue
                else:
                    break

            if intFlag == (len(newSequence)-1):
                return True

        return False


if __name__ == '__main__':
    ais = Almost_Increasing_Sequence()
    print(ais.almostIncreasingSequence([-0.1,-0.3,-0.2]))