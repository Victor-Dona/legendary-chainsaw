number_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
even_numbers = []
odd_numbers = []

for i in number_list:
    if i % 2 ==0:
        even_numbers.append(i)
    else:
        odd_numbers.append(i)

print(even_numbers)
print(odd_numbers)