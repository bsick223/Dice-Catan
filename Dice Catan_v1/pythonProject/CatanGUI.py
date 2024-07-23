import tkinter as tk
from tkinter import messagebox
import random


# Define Dice class
class Dice:
    def __init__(self):
        self.faces = ['wool', 'grain', 'brick', 'ore', 'lumber', 'gold']

    def roll(self):
        return random.choice(self.faces)


# Define ResourceDice class
class ResourceDice:
    def __init__(self):
        self.dice = [Dice() for _ in range(6)]
        self.results = []

    def roll_all(self):
        self.results = [die.roll() for die in self.dice]
        return self.results

    def roll_selected(self, selected):
        for i in selected:
            self.results[i] = self.dice[i].roll()
        return self.results


# Define Player class
class Player:
    def __init__(self, name):
        self.name = name
        self.resources = {'wool': 0, 'grain': 0, 'brick': 0, 'ore': 0, 'lumber': 0, 'gold': 0}
        self.points = 0
        self.map = GameMap()

    def update_resources(self, rolled_resources):
        for resource in rolled_resources:
            self.resources[resource] += 1

    def build(self, structure):
        if structure == "road":
            if self.resources['lumber'] >= 1 and self.resources['brick'] >= 1:
                self.resources['lumber'] -= 1
                self.resources['brick'] -= 1
                self.map.build_road()
                self.points += 1
                return True
        elif structure == "settlement":
            if self.resources['lumber'] >= 1 and self.resources['brick'] >= 1 and self.resources['grain'] >= 1 and \
                    self.resources['wool'] >= 1:
                self.resources['lumber'] -= 1
                self.resources['brick'] -= 1
                self.resources['grain'] -= 1
                self.resources['wool'] -= 1
                self.map.build_settlement()
                self.points += 1
                return True
        elif structure == "city":
            if self.resources['ore'] >= 3 and self.resources['grain'] >= 2:
                self.resources['ore'] -= 3
                self.resources['grain'] -= 2
                self.map.build_city()
                self.points += 2
                return True
        elif structure == "knight":
            if self.resources['grain'] >= 1 and self.resources['wool'] >= 1 and self.resources['ore'] >= 1:
                self.resources['grain'] -= 1
                self.resources['wool'] -= 1
                self.resources['ore'] -= 1
                self.map.build_knight()
                self.points += 1
                return True
        return False


# Define GameMap class
class GameMap:
    def __init__(self):
        self.roads = []
        self.settlements = []
        self.cities = []
        self.knights = []

    def build_road(self):
        self.roads.append("Road")
        print("Road built!")

    def build_settlement(self):
        self.settlements.append("Settlement")
        print("Settlement built!")

    def build_city(self):
        self.cities.append("City")
        print("City built!")

    def build_knight(self):
        self.knights.append("Knight")
        print("Knight built!")


# Define CatanGUI class
class CatanGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Dice Catan")

        # Create player and resource dice
        self.player = Player("Player 1")
        self.dice = ResourceDice()

        # Create frames and widgets
        self.create_widgets()

    def create_widgets(self):
        # Dice roll frame
        self.dice_frame = tk.Frame(self.root)
        self.dice_frame.pack(pady=10)

        self.dice_labels = [tk.Label(self.dice_frame, text="Dice " + str(i + 1), font=("Helvetica", 16)) for i in
                            range(6)]
        for label in self.dice_labels:
            label.pack(side=tk.LEFT, padx=5)

        self.roll_button = tk.Button(self.root, text="Roll Dice", command=self.roll_dice)
        self.roll_button.pack(pady=10)

        # Resource display frame
        self.resource_frame = tk.Frame(self.root)
        self.resource_frame.pack(pady=10)

        self.resource_labels = {}
        for resource in self.player.resources:
            frame = tk.Frame(self.resource_frame)
            frame.pack(side=tk.LEFT, padx=10)
            label = tk.Label(frame, text=resource.capitalize(), font=("Helvetica", 16))
            label.pack()
            self.resource_labels[resource] = tk.Label(frame, text=str(self.player.resources[resource]),
                                                      font=("Helvetica", 16))
            self.resource_labels[resource].pack()

        # Building buttons
        self.build_frame = tk.Frame(self.root)
        self.build_frame.pack(pady=10)

        self.build_road_button = tk.Button(self.build_frame, text="Build Road",
                                           command=lambda: self.build_structure("road"))
        self.build_road_button.pack(side=tk.LEFT, padx=5)

        self.build_settlement_button = tk.Button(self.build_frame, text="Build Settlement",
                                                 command=lambda: self.build_structure("settlement"))
        self.build_settlement_button.pack(side=tk.LEFT, padx=5)

        self.build_city_button = tk.Button(self.build_frame, text="Build City",
                                           command=lambda: self.build_structure("city"))
        self.build_city_button.pack(side=tk.LEFT, padx=5)

        self.build_knight_button = tk.Button(self.build_frame, text="Build Knight",
                                             command=lambda: self.build_structure("knight"))
        self.build_knight_button.pack(side=tk.LEFT, padx=5)

        # Score display
        self.score_label = tk.Label(self.root, text="Score: 0", font=("Helvetica", 16))
        self.score_label.pack(pady=10)

    def roll_dice(self):
        results = self.dice.roll_all()
        for i, result in enumerate(results):
            self.dice_labels[i].config(text=result)
        self.player.update_resources(results)
        self.update_resources_display()

    def update_resources_display(self):
        for resource, label in self.resource_labels.items():
            label.config(text=str(self.player.resources[resource]))

    def build_structure(self, structure):
        if self.player.build(structure):
            self.update_score()
        else:
            messagebox.showwarning("Insufficient Resources",
                                   "You don't have enough resources to build a " + structure + ".")

    def update_score(self):
        self.score_label.config(text="Score: " + str(self.player.points))


if __name__ == "__main__":
    root = tk.Tk()
    gui = CatanGUI(root)
    root.mainloop()
