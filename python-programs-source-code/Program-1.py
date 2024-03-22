def check_number():
    num = float(input("Enter a number: "))
    if num > 0:
        print("\nOutput : Positive number")
    elif num == 0:
        print("\nOutput : Zero")
    else:
        print("\nOutput : Negative number")

def factorial():
    num = int(input("Enter a number to find its factorial: "))
    factorial = 1
    if num < 0:
        print("\nOutput : Factorial does not exist for negative numbers")
    elif num == 0:
        print("\nOutput : Factorial of 0 is 1")
    else:
        for i in range(1, num + 1):
            factorial *= i
        print("\nOutput : Factorial of", num, "is", factorial)

def fibonacci():
    n = int(input("Enter the number of terms: "))
    a, b = 0, 1
    count = 0
    if n <= 0:
        print("Please enter a positive integer")
    elif n == 1:
        print("\nOutput : Fibonacci sequence up to", n, ":")
        print(a)
    else:
        print("\nOutput : Fibonacci sequence:")
        while count < n:
            print(a, end=" ")
            nth = a + b
            a = b
            b = nth
            count += 1

def multiplication_table():
    num = int(input("Enter the number for which you want to print the multiplication table: "))
    print("\nOutput : Multiplication table of", num)
    for i in range(1, 11):
        print("", num, "x", i, "=", num * i)

def is_armstrong_number(num):
    order = len(str(num))
    sum = 0
    temp = num
    while temp > 0:
        digit = temp % 10
        sum += digit ** order
        temp //= 10
    return num == sum

def check_armstrong_number():
    num = int(input("Enter a number to check if it's an Armstrong number: "))
    if is_armstrong_number(num):
        print("\nOutput : ", num, "is an Armstrong number")
    else:
        print("\nOutput : ", num, "is not an Armstrong number")

# Main program
while True:
    print("\nChoose an option:")
    print("1. Check if a number is Positive, Negative or Zero")
    print("2. Find Factorial of a Number")
    print("3. Print the Fibonacci sequence")
    print("4. Print Multiplication Table")
    print("5. Check Armstrong Number")
    print("6. Exit")
    choice = input("Enter your choice (1-6): ")

    if choice == '1':
        check_number()
    elif choice == '2':
        factorial()
    elif choice == '3':
        fibonacci()
    elif choice == '4':
        multiplication_table()
    elif choice == '5':
        check_armstrong_number()
    elif choice == '6':
        print("Exiting the program...")
        break
    else:
        print("Invalid choice. Please enter a number between 1 and 6.")
