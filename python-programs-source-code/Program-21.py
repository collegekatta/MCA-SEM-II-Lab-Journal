import pandas as pd

# Create a list of dictionaries containing student details
students_data = [
    {'student_id': 'S001', 'name': 'John Doe', 'age': 20, 'mobile': '123-456-7890', 'marks': 85},
    {'student_id': 'S002', 'name': 'Jane Smith', 'age': 21, 'mobile': '987-654-3210', 'marks': 90},
    {'student_id': 'S003', 'name': 'Alice Johnson', 'age': 22, 'mobile': '555-555-5555', 'marks': 78},
    {'student_id': 'S004', 'name': 'Bob Brown', 'age': 19, 'mobile': '999-888-7777', 'marks': 95},
    {'student_id': 'S005', 'name': 'Emily Davis', 'age': 20, 'mobile': '333-222-1111', 'marks': 88}
]

# Create a pandas DataFrame from the list of dictionaries
students_df = pd.DataFrame(students_data)

# Display the DataFrame
print("Student Details:")
print(students_df)
