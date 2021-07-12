def checkForAnagrams(word, arr):
    # Checking if the word has an anagram in the sliced array.
    for x in arr:
        if (sorted(word) == sorted(x)):
            return True
    return False
            
def funWithAnagrams(text):
    text.reverse()
    # Creating a copy of the list which will be modified,
    # and will not affect the array slicing during the loop.
    final_text = list(text)

    # Looping through the list in reverse since we're eliminating
    # the second anagram we find from the original list order.
    myflag = 0
    for i in range(len(text)):

        print(">>>: ", text[i+1:])

        if text[i+1:] and checkForAnagrams(text[i], text[i+1:]):
            final_text.pop(i - myflag)
            myflag += 1
        else:
            pass

    print(sorted(final_text))

    return sorted(final_text)
        
if __name__ == '__main__':

    funWithAnagrams(['code', 'aaagmnrs', 'anagrams', 'doce'])