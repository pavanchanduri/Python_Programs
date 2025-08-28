class Error(Exception):
    pass

class InvalidInputError(Error):
    pass

class NotFoundError(Error):
    pass

class PermissionDeniedError(Error):
    pass

try:
    age = int(input("Enter your age: "))
    if age < 0:
        raise InvalidInputError()
except InvalidInputError:
    print("Invalid input: Age cannot be negative.")