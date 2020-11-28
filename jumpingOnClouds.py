def jumpingOnClouds(c):
    
    c.append(1)

    int_Jump = 0
    i = 0
    bln_Stop = True

    while bln_Stop:

        try:

            if (c[i + 1] == 0) and (c[i + 2] == 0):
                int_Jump += 1
                i += 2
                print("Jump: ", int_Jump, " & i: ", i)

            if ((c[i + 1] == 1)) and (c[i + 2] == 0):
                int_Jump += 1
                i += 2
                print("Jump: ", int_Jump, " & i: ", i)

            if ((c[i + 1] == 0)) and (c[i + 2] == 1):
                int_Jump += 1
                i += 1
                print("Jump: ", int_Jump, " & i: ", i)

        except IndexError:
            bln_Stop = False
            break

    return int_Jump


if __name__ == '__main__':
    print(jumpingOnClouds([0,0,1,0,0,1,0]))
    print(jumpingOnClouds([0,0,0,1,0,0]))






    
