import re

def validate_email(email):
    pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    if re.match(pattern, email):
        return True
    else:
        return False

def validate_password(password):
    # Password must be at least 8 characters long, 
    # contain at least one uppercase letter, 
    # one lowercase letter, 
    # one digit, and one special character
    pattern = r'^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[@$!%*?&])[A-Za-z\d@$!%*?&]{8,}$'
    if re.match(pattern, password):
        return True
    else:
        return False

def validate_mobile_number(mobile_number):
    pattern = r'^\d{10}$'
    if re.match(pattern, mobile_number):
        return True
    else:
        return False

def validate_url(url):
    pattern = r'^(http(s)?://)?(www\.)?[a-zA-Z0-9]+\.[a-zA-Z]{2,}(\.[a-zA-Z]{2,})?$'
    if re.match(pattern, url):
        return True
    else:
        return False

# Test the functions
email = "test@example.com"
password = "password@123"
mobile_number = "1234567890"
url = "https://www.example.com"

print("Email validation:", validate_email(email))
print("Password validation:", validate_password(password))
print("Mobile number validation:", validate_mobile_number(mobile_number))
print("URL validation:", validate_url(url))
