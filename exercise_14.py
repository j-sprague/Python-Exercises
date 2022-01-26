def get_combined_dict(dict1, dict2):
    combined_dict = {}
    for i in dict1:
        for j in dict2: #Double for loop so each key checks every key in the other dictionary
            if i == j:
                combined_dict[i] = dict1[i] + dict2[j] #If there's a match, add to combined dictionary and add values
    return combined_dict

my_dict_1 = {'a': 5, 'b': 12, 'c': 3, 'd': 9}
my_dict_2 = {'b': 4, 'c': 9, 'd': 10, 'e': 16}
combined_dict = get_combined_dict(my_dict_1, my_dict_2)
print(combined_dict)
