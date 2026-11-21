def while_loop():
    val = 1
    while val < 51:
        print("lets have fun")
        val = val + 1

# while_loop()


# Write a Python program to calculate the sum of numbers from 1 to 100 using a while loop.

def sum_Number():
    number = 1
    total = 0

    while number <= 100:
        total = number + total
        number = number + 1

    print("Sum of numbers:", total)

# sum_Number()


# Write a Python program to print the multiplication table of a number entered by the user.

def tabel_number():
    number = int(input("Enter the Number "))
    for i in range(1, 11):
        result = number * i
        print(number, "x", i, "=", result)
# tabel_number()

# Write a Python program to calculate the factorial of a number using a for loop
def factorial_number():
    number = int(input("Enter the Number: "))
    fac = 1

    for i in range(1, number + 1):
        fac = fac * i

    print(fac)  # Outside the for loop

# factorial_number()

# Write a Python program to check whether a number is even or odd.

def find_even_odd():
    number = int(input("enter the number"))
    if number % 2 == 0:
      print("its Even Number")
    else:
      print("its odd Number")
      
# find_even_odd()

# Write a Python program to create a calculator that performs addition, subtraction, multiplication and division based on the user's choice.

def calculator():
    get_number = int(input("Enter the first number: "))
    get_second_number = int(input("Enter the second number: "))

    result = 0

    get_operators = input("Enter the operator (+, -, *, /): ")

    if get_operators == "+":
        result = get_number + get_second_number

    elif get_operators == "-":
        result = get_number - get_second_number

    elif get_operators == "*":
        result = get_number * get_second_number

    elif get_operators == "/":
        if get_second_number != 0:
            result = get_number / get_second_number
        else:
            print("Cannot divide by zero")
            return

    else:
        print("Enter a valid operator")
        return

    print("Result:", result)


# calculator()
