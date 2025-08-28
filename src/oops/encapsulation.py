class Person:
    def __init__(self, name, age):
        ## double underscore defines a private attribute
        self.__name = name ## private attribute
        ## single underscore defines a protected attribute
        self._age = age ## protected attribute

    def get_name(self):
        return self.__name
    
    def set_name(self, name):
        self.__name = name

    def get_age(self):
        return self._age

    def set_age(self, age):
        self._age = age

person = Person("Alice", 30)
print("Attributes of Person:"+str(dir(person)))
print(person.get_name())
print(person.get_age())
person.set_name("Bob")
person.set_age(31)
print(person.get_name())
print(person.get_age())