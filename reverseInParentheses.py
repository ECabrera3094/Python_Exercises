def reverseInParentheses(s):
    
    print( '"'+ s.replace('(', '"+("').replace(')', '")[::-1]+"') + '"' )

    return eval('"' + 
    s.replace('(', '"+("').replace(')', '")[::-1]+"') + 
    '"')



if __name__ == '__main__':
    print(reverseInParentheses("foo(bar(baz))blim"))
    print("XXXXXXXXXXXXXXXXXX")
    print(reverseInParentheses("foo(bar(baz(blim)))blim"))