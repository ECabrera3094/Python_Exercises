def decimal_a_binario(decimal):

    binario = ""

    while decimal > 0:

        residuo = int(decimal % 2)

        decimal = int(decimal / 2)

        binario = str(residuo) + binario

    return binario

print(decimal_a_binario(56))