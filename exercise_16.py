inputs = []
i = 1
while i < 6:
    user_input = input(f'Enter int #{i}: ')
    try: # Check to see if user_input can be converted to int
        user_input = int(user_input)
        inputs.append(user_input)
        i = i + 1 #Increment i in for loop
    except ValueError:
        print('Error! Input must be a valid integer. Please enter an integer.')

# I didn't do "for i in range(5)" because it would increment regardless of the exception being caught

print(sum(inputs))