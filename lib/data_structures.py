import ipdb

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
    name_list = [food["name"] for food in spicy_foods]
    print(name_list)
    return name_list

def get_spiciest_foods(spicy_foods):
    spiciest_foods = [food for food in spicy_foods if food["heat_level"] > 5]
    return spiciest_foods

def print_spicy_foods(spicy_foods):
    for spicy_food in spicy_foods:
        print(f"{spicy_food['name']} ({spicy_food['cuisine']}) | Heat Level: {'🌶' * spicy_food['heat_level']}")

def get_spicy_food_by_cuisine(spicy_foods, cuisine):
    for food in spicy_foods:
        if food['cuisine'] == cuisine:
            return food

def print_spiciest_foods(spicy_foods):
    spiciest_foods_pr = get_spiciest_foods(spicy_foods)
    print_spicy_foods(spiciest_foods_pr)

def get_average_heat_level(spicy_foods):
    heat_levels = [food['heat_level'] for food in spicy_foods]
    average = sum(heat_levels) / len(spicy_foods)
    return average

def create_spicy_food(spicy_foods, spicy_food): 
    spicy_foods.append(spicy_food)
    return spicy_foods
