def isEven(number):
    """This function is to find even or odd number"""
    if number%2==0:
        return 'Even'
    else:
        return 'Odd'

# This function uses default parameters
# which gets overriden if passed in the function
# Else default value will be considered
def add(a,b=10): 
    return a+b
    
# This function takes in arguments of variable length
# Also called positional arguments
def positional_arguments(*args):
    for number in args:
        print(number)

# This function takes in keywords arguments
def keyword_arguments(**kwargs):
    for key,value in kwargs.items():
        print(f"{key}:{value}")

# Return multiple values from a function
def return_multiplevalues(a=10,b=10):
    return a*b,a,b

print(isEven(10))
print(add(20))
positional_arguments(1,2,3,4,5,"Test String")
keyword_arguments(name="John Doe", age="32", city="Hyderabad")
print(return_multiplevalues())
    