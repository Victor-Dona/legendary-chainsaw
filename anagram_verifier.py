# User inputs first word. we create dictonary to store letters and frequency of appearance
word_1 = input('We will verify of two words are an anagram.\nPlease input the first word: ')
# print(word_1)

dict_1 = {}
# print(dict_1)

# Same workflow as above for word 2
word_2 = input('Now input the second word: ')
dict_2 = {}

# print(word_2)

# Veifying for word lengths. 
if len(word_1) == len(word_2):
    # Verifiyng that both words include the same letters
    for letter in word_1:
        if letter in dict_1.keys():
            dict_1[letter] += 1
        else:
            dict_1[letter] = 1
    for letter in word_2:
    # Verifying for the second word    
        if letter in dict_2.keys():
            dict_2[letter] += 1
        else:
            dict_2[letter] = 1        

    # Sorting dictionary keys    
    dict_1_sorted_keys = sorted(dict_1.keys())
    dict_2_sorted_keys = sorted(dict_2.keys())

    dict_1_sorted = {key: dict_1[key] for key in dict_1_sorted_keys}
    dict_2_sorted = {key: dict_2[key] for key in dict_2_sorted_keys}

    if dict_1_sorted_keys == dict_2_sorted_keys:
        anagram = True
        for key in dict_1_sorted_keys:
            if dict_1_sorted[key] != dict_2_sorted[key]:
                anagram = False
                break
        if anagram:
            print(dict_1_sorted)
            print(dict_2_sorted)
            print(f'The words {word_1} and {word_2} form an anagram.')
        else:
            print('These two words are the same length and contain the same letters, but not in the same quantity.') 

    else:
        print('These two words are the same length, but do not contain the same letters.') 

else:
    print('These two words are not the same length.')
