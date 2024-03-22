class Employee:
    def __init__(self, emp_id, name, designation, department):
        self.emp_id = emp_id
        self.name = name
        self.designation = designation
        self.department = department

class GrossSalary(Employee):
    def __init__(self, emp_id, name, designation, department, basic_salary, da, hra, ta):
        super().__init__(emp_id, name, designation, department)
        self.basic_salary = basic_salary
        self.da = da
        self.hra = hra
        self.ta = ta
    
    def calculate_gross_salary(self):
        return self.basic_salary + self.da + self.hra + self.ta

class DeductionSalary(GrossSalary):
    def __init__(self, emp_id, name, designation, department, basic_salary, da, hra, ta, income_tax, other_deductions):
        super().__init__(emp_id, name, designation, department, basic_salary, da, hra, ta)
        self.income_tax = income_tax
        self.other_deductions = other_deductions
    
    def calculate_deductions(self):
        return self.income_tax + self.other_deductions

class NetSalary(DeductionSalary):
    def __init__(self, emp_id, name, designation, department, basic_salary, da, hra, ta, income_tax, other_deductions):
        super().__init__(emp_id, name, designation, department, basic_salary, da, hra, ta, income_tax, other_deductions)
    
    def calculate_net_salary(self):
        gross_salary = self.calculate_gross_salary()
        deductions = self.calculate_deductions()
        return gross_salary - deductions

# Example usage:
emp_id = 101
name = "John Doe"
designation = "Software Engineer"
department = "Engineering"
basic_salary = 50000
da = 0.1 * basic_salary
hra = 0.2 * basic_salary
ta = 0.05 * basic_salary
income_tax = 0.15 * basic_salary
other_deductions = 2000

employee = NetSalary(emp_id, name, designation, department, basic_salary, da, hra, ta, income_tax, other_deductions)
net_salary = employee.calculate_net_salary()

print(f"Employee ID: {employee.emp_id}")
print(f"Name: {employee.name}")
print(f"Designation: {employee.designation}")
print(f"Department: {employee.department}")
print(f"Net Salary: ${net_salary:.2f}")
