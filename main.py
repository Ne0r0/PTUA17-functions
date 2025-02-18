# def print_random_stuff(name, age=12, *args, **kwargs) -> None:
#     print(name, age)
#     print(args)
#     print(kwargs)


# print_random_stuff(
#     "Jonas",
#     "Petras",
#     "Antanas",
#     "Mindaugas",
#     random_name="Tomas",
#     random_name_2="Tomas",
# )


# def new_func(a, b, c, d=20, *args, **kwargs) -> None:
#     print(a, b, c, d)
#     if args:
#         # I do whatever I want with args
#         # args is a tuple
#         print(args)
#     if kwargs:
#         # I do whatever I want with kwargs
#         # kwargs is a dictionary
#         print(kwargs)



# def multiply(num_1: int, num_2: int) -> int:
#     return num_1 * num_2


# print(multiply(2, 2))


# multiplication = lambda num_1, num_2: num_1 * num_2

# print(multiplication(2, 7))

# answer = (lambda num_1, num_2: num_1 * num_2)(2, 7)
# print(answer)

# a = 5
# b = 7

# answer = (lambda num_1, num_2: num_1 * num_2)(a, b)
# print(answer)


try:
    print("I am here!")
    print(2 / 0)
except Exception as e:
    print(f"Learn some basic math dude!,because off error: {e}")


try:
    # print("I am here!")
    print(2 / 0)
except ZeroDivisionError:
    print(f"CAN'T DIVIDE BY ZERO!")


try:
    input = int(input("Enter a number: "))
    print(input)
except Exception as e:
    print(f"Error: {e}")