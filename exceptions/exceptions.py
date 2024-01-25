"""
In Python, exceptions are used to handle errors and exceptional situations that may
occur during the execution of a program. Exception handling allows you to gracefully
handle errors and control the flow of your program when an exception is raised. To
handle exceptions in Python, you can use a combination of the try, except, else, and
finally blocks.

"""

try: 
    numerator = 10
    denominator = 2
    result = numerator / denominator
    print("Result",  result)

except ZeroDivisionError:
    print("ERROR: Division by zero")

else:
    print("No exception ocurred")

finally:
    print("cleanup operations")


"""
Here's a breakdown of the different parts of exception handling:
1. try: The try block is where you put the code that may raise an exception. If an
exception occurs within this block, the execution jumps to the appropriate except
block.
2. except: The except block catches specific exceptions and provides the handling
code for each exception type. You can have multiple except blocks to handle
different types of exceptions.
3. else: The else block is optional and is executed if no exception occurs in the try
block.
4. finally: The finally block is optional and is always executed, regardless of
whether an exception occurred or not.
"""