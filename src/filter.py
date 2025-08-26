def even(number):
    return number % 2 == 0

## Use filter() to filter out even numbers
## This will return a new list with only the even numbers
numbers = [1,2,3,4,5,6]
print(list(filter(even, numbers)))  # Output: [2, 4, 6]

## Use filter() to filter out numbers greater than five
## This uses a lambda function to filter the numbers
numbers=[1,2,3,4,5,6,7,8,9]
greater_than_five=list(filter(lambda x:x>5,numbers))
print(greater_than_five)

## Filter with a lambda function and multiple conditions
numbers=[1,2,3,4,5,6,7,8,9]
even_and_greater_than_five=list(filter(lambda x:x>5 and x%2==0,numbers))
print(even_and_greater_than_five)

## Filter() to check if the age is greate than 25 in dictionaries
people=[
    {'name':'Krish','age':32},
    {'name':'Jack','age':33},
    {'name':'John','age':25}
]

def age_greater_than_25(person):
    return person['age']>25

print(list(filter(age_greater_than_25,people)))