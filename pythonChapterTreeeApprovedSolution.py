# pythonChapterThreeApprovedSolution.py
#
# Programmer Name: Dennis Mohle
# Date: 8/11/23
#
# This python program demonstrates the Python programming concepts in Cengage module (chapter) three.
#
# The "largest of three" program in Python is coded here using one nested if statement, a compound if statement, and
# another solution from ChatGPT

#    int, string, double, and bool variable types were used
#    The primitive data type "str" was demonstrated by getting and displaying user name, outputting the quotient of
#    the first input number by the second input number

#    variable data type was demonstrated with the type() function.
#
print("\n Welcome to the Approved Solution for the Largest of Three program!\n")
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
# done: TODO: Output the types of the variables: result_of_division and play_again.
print("\n The type of result_of_division is: ", str(type(result_of_division)))
print("\n The type of play_again is: ", str(type(play_again)))

# Get three integers from the user.
num1 = input("\n Please enter the first whole (integer) number: ")
print("\n num1 = " + num1)
# done: TODO: get two more ints from the user
num2 = input("\n Please enter the second whole (integer) number: ")
print("\n num2 = " + num2)
num3 = input("\n Please enter the third whole (integer) number: ")
print("\n num3 = " + num3)
# Note that we can concatenate (combine) two strs using the addition operator!

# done: TODO: examine the type of num1, num2, and num3. why/how did the data type change from int to str?
# The variable num1 was initialized as an int, but the input() function returned a str.
# done: TODO: Get the data types of num1, num2, and num3 back to int so you can compare values.
# To do this use the int() function, like this: int(num1).

# Get the user's name.
# done: TODO: get and print() the user's name
user_name = input("Please enter your name: ")
print("Hello " + user_name + " ... Welcome to the largest of three game!")
# Note how spaces are used here. We concatenate strs with the + operator.


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

# done: (see code immediately above) TODO: Code up a nested-if statement solution after making num1, num2, and num3
#    proper data types to work with arithmetic operators

# done: (see code below) TODO: Code up a solution using compound if statements (use the 'and' operator)
# Example compound if statement:
n1 = 4
n2 = 5
n3 = 3
n4 = 4
if (n1 < n2) and (n1 < n3):
    print("\n\n" + str(n1) + " is smallest.")
else:
    print("\n\n" + str(n1) + " is not smallest.")

# done: TODO: Code up a solution from ChatGPT
# Note that chatGPT used the print(f) function, so the numeric-type variable named "largest" could be using inline

# Get user's name
user_name = input("Please enter your name: ")

# Get three integers from the user
num1 = int(input("Enter the first integer: "))
num2 = int(input("Enter the second integer: "))
num3 = int(input("Enter the third integer: "))

# Find the largest number
if num1 >= num2 and num1 >= num3:
    largest = num1
elif num2 >= num1 and num2 >= num3:
    largest = num2
else:
    largest = num3

# Display the result
print(f"Hello, {user_name}! The largest number is: {largest}")