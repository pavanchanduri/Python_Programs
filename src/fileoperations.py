with open('src/sample.txt', 'r') as file:
    content = file.read()
    print(content)


with open('src/sample.txt', 'a+') as file:
    file.write('\nAppending new text')

with open('src/sample.txt', 'r') as file:
    lines = file.readlines()

with open('src/sample.txt', 'r') as file:
    lines = file.readlines()
    print(len(lines))
    words = [word for line in lines for word in line.split()]
    print(len(words))
    characters = [char for word in words for char in word]
    print(len(characters))

# Remove the last line i.e., Appending new text
lines = lines[:-1]
print(lines)

with open('src/sample.txt', 'w') as file:
    file.writelines(lines)

# writing to binary files
with open('src/example.bin', 'wb') as file:
    file.write(b'\x00\x01\x02\x03\x04')

with open('src/example.bin', 'rb') as file:
    content = file.read()
    print(content)