def print_random_stuff(name, age=12, *args, **kwargs) -> None:
    print(name, age)
    print(args)
    print(kwargs)


print_random_stuff(
    "Jonas",
    "Petras",
    "Antanas",
    "Mindaugas",
    random_name="Tomas",
    random_name_2="Tomas",
)


def new_func(a, b, c, d=20, *args, **kwargs) -> None:
    print(a, b, c, d)
    if args:
        # I do whatever I want with args
        # args is a tuple
        print(args)
    if kwargs:
        # I do whatever I want with kwargs
        # kwargs is a dictionary
        print(kwargs)