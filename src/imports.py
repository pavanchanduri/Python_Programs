import math
import sys
import keyword
import random
import os
from datetime import datetime, timedelta
import json
import re

## Custom package
from package.mathoperations import add, subtract, multiply, divide

print(math.sqrt(16));
print(math.factorial(5));
print(math.degrees(math.pi));
print(sys.version);
print(keyword.kwlist); ## List of all keywords in Python

print(add(5, 10))
print(subtract(5, 10))
print(multiply(5, 10))
print(divide(5, 10))
print(divide(5, 0))

print(random.randint(1, 100))  # Random integer between 1 and 100

print(os.getcwd())  # Current working directory
if not os.path.exists('test_directory'):
    os.mkdir('test_directory')  # Create a new directory
    file = open('test_directory/test_file.txt', 'w')
    file.write('Hello, World!')
    file.close()
if os.path.exists('test_directory/test_file.txt'):
    os.remove('test_directory/test_file.txt')  # Remove the file
print(os.listdir('.'))  # List files and directories in the current directory
os.rmdir('test_directory')  # Remove the directory


print(datetime.now().timestamp())  # Current timestamp
print(datetime.now())
print(datetime.now() + timedelta(days=1))  # Current time + 1 day

## Data Serialization

data = {
    'name': 'John',
    'age': 30,
    'city': 'New York'
}

# Serialize to JSON (Python object -> JSON string)
json_string = json.dumps(data)
print(json_string)
print(type(json_string))

# Deserialize back to Python object (JSON string -> Python object)
data = json.loads(json_string)
print(data)
print(type(data))

pattern = r'\d+'
text = 'There are 123 apples'
matches = re.search(pattern, text)
print(matches.group())  # Output: 123