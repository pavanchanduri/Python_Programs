class Dog:
    ## Constructor
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def display(self):
        print(f"Name: {self.name}, Age: {self.age}")

dog1 = Dog("Buddy", 5)
dog1.display()