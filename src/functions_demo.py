import re ## Regular expressions module

def convert_temperature(temp, unit):
    if unit.lower() == "c":
        return (temp * 9/5) + 32, "F" ## returns a tuple with (temp, "F")
    elif unit.lower() == "f":
        return (temp - 32) * 5/9, "C" ## returns a tuple with (temp, "C")
    else:
        return None, None ## returns a tuple with (None, None)

print(convert_temperature(100, "C"))
print(convert_temperature(212, "F"))
print(convert_temperature(0, "K"))

def is_strong_password(password):
    """
    Check if the provided password is strong.
    A strong password is defined as:
    - At least 8 characters long
    - Contains at least one digit
    - Contains at least one uppercase letter
    - Contains at least one lowercase letter
    - Does not consist only of alphanumeric characters
    """
    if (len(password) >= 8 and
        any(char.isdigit() for char in password) and
        any(char.isupper() for char in password) and
        any(char.islower() for char in password) and
        not password.isalnum()):
        return True
    return False

print(is_strong_password("Password123!")) 
print(is_strong_password("weakpassword"))
print(is_strong_password("12345678"))
print(is_strong_password("PASSWORD123!"))
print(is_strong_password("Password!"))

## Example cart data
cart=[
    {'name':'Apple','price':0.5,'quantity':4},
    {'name':'Banana','price':0.3,'quantity':6},
    {'name':'Orange','price':0.7,'quantity':3}

]

def calculate_total(cart):
    total = sum(item['price'] * item['quantity'] for item in cart)
    return total

print(f"Total cart value: ${calculate_total(cart):.2f}")

def is_palindrome(s):
    s = s.lower().replace(" ", "") ## Normalize the string
    return s == s[::-1] ## Check if the string is equal to its reverse

print(is_palindrome("A man a plan a canal Panama"))
print(is_palindrome("Was it a car or a cat I saw?"))
print(is_palindrome("No lemon no melon"))
print(is_palindrome("Hello World"))

def fact(n):
    if n == 0:
        return 1
    else:
        return n * fact(n-1)

print(fact(5))  # 120
print(fact(0))  # 1

def get_word_frequency(file):
    word_frequency = {}
    with open(file, 'r') as f:
        text = f.read()
    words = text.lower().split()
    for word in words:
        word = word.strip('.,!?";:()[]{}')
        word_frequency[word] = word_frequency.get(word, 0) + 1
    return word_frequency

print(get_word_frequency('src/sample.txt'))

## Validate Email
def is_valid_email(email):
    pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    if re.match(pattern, email):
        return True
    return False

print(is_valid_email("test@example.com"))
print(is_valid_email("invalid-email"))