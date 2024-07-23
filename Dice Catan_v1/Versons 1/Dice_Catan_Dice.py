import random
"""
Dice for the catan

1) assign the element variables using a dictionary(key, value)
    a) {Gold: 0, Ore: 1, Wheat: 2}
"""

dice = {"Gold": 1, "Ore": 2, "Wheat": 3, "Sheep": 4, "Wood": 5, "Brick": 6}

def get_key_by_value(d, value, none=None):
    for resource, val in d.items():
        if val == value:
            return resource
    return none # returns none if value not found

"""
random_value = [0, 2, 3, 4, 5, 6]

for i in range(1, 5):
    random_value[i] = random.choice(list(dice.values()))
    print(random_value[i])
"""
# num_rolls = 6
# rolled_values = [random.choice(list(dice.values())) for _ in range(num_rolls)]

random_value1 = random.choice(list(dice.values()))
random_value2 = random.choice(list(dice.values()))
random_value3 = random.choice(list(dice.values()))
random_value4 = random.choice(list(dice.values()))
random_value5 = random.choice(list(dice.values()))
random_value6 = random.choice(list(dice.values()))



resource1 = get_key_by_value(dice, random_value1)
resource2 = get_key_by_value(dice, random_value2)
resource3 = get_key_by_value(dice, random_value3)
resource4 = get_key_by_value(dice, random_value4)
resource5 = get_key_by_value(dice, random_value5)
resource6 = get_key_by_value(dice, random_value6)


print(resource1)
print(resource2)
print(resource3)
print(resource4)
print(resource5)
print(resource6)

# Make a way to hold them
# tighten up with a function for rolling
# make holding the dice with holding their value from the dictionary.
