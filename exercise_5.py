# Worked on with Alex Stahlman

list1 = []
list2 = []
similar_values = []

for i in range(5):
    list1.append(int(input('Enter a number for first list: ')))

for i in range(5):
    list2.append(int(input('Enter a number for second list: ')))

for i in list1:
    for h in list2:
        if i == h:
            if i not in similar_values:
                similar_values.append(h)

print(similar_values)
