class Arithmetic:
    def __init__(self):
        pass

    def add(self, a, b):
        return a + b

class AdvancedArithmetic(Arithmetic):
    def __init__(self):
        super().__init__()

    def add(self, a, b):
        return a + b + 2

class Person:
    def __init__(self, name, age):
        self.__name = name ## private attribute
        self.age = age

advanced_arithmetic = AdvancedArithmetic()
print(advanced_arithmetic.add(5, 10))
person = Person("Alice", 30)
print(dir(person))