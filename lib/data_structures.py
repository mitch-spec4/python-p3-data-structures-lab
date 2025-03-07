spicy_foods = [
    {
        "name": "Green Curry",
        "cuisine": "Thai",
        "heat_level": 9,
    },
    {
        "name": "Buffalo Wings",
        "cuisine": "American",
        "heat_level": 3,
    },
    {
        "name": "Mapo Tofu",
        "cuisine": "Sichuan",
        "heat_level": 6,
    },
]

def get_names(spicy_foods):
    return [food['name'] for food in spicy_foods]


spicy_foods = [
    {"name": "Green Curry", "cuisine": "Thai", "heat_level": 9},
    {"name": "Buffalo Wings", "cuisine": "American", "heat_level": 3},
    {"name": "Mapo Tofu", "cuisine": "Sichuan", "heat_level": 6}
]

result = get_names(spicy_foods)
print(result)



def get_spiciest_foods(spicy_foods):
        return [food for food in spicy_foods if food["heat_level"] > 5]

result = get_spiciest_foods(spicy_foods)
print(result)



def print_spicy_foods(spicy_foods):
     for food in spicy_foods:
        name = food["name"]
        cuisine = food["cuisine"]
        heat_level = food["heat_level"]
        
        # Create the emoji representation of heat_level
        chili_emoji = "🌶" * heat_level
        
        # Print the formatted spicy food information
        print(f"{name} ({cuisine}) | Heat Level: {chili_emoji}")

print_spicy_foods(spicy_foods)




def get_spicy_food_by_cuisine(spicy_foods, cuisine):
    for food in spicy_foods:
        if food["cuisine"] == cuisine:
            return food
        
result_american = get_spicy_food_by_cuisine(spicy_foods, "American")
print(result_american)


result_thai = get_spicy_food_by_cuisine(spicy_foods, "Thai")
print(result_thai)



def print_spiciest_foods(spicy_foods):
     spiciest_foods = get_spiciest_foods(spicy_foods)
     print_spicy_foods(spiciest_foods)

print_spiciest_foods(spicy_foods)



def get_average_heat_level(spicy_foods):
    if not spicy_foods:
        return 0  # Return 0 if the list is empty to avoid division by zero

    total_heat_level = sum(food["heat_level"] for food in spicy_foods)
    average = total_heat_level / len(spicy_foods)
    return round(average)

result = get_average_heat_level(spicy_foods)
print(result)



def create_spicy_food(spicy_foods, spicy_food):
    spicy_foods.append(spicy_food)
    return spicy_foods
new_spicy_food = {"name": "Mild Chicken", "cuisine": "Canada", "heat_level": 8}

updated_spicy_foods = create_spicy_food(spicy_foods, new_spicy_food)
print(updated_spicy_foods)