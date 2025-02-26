# 4 klases, su atributais, su intsnace metodais (bent 5kiais) ir viskas pratestuota

class House:
    def __init__(self, price: int, age: int, rooms: int, area: float):
        self.price = price
        self.age = age
        self.rooms = rooms
        self.area = area

    def get_price(self):
        return self.price
    
    def is_within_budget(self, budget: int):
        return self.price <= budget
    
    def calculate_price_per_square_meter(self):
        if self.area == 0:
            return 0
        return self.price / self.area
    
    def describe_house(self):
        description = (
            f"This house costs {self.price}€, build in {self.age}, with {self.rooms} rooms, and an area of {self.area} m². "
            f"Prise per square meter: {self.calculate_price_per_square_meter():.2f}€"
        )
        return description
my_house = House(120000, 1987, 3, 64.3)

print(my_house.describe_house())

budget = 150000
if my_house.is_within_budget(budget):
    print(f"You can buy this house with your budget of {budget}€")
else:
    print(f"This house is over yours {budget}€ budget")


class Person:
    def __init__(self, name, age, gender, occupation):
        self.name = name
        self.age = age
        self.gender = gender
        self.occupation = occupation

    def introduce(self):
        return f"Hi, my name is {self.name}. I am a {self.age}-year-old {self.occupation}."

    def celebrate_birthday(self):
        self.age += 1
        return f"Happy Birthday, {self.name}! You are now {self.age} years old."

    def change_occupation(self, new_occupation):
        previous_occupation = self.occupation
        self.occupation = new_occupation
        return f"{self.name} has changed their occupation from {previous_occupation} to {new_occupation}."

    def is_adult(self):
        return self.age >= 18

person1 = Person("Rimas", 33, "Male", "Electrician")

print(person1.introduce())
print(person1.celebrate_birthday())
print(person1.change_occupation("Programmer"))
print(f"Is {person1.name} an adult? {person1.is_adult()}")

