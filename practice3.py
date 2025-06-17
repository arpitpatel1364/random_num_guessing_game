# remove duplicates from list
my_list = [1, 2, 2, 3, 4, 4, 5]
new_list = []
for item in my_list:
    if item not in new_list:
        new_list.append(item)
print(new_list)
