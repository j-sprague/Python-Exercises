cool_list = []
dupes = []

for i in range (10):
    val = int(input('Enter a number: '))
    if val not in dupes and val in cool_list:
        cool_list.remove(val)
        dupes.append(val)
    elif val not in dupes and val not in cool_list:
        cool_list.append(val)

print(cool_list)
