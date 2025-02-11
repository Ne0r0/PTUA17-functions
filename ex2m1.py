# Write a function to filter and sort a list of restaurants based on their ratings. 
# Each restaurant should be represented as a dictionary containing keys for “name” and “rating”. 
# The function should allow the user to specify a minimum rating threshold. If no threshold is specified, the default should be set to 4.0.
# The function should return a list of restaurant names that meet or exceed the rating threshold, sorted alphabetically.

# Functionality:

# Input Handling: Prompt the user to enter the number of restaurants they wish to input. For each restaurant, 
# the user should provide a name and a numerical rating.

# Rating Filter: By default, only include restaurants with a rating of 4.0 or higher unless the user specifies a different minimum.

# Sorting: The output list should be alphabetically sorted by the restaurant name for those that meet the rating criteria.

# User Feedback: Display the filtered and sorted list of restaurant names to the user.

from typing import List, Dict

def filter_and_sort_restaurants() -> None:
    restaurants: List[Dict[str, float]] = []
    
    num_restaurants: int = int(input("Enter the number of restaurants: "))
    
    for _ in range(num_restaurants):
        name: str = input("Enter restaurant name: ")
        rating = float(input("Enter restaurant rating: "))
        restaurants.append({"name": name, "rating": rating})
    
    min_rating_input = input("Now enter the minimum restaurant rating (or leave blank): ")
    min_rating = float(min_rating_input) if min_rating_input else 4.0 #Default value is 4.0, otherwise users input float
    
    filtered_restaurants: List[str] = [entry["name"] for entry in restaurants if entry["rating"] >= min_rating]
    filtered_restaurants.sort()
    
    print(f"Restaurants with a rating above {min_rating}: {filtered_restaurants}")

filter_and_sort_restaurants()
