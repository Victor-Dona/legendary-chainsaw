s = input('Write the string to invert: ')


# String inversion with a while loop
def invert_string_while(s):
    inverted = ""

    i = len(s) - 1

    while i >= 0:
        inverted += s[i]
        i -= 1
    return inverted

s_inverted_while = invert_string_while(s)

print(s_inverted_while)
