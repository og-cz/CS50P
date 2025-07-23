# Define a function called 'sum' that takes two parameters a and b
# It returns the sum of a and b
def sum(a, b):
    return a + b 

# Call the sum function with arguments 1 and 1
# Then print the returned result (which is 2)
print(sum(1, 1))

# Define a function called 'square' that takes one parameter 'number'
# It returns the square of that number (number * number)
def square(number):
    return number * number

# Define the main function
def main():
    # Ask the user to input a number
    # Convert the input from string to integer
    number = int(input("give a number to square: "))
    
    # Call the square function with the input number
    # Return the result back to whoever calls main()
    return square(number)

# Call the main function and print its returned value
print(main())
