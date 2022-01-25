# Worked on with Alex Stahlman

row = int(input('Enter a row number from 1 to 5: ')) - 1
col = int(input('Enter a column number from 1 to 5: ')) - 1

for i in range (5):
    for h in range (5):
        if i == row and h == col:
            print('1',end=' ')
        else:
            print('0',end=' ')
    print('')
