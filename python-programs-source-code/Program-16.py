def create_file(filename):
    try:
        with open(filename, 'w') as file:
            print(f"File '{filename}' created successfully.")
    except IOError as e:
        print(f"Error creating file '{filename}': {e}")

def append_data(filename, data):
    try:
        with open(filename, 'a') as file:
            file.write(data + '\n')
            print("Data appended to the file.")
    except IOError as e:
        print(f"Error appending data to file '{filename}': {e}")

def read_data(filename):
    try:
        with open(filename, 'r') as file:
            print(f"Data from file '{filename}':")
            print(file.read())
    except IOError as e:
        print(f"Error reading file '{filename}': {e}")

# Main function
def main():
    filename = "example_created-in-program-16.txt"

    # Creating a new file
    create_file(filename)
    data_to_append = "This is some appended data."
    append_data(filename, data_to_append)

    read_data(filename)

if __name__ == "__main__":
    main()
