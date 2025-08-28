## Operator Overloading in Python
## Creating a Vector Class
class Vector:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __add__(self, other):
        if isinstance(other, Vector):
            return Vector(self.x + other.x, self.y + other.y)
        return NotImplemented

    def __sub__(self, other):
        if isinstance(other, Vector):
            return Vector(self.x - other.x, self.y - other.y)
        return NotImplemented

    def __mul__(self, scalar):
        if isinstance(scalar, (int, float)):
            return Vector(self.x * scalar, self.y * scalar)
        return NotImplemented

    ## Division
    ## True Division 
    def __truediv__(self, scalar):
        if isinstance(scalar, (int, float)): ## Check if scalar is a number
            return Vector(self.x / scalar, self.y / scalar) ## True division
        return NotImplemented

    def __repr__(self):
        return f"Vector({self.x}, {self.y})"

    def __eq__(self, other):
        if isinstance(other, Vector):
            return self.x == other.x and self.y == other.y
        return NotImplemented

    def __lt__(self, other):
        if isinstance(other, Vector):
            return (self.x ** 2 + self.y ** 2) < (other.x ** 2 + other.y ** 2)
        return NotImplemented

vector1 = Vector(2, 3)
vector2 = Vector(5, 7)
print("Addition:", vector1 + vector2)
print("Subtraction:", vector1 - vector2)
print("Multiplication:", vector1 * 2)
print("Division:", vector2 / 2)
print("Equality:", vector1 == vector2)
print("Less than:", vector1 < vector2)