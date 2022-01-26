def get_unique_list(list):
    unique_list = []
    for i in list: 
        if i not in unique_list:
            unique_list.append(i) #If item isn't already in unique list, add value
    return unique_list

my_list = [1, 2, 3, 2, 1, 4]
unique_list = get_unique_list(my_list)
print(unique_list)
