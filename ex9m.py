# TypeError, ValueError, KeyError, IndexError, AttributeError?, ir dar trys papildomi liko (NameError, )

import logging
import math

logging.basicConfig(
    filename="Handling_errors.log",
    level=logging.DEBUG,
    format="%(asctime)s - %(levelname)s - %(message)s",
    datefmt="%Y-%m-%d %H:%M:%S",
)

def adding_numbers(number_three: int, number_four: int) -> int:
    try:
        result_two = number_three + number_four
        return result_two
    except TypeError:
        logging.error(f"Used letter not a number {TypeError}")
        return "You need to put two numbers"
print(adding_numbers(20, "a"))

def my_basket(apple: str, pear: str, coconut: str) -> list:
    basket = [apple, pear, coconut]
    try:
        return basket[4]
    except IndexError:
        logging.error(f"Searching something else in the list {IndexError}")
        return "There is no more items"
print(my_basket("apple","pear", "coconut"))

def my_friends(Rimas: str, Antanas: str, Jevgenijus: str) -> dict:
    friends = {"Rimas" : Rimas, "Antanas" : Antanas, "Jevgenijus" : Jevgenijus}
    try:
        return friends["Vaidas"]
    except KeyError:
        logging.error(f"There are only three friends {KeyError}")
        return "There are only three friends"
print(my_friends("Rimas", "Antanas", "Jevgenijus"))

def sqrt_number():
    try:
        return math.sqrt(-1)
    except ValueError:
        logging.error(f"ValueError occurred: {ValueError}")
        return "YOU CAN'T SQUARE ROOT THIS NUMBER"
print(sqrt_number())

def handle_name_error():
    try:
        geek = input("Enter something: ")
        printf(geek)
    except NameError:
        logging.error("There is some problem with the code")
        print("Caught a NameError! Did you mean 'print' instead of 'printf'?")
handle_name_error()
