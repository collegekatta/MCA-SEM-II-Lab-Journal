import pandas as pd

# 1. Create a DataFrame 'student' with fields
student_data = {
    'student_id': ['S001', 'S002', 'S003', 'S004', 'S005'],
    'name': ['John Doe', 'Jane Smith', 'Alice Johnson', 'Bob Brown', 'Emily Davis'],
    'class': ['X', 'X', 'XI', 'XI', 'X'],
    'sub1': [85, 90, 78, 95, 88],
    'sub2': [75, 80, 85, 90, 82],
    'sub3': [70, 75, 80, 85, 78],
    'sub4': [80, 85, 90, 95, 90],
    'sub5': [90, 95, 88, 92, 85],
    'practical': [90, 88, 92, 85, 80],
    'project': [95, 90, 85, 88, 75]
}

student_df = pd.DataFrame(student_data)

# Display the DataFrame
print("Original DataFrame:")
print(student_df)
print()

# 2. Convert DataFrame into CSV file
student_df.to_csv('students-program-22.csv', index=False)
print("DataFrame converted to CSV file: students-program-22.csv")

# 3. Load created CSV file
loaded_df = pd.read_csv('students-program-22.csv')
print("\nLoaded DataFrame from CSV file:")
print(loaded_df)
print()

# 4. Calculate total marks and add new column using lambda function
loaded_df['total'] = loaded_df.apply(lambda row: sum(row[3:]), axis=1)

print("DataFrame with total marks column added:")
print(loaded_df)
print()

# 5. Calculate percentage
loaded_df['percentage'] = (loaded_df['total'] / 500) * 100

print("DataFrame with percentage calculated:")
print(loaded_df)
print()

# 6. Fetch the students having percentage greater than equal to 70
result_df = loaded_df[loaded_df['percentage'] >= 70]

print("Students with percentage greater than equal to 70:")
print(result_df)
