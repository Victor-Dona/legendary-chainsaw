s = input('Write the string to invert: ')

# String Inversion with a for loop
def invert_string_for(s):
    inverted = ""

    for i in range(len(s) -1 , -1, -1):
        inverted += s[i]

    return inverted
    
s_inverted_for = invert_string_for(s)
print(s_inverted_for)
