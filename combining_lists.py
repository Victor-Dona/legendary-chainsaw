# Combining lists

# If lists have the same lenght
list1 = [1, 3, 5, 7]
list2 = [2, 4, 6]
combined_list = []

for i in range(min(len(list1), len(list2))):
    combined_list.append(list1[i])
    combined_list.append(list2[i])


# If lists have different lenghts
if list1 > list2:
    combined_list.extend(list1[len(list2):])
else:
    combined_list.extend(list2[len(list1):])

print(combined_list)