import random

# Define resources (dice) with their values
dice = {"Gold": 1, "Ore": 2, "Wheat": 3, "Sheep": 4, "Wood": 5, "Brick": 6}


# get key by value
def roll_dice(key, value, none=None):
    """ Get the key (resource name) from the dictionary `key` based on `value`. """
    for resource, val in key.items():
        if val == value:
            return resource
    return none  # returns none if value not found


# Get random numbers and put into array
random_values = [random.randint(1, 6) for _ in range(6)]

# Convert the value numbers to call the corresponding resources
resources = [roll_dice(dice, value) for value in random_values]


# Print initial roll
print("Initial Roll:")
for i in range(6):
    print(f"{resources[i]} [{i + 1}]")

# Hold dice based on user input
while True:
    try:
        hold_input = input("Enter the dice numbers (1-6) you want to hold, separated by spaces: ")
        hold_numbers = list(map(int, hold_input.split()))  # Convert input to a list of integers

        # Check if all numbers are between 1 and 6
        if all(1 <= num <= 6 for num in hold_numbers):
            break  # Exit the loop if input is valid
        else:
            print("Please enter numbers between 1 and 6.")
    except ValueError:
        print("Invalid input. Please enter numbers only.")

print("You chose to hold the following dice:", hold_numbers)
# Display the held dice
print("Held Dice:")
for num in hold_numbers:
    print(f"{resources[num - 1]} [{num}]")


# Example of continuing with the held dice
for i in range(6):
    if i + 1 in hold_numbers:
        continue
    else:
        print(f"Rolling dice {i + 1} again: {resources[i]} [{i}]")
















# Make a way to hold them

# hold = input("Which dice would you like to hold? ")
# for i in range(0, dice_value):
# if hold != dice_value:
# continue
# else:
# print(str(dice_value))

# take input as a

# tighten up with a function for rolling
