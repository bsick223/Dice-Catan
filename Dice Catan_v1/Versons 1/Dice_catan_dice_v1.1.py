import random
# Initialize the dice dictionary
dice = {
    "Gold": 1,
    "Ore": 2,
    "Wheat": 3,
    "Sheep": 4,
    "Wood": 5,
    "Brick": 6
}

# Function to get the key by value
def get_key_by_value(d, value, none=None):
    for key, val in d.items():
        if val == value:
            return key
    return none

# Number of rolls
num_rolls = 6

# Generate random values
random_values = [random.choice(list(dice.values())) for _ in range(num_rolls)]

# Get corresponding resources
resources = [get_key_by_value(dice, value) for value in random_values]

# Print the resources
for resource in resources:
    print(resource)