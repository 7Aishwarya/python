def is_palindrome(s):
    if s == '':
        return True
    else:
        if (ord(s[0]) - ord(s[len(s)-1])) == 0:
            is_palindrome(s[1:len(s)-1])
        else:
            return False

print (is_palindrome(''))
#>>> True    (expected = True)

print(is_palindrome('abab'))
#>>> False    (expected = False)

print(is_palindrome('abba'))
#>>> None    (expected = True)

print (is_palindrome('andrea'))
#>>> None    (expected = False)

print(is_palindrome('abaaba'))
#>>> None    (expected = True)
