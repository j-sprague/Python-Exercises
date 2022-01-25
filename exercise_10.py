# Worked with Alex Stahlman

str1 = str(input('Enter a string: '))
size = len(str1)
answer = []

while size > 0:
    if size < 3:
        new_arr = str1[0:size]
        size = 0
    else:
        new_arr = str1[0:3]
        size = size - 3
    new_arr = list(new_arr)
    answer.append(new_arr)
    str1 = str1[3:]

print(answer)
