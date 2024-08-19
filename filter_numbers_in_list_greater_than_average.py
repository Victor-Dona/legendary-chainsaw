# Filtering numbers in a list that are greater than te average of the list.

# First, doing it without incorporated functions
the_list = [2, 4, 6, 8, 10]

n = 0
counter = 0
for i in the_list:
    n += i
    counter += 1

avg = n / counter

filtered_list_a = [i for i in the_list if i > avg]

print(n, counter, avg, filtered_list_a)


# Solving with incorporated functions
avg = sum(the_list) / len(the_list)

filtered_list = [i for i in the_list if i > avg]

print(filtered_list)