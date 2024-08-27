# Substring generator: script that verifies all possible string combinations out of a word.
def generate_substrings(input_string):
    substrings = []
    for start in range(len(input_string)):
        for end in range(start + 1, len(input_string) + 1):
            substrings.append(input_string[start:end])
    return substrings

# Ejemplo de uso
input_string = "hola"
result = generate_substrings(input_string)
print(result)
