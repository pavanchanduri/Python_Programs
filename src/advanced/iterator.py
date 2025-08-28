### Using an Iterator to Traverse a List
mylist = [1, 2, 3, 4, 5]
iterator = iter(mylist)
try:
    while True:
        item = next(iterator)
        print(item)
except StopIteration:
    print("There are no more elements in the list")