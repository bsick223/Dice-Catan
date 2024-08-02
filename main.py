import random
from player import Player
from currentPlayers import currentPlayers
# resource_map = {1: 'gold', 2: 'wood', 3: 'brick', 4: 'grain', 5: 'sheep', 6: 'ore'}
# BAR = "***************************************************************"

# To-Do: Gold, wheat
# To-Do: Final roll is the same as 2nd
# To-Do: Show the player stats after building something

# def roll_dice(dice):
#     for i in range(len(dice)):
#         if dice[i] is None:
#             dice[i] = random.randint(1,6)
#     resources = [resource_map[die] for die in dice]
#     return dice, resources


# def allocate_resources(resources, player):
#     for resource in resources:
#         if resource in player.resources:
#             player.resources[resource] += 1

# def check_achievements(players):
#     longest_road_player = None
#     largest_army_player = None

#     for player in players:
#         if player.roads >= 5:
#             if longest_road_player is None or player.roads > longest_road_player.roads:
#                 if longest_road_player:
#                     longest_road_player.has_longest_road = False
#                     longest_road_player.victory_points -= 2
#                 longest_road_player = player
#                 player.has_longest_road = True
#                 player.victory_points += 2
#         if player.knights >= 3:
#             if largest_army_player is None or player.knights > largest_army_player.knights:
#                 if largest_army_player:
#                     largest_army_player.has_largest_army = False
#                     largest_army_player.victory_points -= 2
#                 largest_army_player = player
#                 player.has_largest_army = True
#                 player.victory_points += 2


def main():
    temp = {"Brendan": Player("Brendan"), "Sara": Player("Sara")}
    players = currentPlayers(temp)
    while True:
        if players.playersTurn():
            break
        








if __name__ == "__main__":
    main()
