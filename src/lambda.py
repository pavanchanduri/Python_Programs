result = lambda x: x * 2
print(result(5))  # Output: 10

is_even = lambda x: x % 2 == 0
print(is_even(4))  # Output: True
print(is_even(5))  # Output: False

add = lambda x, y, z: x + y + z
print(add(1, 2, 3))  # Output: 6

"""
   map takes in a function and a collection
   It applies the function to each item in the collection
   and returns a new collection with the results
"""
numbers = [1, 2, 3, 4, 5]
squared = list(map(lambda x:x**2,numbers))
print(squared)  # Output: [1, 4, 9, 16, 25]