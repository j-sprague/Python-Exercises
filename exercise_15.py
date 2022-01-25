## Worked with Alex Stahlman

def count_letters(user_string):
    letter_count = {}
    for i in user_string.lower():
        if i.isalpha():
            if i in letter_count.keys():
                letter_count[i] += 1
            else:
                letter_count[i] = 1
    return letter_count

user_string = input("Enter a string: ")

print(count_letters(user_string))
