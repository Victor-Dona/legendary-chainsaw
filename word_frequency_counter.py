# Input: "manzana naranja manzana pera naranja manzana"
# Desired output: {'manzana': 3, 'naranja': 2, 'pera': 1}

text = 'manzana naranja manzana pera naranja manzana'

new_text = text.split()

frequency_counter = {}

for word in new_text:
    if word in frequency_counter:
        frequency_counter[word] +=  1
    else:
        frequency_counter[word] = 1


print(frequency_counter)
print(new_text)