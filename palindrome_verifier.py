# This code verifies if the word inputted is a palindrome or not

s = 'rotator'

def palindrome_verifier(s):

    # Inversion of the string
    inverted = ""

    for i in range(len(s) - 1, -1, -1):
        inverted += s[i]

    return inverted

inverted_string = palindrome_verifier(s)
print(inverted_string)
print(s)
if inverted_string == s:
    print('It is a palindrome')
else:
    print('Not a palindrome')


# Pending to develop it with multi-word palindromes. 'anita lava la tina, for example'


