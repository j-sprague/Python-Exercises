s1 = input('Enter a string: ')
s2 = input('Enter another string: ')

if s2.startswith(s1) | s1.startswith(s2):
    print('True')
else:
    print('False')
    