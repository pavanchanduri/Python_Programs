class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __str__(self):
        return f"{self.name} is {self.age} years old"

    def __eq__(self, other):
        if isinstance(other, Person):
            return self.name == other.name and self.age == other.age
        return False

    def __repr__(self):
        return f"Person(name={self.name}, age={self.age})"

    def __len__(self):
        return self.age

    def __getitem__(self, key):
        if key == "name":
            return self.name
        elif key == "age":
            return self.age
        raise KeyError(f"Invalid key: {key}")

person = Person("Alice", 30)
print(person)  # Uses __str__
person2 = Person("Bob", 25)
print(person2)  # Uses __str__
print(person == person2)  # Uses __eq__
print(repr(person))  # Uses __repr__
print(len(person))  # Uses __len__
print(person["name"])  # Uses __getitem__
print(person["age"])  # Uses __getitem__