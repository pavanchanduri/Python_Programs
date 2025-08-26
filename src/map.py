numbers1=[1,2,3]
numbers2=[4,5,6]

## Map multiple iterables
## It applies the function to each item in the collection
## and returns a new collection with the results
added_numbers=list(map(lambda x,y:x+y,numbers1,numbers2))
print(added_numbers)

## map() to convert a list of strings to integers
# Use map to convert strings to integers
str_numbers = ['1', '2', '3', '4', '5']
int_numbers = list(map(int, str_numbers))
print(int_numbers)  # Output: [1, 2, 3, 4, 5]

## map() to convert a list of strings to uppercase
## Use map to convert strings to uppercase
words=['apple','banana','cherry']
upper_word=list(map(str.upper,words))
print(upper_word)

## Use map to extract names from a list of dictionaries
## This function takes a dictionary and returns the name
def get_name(person):
    return person['name']

people=[
    {'name':'Krish','age':32},
    {'name':'Jack','age':33}
]
list(map(get_name,people))