# The digits 0,4,6 & 9 each have 1 closed pathe, and 8 has 2. 
# number = 649578
# The digits with closed paths are 6,4,9 & 8 
# The total is 1 + 1 + 1 + 2 = 5

def closedPaths(number):

    ans = 0

    dict_paths = { 0:1, 4:1, 6:1, 8:2, 9:1 }

    list_number = [int(a) for a in str(number)]

    for each_number in range(len(list_number)):

        for k in dict_paths.keys():

            if list_number[each_number] == k:

                ans += dict_paths[k]

    return ans

if __name__ == '__main__':
    print(closedPaths(854789))