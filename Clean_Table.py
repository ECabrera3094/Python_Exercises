def solution(S):

    my_rows = S.split('\n') # Dividimos la Cadena en una Lista.

    new_table = []

    for row in my_rows:
        if "NULL" not in row:
            new_table.append(row)

    ans = "\n".join(new_table) # Convertimos la Lista en una sola Cadena unida por Saltos.

    return ans

print(solution("id,name,age,socre\n1,Jack,NULL,12\n17,Betty,28,11"))