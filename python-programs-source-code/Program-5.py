from helpers import logical_operations

# Perform logical operations
result_and = logical_operations.logical_and(True, False)
result_or = logical_operations.logical_or(True, False)
result_not = logical_operations.logical_not(True)

# Display results
print("""Perform logical AND operation.""")
print("Logical AND:", result_and, "\n")
print("""Perform logical OR operation.""")
print("Logical OR:", result_or, "\n")
print("""Perform logical NOT operation.""")
print("Logical NOT:", result_not, "\n")
