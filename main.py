import random
from player import Player
from currentPlayers import currentPlayers

def main():
    
    number_of_players = input("Please enter the number of players: ")
    while True:
        try:
            number_of_players = int(number_of_players)
            print(f"The number of players entered is: {number_of_players}")
            break
        except ValueError:
            number_of_players = input("Invalid input. Please enter a valid integer: ")
        
    player_names = {}    
    
    for _ in range(number_of_players):
        user = input("Enter Name: ")    
        player_names[user] = Player(user)
    
    # temp = {"Brendan": Player("Brendan"), "Sara": Player("Sara")}
    players = currentPlayers(player_names)
    while True:
        if players.playersTurn():
            break
        








if __name__ == "__main__":
    main()
