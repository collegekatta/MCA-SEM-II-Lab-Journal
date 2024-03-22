def sum_of_even_numbers(n):
    """Generator function to generate the sum of n even numbers."""
    count = 0
    total_sum = 0
    current_number = 0
    
    while count < n:
        current_number += 2  # Increment by 2 to get the next even number
        total_sum += current_number
        count += 1
        yield total_sum

# Example usage:
n = 5
sum_generator = sum_of_even_numbers(n)

for i, result in enumerate(sum_generator, start=1):
    print(f"Sum of first {i} even numbers:", result)
