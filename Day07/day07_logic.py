"""
Write robust code that doesn't crash.
Task: Write a function safe_divide(a, b) that divides numbers but handles errors gracefully.

Inputs: (10, 2), (5, 0), ("a", 2)
Constraint: Use try, except ZeroDivisionError, and except TypeError.

"""


try:
    a = int(input("Enter the Value of A: "))
    b = int(input("Enter the Value of B: "))
    print(a/b)
    
except ZeroDivisionError:
    print("Cannot Divide by 0")
    
except ValueError:
    print("Cannot divide integer values with strings")

else:
    print("Successfuly Executed")
    
    