# Same functionality as the previous anagram verifier but optimized

def letter_counter(word):
    letter_count = {}
    for letter in word:
        letter_count[letter] = letter_count.get(letter, 0) + 1
    return letter_count

# Inputs
word_1 = input('We will verify if two words are an anagram.\nPlease input the first word: ')
word_2 = input('Now input the second word: ')

# Anagram verification
if letter_counter(word_1) == letter_counter(word_2):
    print(f'The words "{word_1}" and "{word_2}" form an anagram.')
else:
    print(f'The words "{word_1}" and "{word_2}" do not form an anagram.')
