import numpy as np
import time

# Function to find the sum of elements using a list
def sum_using_list(data):
    total = 0
    for num in data:
        total += num
    return total

# Function to find the sum of elements using a NumPy array
def sum_using_array(data):
    return np.sum(data)

# Convert seconds to hours, minutes, seconds, and milliseconds format
def seconds_to_hms(seconds):
    hours = seconds // 3600
    seconds %= 3600
    minutes = seconds // 60
    seconds %= 60
    milliseconds = (seconds - int(seconds)) * 1000
    seconds = int(seconds)
    return hours, minutes, seconds, milliseconds

# Generate a large collection of numbers (for example purposes)
data = list(range(1000000))
array_data = np.array(data)

# Measure time and space utilization for list
start_time = time.time()
list_sum = sum_using_list(data)
end_time = time.time()
list_time_taken = end_time - start_time
list_hours, list_minutes, list_seconds, list_milliseconds = seconds_to_hms(list_time_taken)
list_space_taken = data.__sizeof__() / 1024  # Convert bytes to kilobytes

# Measure time and space utilization for array
start_time = time.time()
array_sum = sum_using_array(array_data)
end_time = time.time()
array_time_taken = end_time - start_time
array_hours, array_minutes, array_seconds, array_milliseconds = seconds_to_hms(array_time_taken)
array_space_taken = array_data.nbytes / 1024  # Convert bytes to kilobytes

# Display results
print("Using List:")
print("Time taken:", f"{int(list_hours)}hr, {int(list_minutes):02}min, {int(list_seconds):02}sec, {int(list_milliseconds):03}ms")
print("Space taken:", f"{list_space_taken:.2f} KB")
print("Sum:", list_sum)
print()

print("Using NumPy Array:")
print("Time taken:", f"{int(array_hours)}hr, {int(array_minutes):02}min, {int(array_seconds):02}sec, {int(array_milliseconds):03}ms")
print("Space taken:", f"{array_space_taken:.2f} KB")
print("Sum:", array_sum)
