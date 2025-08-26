#### Sets
# Sets are a built-in data type in Python used 
# to store collections of unique items. 
# They are unordered, meaning that the elements do not follow a specific order, 
# and they do not allow duplicate elements. Sets are useful for membership tests, 
# eliminating duplicate entries, and performing mathematical set operations like 
# union, intersection, difference, and symmetric difference.

my_set={1,2,3,4,5}
print(my_set)
print(type(my_set))

# Empty Set
my_empty_set=set()
print(type(my_empty_set))

#set creation using list
my_list = [1,2,3,4,5,6]
my_set=set(my_list)
print(my_set)

## Basics Sets Operation
## Adding and Removing Elements
my_set.add(7)
print(my_set)
my_set.add(7)
print(my_set)

## Remove the elements from a set
# my_set.remove(3)
# print(my_set)
# my_set.remove(10) #throws KeyError

my_set.discard(11)
print(my_set) #No Error even if key is not present

## pop method - removes the first element
removed_element=my_set.pop()
print(f"Popped Element is: {removed_element}")
print(my_set)

## clear all the elements
my_set.clear()
print(my_set)

## Set Memebership test
my_set={1,2,3,4,5}
print(3 in my_set)
print(10 in my_set)

## Mathematical Operation
set1={1,2,3,4,5,6}
set2={4,5,6,7,8,9}

### Union
union_set=set1.union(set2)
print(union_set)

## Intersection
intersection_set=set1.intersection(set2) # Common Elements in set1 and set2
print(intersection_set)

# Updates set1 with the common elements in set1 and set2
set1.intersection_update(set2) 
print(set1)

set1={1,2,3,4,5,6}
set2={4,5,6,7,8,9}

## Difference - Unique elements in set1 only
print(set1.difference(set2))

## Symmetric Difference - Unique elements in set1 and set2 both
print(set1.symmetric_difference(set2))

## Sets Methods
set1={1,2,3,4,5}
set2={3,4,5}

## is subset and superset
print(set1.issubset(set2))
print(set1.issuperset(set2))

# List to Set
lst=[1,2,2,3,4,4,5]
set(lst)

## Set comprehension
squared_set = {x**2 for x in range(10)}
print(squared_set)

### Counting Unique words in text
text="In this tutorial we are discussing about sets"
words=text.split()

## convert list of words to set to get unique words
unique_words=set(words)
print(unique_words)
print(len(unique_words))