def my_generator():
    for i in range(1,5):
        yield i**2

## Using the Generator
## Example - Squared Values
generator = my_generator()
for value in generator:
    print(value)

## Generators are particularly useful in scenarios where you want to 
# iterate over a potentially large dataset without loading it all into memory at once.
## Example
def read_large_file(file_path):
    with open(file_path, 'r') as file:
        for line in file:
            yield line.strip()
# Usage
for line in read_large_file('src/advanced/large_file.txt'):
    print(line)