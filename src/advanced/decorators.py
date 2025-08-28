def main_method():
    print("This is the main method.")
    msg = "Hello from the inner method!"
    def inner_method():
        ## The inner method can access variables from the outer method
        ## But the inner method cannot be accessed outside
        ## scope of the sub method is within the main method
        print("This is the inner method.")
        print(msg)
    inner_method()
    print("Exiting the main method.")

main_method()

### Decorator
def my_decorator(func):
    def wrapper():
        print("Before the function call")
        func()
        print("After the function call")
    return wrapper

@my_decorator
def say_hello():
    print("Hello!")

say_hello()

## Decorator with arguments
def repeat(num_times):
    def decorator_repeat(func):
        def wrapper(*args, **kwargs):
            for _ in range(num_times):
                func(*args, **kwargs)
        return wrapper
    return decorator_repeat

@repeat(num_times=3)
def say_hello():
    print("Hello!")

say_hello()