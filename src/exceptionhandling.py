## Exception Handling 
try:
    num = int(input("Enter a number: "))
    result = 10 / num
except ValueError:
    print("That's not a valid number!")
except ZeroDivisionError:
    print("You can't divide by zero!")
except Exception as ex:
    print(ex)
else:
    print(f"The result is {result}")
finally:
    print("Execution complete.")

## File exceptions
try:
    with open('non_existent_file.txt', 'r') as file:
        content = file.read()
except FileNotFoundError:
    print("File not found!")
except Exception as ex:
    print(f"Exception: {ex}")
finally:
    if 'file' in locals() and not file.closed:
        file.close()