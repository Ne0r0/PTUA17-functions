# In Python, dividing by zero raises a ZeroDivisionError. Your task is to create a function safe_divide() that:
# Takes two numbers as arguments.
# Tries to divide the first number by the second number.
# If the second number is 0, it should catch the ZeroDivisionError and return a custom error message.
# If at least one of the inputs is not a number, it should catch the TypeError and return a custom error message.
# If no exceptions occurred, it should print a message Division was successful (using the else clause).
# Regardless of whether the division is successful or not, it should print a message Attempted division.
# If the division is successful, it should return the result (either in the else clause or at the very end of the function).

import logging
from typing import Optional

logging.basicConfig(
    filename="safe_divide.log",
    level=logging.DEBUG,
    format="%(asctime)s - %(levelname)s - %(message)s",
    datefmt="%Y-%m-%d %H:%M:%S",
)

def safe_divide(num1: Optional[int], num2: Optional[int] ) -> float:
    try:
        result = num1 / num2
        return result
    except ZeroDivisionError as e:
        logging.error(f"User divided by 0 {e}")
        print(f"You can't do math")
    except TypeError as e:
        logging.error(f"User used letters not a number: {e}")
        print(f"Don't use letters, you dumb!!")

    
print(safe_divide(20, 0))

print(safe_divide(10, "2"))

print(safe_divide(8, 4))