class Animal:
    def __init__(self, name):
        self.name = name
    
    def speak(self):
        return f"{self.name} makes a sound."

class Pet: 
    def __init__(self, owner):
        self.owner = owner

    def speak(self):
        return f"{self.owner}'s pet makes a sound."

class Dog(Animal, Pet): ## Dog class inherits from both Animal and Pet
    def __init__(self, name, owner):
        Animal.__init__(self, name)
        Pet.__init__(self, owner)

    def speak(self):
        return f"{self.name} says Woof!"

dog = Dog("Buddy", "Alice")
print(dog.speak())  # Output: Buddy says Woof!