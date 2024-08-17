# This code verifies if the word inputted is a palindrome or not

s = 'rotator'

def string_inverter(s):
    # Inversion of the string
    inverted = ""
    
    for i in range(len(s) - 1, -1, -1):
        inverted += s[i]

    return inverted

inverted_string = string_inverter(s)
print(inverted_string)
print(s)
if inverted_string == s:
    print(f'The word {s} is a palindrome')
else:
    print(f'The word {s} is not a palindrome')


# Palindrome verification through slicing
def slice_palindrome_verifier(s):
    if s[:] == s[::-1]:
        print(f'The string {s} is a palindrome')
    else:
        print(f'The string {s} is not a palindrome')

slice_palindrome_verifier(s)

