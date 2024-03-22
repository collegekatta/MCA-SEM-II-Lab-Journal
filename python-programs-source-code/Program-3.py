from functools import reduce

is_even = lambda x: x % 2 == 0

addition = lambda x, y: x + y

def add_even_numbers(numbers):
    even_numbers = filter(is_even, numbers)
    result = reduce(addition, even_numbers)
    return result

# Main function
def main():
    try:
        numbers = list(map(int, input("Enter a list of numbers separated by space: ").split()))
        
        if len(numbers) > 3:
            result = add_even_numbers(numbers)
            print("Sum of even numbers:", result)
        else:
            print("Input list has 3 or fewer numbers.")
    except ValueError:
        print("Please enter valid numbers.")

if __name__ == "__main__":
    main()
