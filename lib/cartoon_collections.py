def display_dwarves(names_list):
    for index, name in enumerate(names_list):
        print(f"{index + 1}. {name}")

def summon_captain_planet(elements_list):
    return [element.capitalize() + "!" for element in elements_list]

def has_long_call(calls_list):
    for call in calls_list:
        if len(call) > 4:
            return True
    return False

def find_cheese(strings_list):
    cheeses = ["cheddar", "gouda", "camembert"]
    for word in strings_list:
        if word in cheeses:
            return word
    return None
