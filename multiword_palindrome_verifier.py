# Verifying for a multi-word palindrome.
# Good multi-word palindrome to test the code 'A man a plan, a canal: Panama!'
s = input('Insert a word or text to verify if it is a palindrome: ')

def palindrome_verifier(s):
    normalized_string = ""
    # Normalizing the string
    for char in s:
        if 'a' <= char <= 'z' or 'A' <= char <= 'Z' or '0' <= char <= '9':
            if 'A' <= char <= 'Z':
                char = chr(ord(char) + 32)
            normalized_string += char

    # Verifying for a palindrome
    start = 0
    end = len(normalized_string) - 1

    while start < end:
        if normalized_string[start] != normalized_string[end]:
            return print(f'{s} is not a palindrome')
        start += 1
        end -= 1
        
    return print(f'{s} is a palindrome')

palindrome_verifier(s)
