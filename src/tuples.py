## creating a tuple
empty_tuple=()
print(empty_tuple)
print(type(empty_tuple))

## creating a tuple from a list
numbers=tuple([1,2,3,4,5,6,1])
print(numbers)

## creating a list from a tuple
list_from_tuple = list((1,2,3,4,5,6))
print(list_from_tuple)

## creating a mixed tuple
mixed_tuple=(1,"Hello World",3.14, True)
print(mixed_tuple)

## accessing elements in a tuple
print(numbers[2])
print(numbers[-1])
print(mixed_tuple[1:3])
print(numbers[::-1])

## Tuple Operations
concatenation_tuple=numbers + mixed_tuple
print(concatenation_tuple)
print(mixed_tuple * 3)

## Immutable Nature Of Tuples
## Tuples are immutable, meaning their elements cannot be changed once assigned.
# numbers[1] = 10 ## Throws an exception saying 'tuple' object does not support item assignment
# print(numbers)

## Tuple Methods
print(numbers.count(1))
print(numbers.index(3))

## Packing and Unpacking tuple
## packing
packed_tuple=1,"Hello",3.14
print(packed_tuple)

## unpacking
a,b,c=packed_tuple
print(a)
print(b)
print(c)

## Unpacking with *
numbers=(1,2,3,4,5,6)
first,*middle,last=numbers ## Unpacking with *
print(first)
print(middle)
print(last)

## Nested Tuple
## Nested List
lst=[[1,2,3,4],[6,7,8,9],[1,"Hello",3.14,"c"]]
print(lst[0][0:3])

## List of lists and tuples
lst=[[1,2,3,4],[6,7,8,9],(1,"Hello",3.14,"c")]
print(lst[2][0:3])

nested_tuple = ((1, 2, 3), ("a", "b", "c"), (True, False))

## access the elements inside a tuple
print(nested_tuple[0])
print(nested_tuple[1][2])

## iterating over nested tuples
for sub_tuple in nested_tuple:
    for item in sub_tuple:
        print(item,end=" ")
    print()