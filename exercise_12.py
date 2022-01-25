user_input = input(str('Enter a string: '))
lower = str()
upper = str()

for i in user_input:
    if i.isupper():
        upper += i
    elif i.islower():
        lower += i

ans = str(lower + upper)
print(ans)
