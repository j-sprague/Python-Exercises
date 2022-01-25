# Used W3Schools resource: https://www.w3schools.com/python/python_howto_reverse_string.asp

user_input = input(str('Enter a string: '))[::-1] 
# The [X:Y:Z] box at the end of a string allows you to cut a string up from the X position to the Y position of a 
# string, along with a third optional step Z. Setting the Z value to -1 reverses the order of the list (string in this case)

print(user_input)
