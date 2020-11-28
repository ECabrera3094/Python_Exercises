class Century_from_Year(object):

    def __init__(self):
        pass

    @staticmethod
    def centuryFromYear(year):

        if (1 <= year) and (year <= 2005):
            # Convertimos el Year en Lista.
            year = list(str(year))
            # List Comprenhension.
            # year = [int(x) for x in str(year)]

            # Validamos del Year 1 al 99
            if len(year) <= 2:
                return 1
            #Validamos del Year 100 al 999
            elif len(year) <= 3:
                if (year[1] == '0') and (year[2] == '0'):
                    return int(str(year[0]))
                elif (year[2] >= '1') and (year[1] == '0') or (year[1] > '0'):
                    return int(str(year[0])) + 1
            # Validamos del Year 1000 al 2005
            else:
                if (year[2] == '0') and (year[3] == '0'):
                    return int(str(year[0] + year[1]))
                elif (year[3] >= '1') and (year[2] == '0') or (year[2] > '0'):
                    return int(str(year[0] + year[1])) + 1

        else:
            print("Wrong Year!")


if __name__ == '__main__':
    y = Century_from_Year()
    print(y.centuryFromYear(1))
