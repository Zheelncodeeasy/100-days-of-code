import art

# print logo
print(art.logo)

# Functions for calculator
def add(n1, n2):
    return n1 + n2

def subtract(n1, n2):
    return n1 - n2

def multiply(n1, n2):
    return n1 * n2

def divide(n1, n2):
    return n1 / n2

# storing operations in a dictionary "+", "-", "*", "/" as keys and
# values as the above functions
operations = {
    "+" : add,
    "-" : subtract,
    "*" : multiply,
    "/" : divide
}

# outer loop to ask the input again when the user choice is 'n' or the operation is invalid
while True:
    first_num = float(input("What's the first number?: "))

    # inner loop to perform calculation using previous result when the choice is 'y'
    # inner loop will keep running if the choice is y and perform calculation once when choice is 'n
    while True:
        print(" +\n", "-\n", "*\n", "/\n")
        operation = input("Pick an operation: ")

        # break the loop if user entered invalid option
        if operation not in operations:
            print("Invalid operation, try again")
            print("\n" * 5)
            break

        second_num = float(input("What's the next number? "))

        # performing operations
        perform_calculation = operations[operation]
        result = perform_calculation(first_num, second_num)
        print(f"{str(first_num)} {operation} {str(second_num)} = {result}")

        # ask for user input to continue calculating using previous result or start new calculation
        user_choice = input(f"Type 'y' to continue calculation with {result}, or type 'n' to start a new calculation: ")

        # if user chose y, then we will update the value of first_num to that of result
        # else we will break from inner loop and start taking input from start
        if user_choice == "y":
            first_num = result
        else:
            print("\n" * 50)
            break