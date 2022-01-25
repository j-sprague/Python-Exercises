num1 = int(input('Enter a number : '))
num2 = int(1)
num_list = []
sum = float(0)

while num1 >= num2:
    temp = float(input(f'Enter value number {num2} : '))
    num_list.append(temp)
    sum = sum + temp
    num2 = num2 + 1

mean = sum / num1

print(f'List: {num_list}')
print(f'Average: {mean}')
