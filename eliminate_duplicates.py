import time

# Elmininating duplicates

input_list = [1, 2, 2, 3, 4, 4, 5]
output_list = [1, 2, 3, 4, 5]


# Creating empty list to include unique values
empty_list = []

start_time = time.time()

# Looping through the list and adding unique values 
for i in input_list:
    if i not in empty_list:
        empty_list.append(i) 

end_time = time.time()

run_duration = (end_time - start_time) * 1000
run_duration = round(run_duration, 5)

print(f'List of unique values: {empty_list}')
print(f'Execution time with for loop: {run_duration}: miliseconds')


# Elmininating duplicates with set for improved efficiency
input_list = [1, 2, 2, 3, 4, 4, 5]
output_list = [1, 2, 3, 4, 5]

unique_set = set(input_list)

unique_list = list(unique_set)

start_time = time.time()

end_time = time.time()

run_duration = (end_time - start_time) * 1000
run_duration = round(run_duration, 5)

print(f'List of unique values: {unique_list}')
print(f'Execution time with set function: {run_duration}: miliseconds')