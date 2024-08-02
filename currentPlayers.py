import random

resource_map = {1: 'gold', 2: 'wood', 3: 'brick', 4: 'grain', 5: 'sheep', 6: 'ore'}
def roll_dice(dice):
    for i in range(len(dice)):
        if dice[i] is None:
            dice[i] = random.randint(1,6)
    resources = [resource_map[die] for die in dice]
    return dice, resources


def allocate_resources(resources, player):
    for resource in resources:
        if resource in player.resources:
            player.resources[resource] += 1

class currentPlayers:
    def __init__(self,players):
        self.players = players
        self.longestRoad = None
        self.largestArmy = None
    
    def checkLongestRoad(self,player):
        if player.roads >=5:
            if self.longestRoad == None:
                print(f"{player.name} has the longest road")
                self.longestRoad = player
                self.players[player.name].victory_points += 2
            if  player.roads > self.longestRoad.roads:
                print(f"{player.name} has the longest road")
                self.players[self.longestRoad.name].victory_points -= 2
                self.longestRoad = player
                self.players[player.name].victory_points += 2
                
    def playersTurn(self):
        BAR = "***************************************************************"
        print(self.players)
        for key in self.players:
            player = self.players[key]
            print(f"{player.name}'s turn:")

            dice = [None] * 6
            for roll_number in range(3):
                dice, resources = roll_dice(dice)
                if roll_number < 2:
                    print(f"Roll {roll_number + 1}: {resources}")
                else:
                    print(f"Final Roll: {resources}")

                # pick the dice to hold
                if roll_number < 2:
                    #hold_input: = input("Select which dice you want to hold: ")
                    hold_input = input("Enter the dice positions to hold (ex. '1 3 5') or press Enter to roll all: ")

                    if hold_input.strip():
                        hold_positions = list(map(int, hold_input.split()))
                        for i in range(len(dice)):
                            if i + 1 not in hold_positions:
                                dice[i] = None
                    else:
                        dice = [None] * 6  # if no input, roll all dice

                    print(BAR)


            allocate_resources(resources, player)
            print(player)
            print(BAR)
            print(BAR)
            print(BAR)

            print(f"Resources after final roll: {player.resources}")

            while True:

                action = input("Choose action (build_settlement, build_city, build_road, build_knight, pass)")
                if action == 'build_settlement':
                    if player.build_settlement():
                        print("Settlement built!")
                    else:
                        print("Not enough resources!")
                elif action == 'build_city':
                    if player.build_city():
                        print("City Built!")
                    else:
                        print("Not enough resources!")
                elif action == 'build_road':
                    if player.build_road():
                        print("Road Built")
                    else:
                        print("Not enough resources!")
                elif action == 'build_knight':
                    if player.build_knight():
                        print("Got Knight!")
                    else:
                        print("Not enough resources!")
                elif action == ('pass'):
                    break
                else:
                    print("Invalid action. Try again.")

                print(f"Remaining resources: {player.resources}")

            player.reset_resources()
            print(f"Victory points: {player.victory_points}")
            print(f"Roads built: {player.roads}")
            print(f"Settlements built: {player.settlements}")
            print(f"Cities built: {player.cities}")
            print(f"Knights: {player.knights}")
            
            if player.victory_points >= 10:
                print(f"{player.name} wins!")
                return True
            
        return False
        
                