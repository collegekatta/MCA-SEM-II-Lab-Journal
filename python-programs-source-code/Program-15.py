import threading
import time

# Function to print numbers from 1 to 5
def print_numbers():
    for i in range(1, 6):
        print(f"Number: {i}")
        time.sleep(1)

# Function to print letters from 'a' to 'e'
def print_letters():
    for char in 'abcde':
        print(f"Letter: {char}")
        print("Sleeping...")
        time.sleep(1)

# Creating threads for each function
thread1 = threading.Thread(target=print_numbers)
thread2 = threading.Thread(target=print_letters)

thread1.start()
thread2.start()

thread1.join()
thread2.join()

print("Multithreading example is complete.")
