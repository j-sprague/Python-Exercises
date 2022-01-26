# Used W3Schools resource: https://www.w3schools.com/python/python_howto_reverse_string.asp

user_input = input(str('Enter a string: '))[::-1] 
# The [X:Y:Z] slice box at the end of a list allows you to cut a list up from the X position to the Y position of a 
# list, along with a third optional step Z. Setting the Z value to -1 reverses the order of the list (string in this case)

print(user_input)
