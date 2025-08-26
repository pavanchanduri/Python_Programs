## Creating Dictionaries
empty_dict={}
print(type(empty_dict))

empty_dict=dict()
empty_dict
print(empty_dict)

# Declaration of Dictionary
student={"name":"Krish","age":32,"grade":24}
print(student)
print(type(student))

# Single key is always used
student={"name":"Krish","age":32,"name":24}
print(student)

## accessing Dictionary Elements
student={"name":"Krish","age":32,"grade":'A'}
print(student)
print(student['age']) # accessing with key

## Accessing Dictionary elements
print(student['grade'])
print(student['age'])

## Accessing using get() method
print(student.get('grade'))
print(student.get('last_name'))
print(student.get('last_name',"Not Available"))

## Modifying Dictionary Elements
## Dictionary are mutable,so you can add, update or delete elements
print(student)

student["age"]=33  ##update value for the key
print(student)
student["address"]="India" ## added a new key and value
print(student)

del student['grade'] ## delete key and value pair
print(student)

# del student
# print(student) # Not defined exception

## Dictionary methods

keys=student.keys() ##get all the keys
print(keys)
values=student.values() ##get all values
print(values)

items=student.items() ##get all key value pairs
print(items)

### Iterating Over Dictionaries
## You can use loops to iterate over dictionatries, keys,values,or items

## Iterating over keys
for keys in student.keys():
    print(keys)

## Iterating using items
for key,value in student.items():
    print(f"item:({key} , {value})")

## This copies reference of the dictionary
## So changes made to one will reflect in the other
student1 = student
print(student1)
student1["name"]="John"
print(student1)
print(student)

## This copies contents of the dictionary
## So changes made to one will not reflect in the other
## Only student1 dictionary is affected
student1 = student.copy()
print(student1)
student1["name"]="Krish" 
print(student1)
print(student)

## Nested Disctionaries
students={
    "student1":{"name":"Krish","age":32},
    "student2":{"name":"Peter","age":35}
}
print(students)

## Access nested dictionaries elements
print(students["student2"]["name"])
print(students["student2"]["age"])

## Dictionary Comprehension
squares={x:x**2 for x in range(5)}
print(squares)

## Condition dictionary comprehension
evens={x:x**2 for x in range(10) if x%2==0}
print(evens)

## Dictionary to count the frequency of elements
nums = [1,2,2,3,3,3,4,4,4,4,5,5,6]
freq = {}
for n in nums:
    freq[n] = freq.get(n,0) + 1 ## freq.get(n,0) -> 0 if n is not found
print(freq)

## Merge two dictionaries in to one
dict1 = {"a": 1, "b": 2}
dict2 = {"b": 3, "c": 4}
merged_dict = {**dict1, **dict2}
print(merged_dict)