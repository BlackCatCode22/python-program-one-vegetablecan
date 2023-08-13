# pythonChapterThree.py
#
# Programmer Name: Donald Cao
# Date: 08/13/2023
#
# Demonstrate the Python programming concepts in Cengage module (chapter) three by...
#
# Writing the "largest of three" program in Python using one nested if statement, a compound if statement, and
# another solution from ChatGPT
#    use int, string, double, and bool variable types
#    demonstrate primitive variable usage by getting and displaying user name, outputting the quotient of the first
#    input number by the second input number
#    display, print(), the types of all variables used in the program
#
print("\n Welcome to the Largest of Three program!\n")
#
# Variable Declaration Section
#
# int variables:
num1 = 0
num2 = 0
num3 = 0
largest_num = 0

# string variables:
user_name = ""

# double variables
result_of_division = 0.0

# bool variables
play_again = False

print("\n num1 is of type: " + str(type(num1)))
print("\n user_name is of type: " + str(type(user_name)))
# TODO: Output the types of the variables: result_of_division and play_again.
print("\n The type of result_of_division is: ", str(type(result_of_division)))
print("\n The type of play_again is: ", str(type(play_again)))

# Get three integers from the user.
num1 = input("\n Please enter the first whole (integer) number: ")
print("\n num1 = " + num1)
# TODO: get two more ints from the user
num2 = input(("\n Please enter the second whole (integer) number: "))
print("\n num2 = " + num2)
num3 = input(("\n Please enter the third whole (integer) number: "))
print("\n num3 = " + num3)

# TODO: examine the type of num1, num2, and num3. why/how did the data type change from int to str?
print(type(num1))
print(type(num2))
print(type(num3))

#The variable from num1 is a str because input() function returns it as str while eval() returns int.

# TODO: Get the data types of num1, num2, and num3 back to int so you can compare values.
int(num1)
int(num2)
int(num3)

# Get the user's name.
userName=input("Enter your name: ")
# TODO: get and print() the user's name
print("Hello, userName")


a_num1 = 11
a_num2 = 44
a_num3 = 22

# Example solution using a nested if statement
if (a_num1 > a_num2):
    if (a_num1 > a_num3):
        largest_num = a_num1
    else:
        largest_num = a_num3
else:
    if (a_num2 > a_num3):
        largest_num = a_num2
    else:
        largest_num = a_num3

print("\n\n Largest of three is: " + str(largest_num))

# TODO: Code up a nested-if statement solution after making num1, num2, and num3 proper data types to work
# with arithmetic operators
#Below is mine - Donald Cao
if (num1 > num2):
    if (num1 > num3):
        largest_num = num1
    else:
        largest_num = num3
else:
    if (num2 > num3):
        largest_num = num2
    else:
        largest_num = num3
print(f"\n\nLargest of the three is: {largest_num}")

# TODO: Code up a solution using compound if statements (use the 'and' operator)
# Example compound if statement:
n1 = 4
n2 = 5
n3 = 3
n4 = 4
if (n1 < n2) and (n1 < n3):
    print("\n\n" + str(n1) + " is smallest.")
else:
    print("\n\n" + str(n1) + " is not smallest.")

# TODO: Code up a solution from ChatGPT
# Get user inputs
user_name = input("Enter your name: ")
num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))

# Perform division operation
quotient = num1 / num2

# Display user name and quotient
print("Hello, " + user_name + "!")
print("The quotient of", num1, "divided by", num2, "is:", quotient)

# Display variable types
print("Variable Types:")
print("user_name:", type(user_name))
print("num1:", type(num1))
print("num2:", type(num2))
print("quotient:", type(quotient))
