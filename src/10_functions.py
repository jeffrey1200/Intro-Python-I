# Write a function is_even that will return true if the passed-in number is even.

# YOUR CODE HERE


def isEven(number):
    if number % 2 == 0:
        return True
    else:
        return False


# Read a number from the keyboard
num = input("Enter a number: ")
num = int(num)

# Print out "Even!" if the number is even. Otherwise print "Odd"

# YOUR CODE HEREsd
if isEven(num):
    print("Even!")
else:
    print("Odd")

