# Character frequency counter

def character_frequency_counter():
    text = input('Input text for character counting: ')

    print(text)
    char_frequency_counter = {}

    for char in text:
        if char in char_frequency_counter:
            char_frequency_counter[char] += 1
        else:
            char_frequency_counter[char] = 1

    # Sorting alphabetically 
    sorted_keys = sorted(char_frequency_counter.keys())
    sorted_dict = {key: char_frequency_counter[key] for key in sorted_keys}
    print(sorted_dict)


character_frequency_counter()
