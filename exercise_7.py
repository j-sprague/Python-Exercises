has_quit = 0
even_values = []

while has_quit == 0:
    val = input('Enter a number or QUIT to quit: ')
    if val == 'QUIT':
        has_quit = 1
    else:
        val = int(val)
        if val % 2 == 0:
            even_values.append(val)

print(even_values)
