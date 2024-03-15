import random
import check_input
# Author: Diego Cid, Lela Wondafrash, Sarena Hieng
# Date: 9/5/2023
# Description: Runs a game of "Ship, Captain, and Crew!", where two players roll 5 dice for numbers 6 (ship), 5 (captain), and 4 (crew) in descending order. If a player rolls these 3 numbers on separate dice, the remaining 2 dice are used to count their points. If a player is unable to get a ship, captain, and crew in 3 rolls, the player gets 0 points. Whoever has the most points wins!

  
  
def roll_dice(dice):
  """
  Randomizes the values of each dice 1-6 and stores the values on descending order
  INPUT:
  - dice: list type; a list of values of dice 1-6
  RETURNS:
  - a list of 6 randomized dice in descending order
  """
  for item in range(len(dice)):
    dice[item] = random.randint(1,6)
  dice.sort()
  dice.reverse()
  return dice 

def display_dice(name, dice):
  """
  Displays the dice values. (Separated by spaces.)
  - name: string type; name of the dice
  - dice: list type; list of the dice
  """
  if len(dice) > 0:
    if name == "roll":
      print("Roll = ", end = "")
    if name == "keep":
      print("Keep = ", end = "")
    if name == "cargo": 
      print("Cargo = ", end = "")
    for item in range(len(dice)):
      print(dice[item], end = " ")
    print("")
  
  
def find_winner(player_points):
  """
  Compares the points of player 1 and player 2 and determines the winner
  INPUT:
  - player_points: list type; a list of player 1 and player 2 points
  """
  print(f"Score: \nPlayer #1: {player_points[0]}\nPlayer #2: {player_points[1]}")
  if player_points[0] > player_points[1]:
    print("Player #1 won!")
  elif player_points[0] < player_points[1]:
    print("Player #2 won!")
  else:
    print("It's a tie!")

def main():

  
  #starts the game
  print("Welcome to ship, captain. and crew! \n")
  score = [0,0]
  keep_playing = ""

  #loops 2 times in order for 2 people to play and resets the lists
  for i in range(2):
    dice = [0, 0, 0, 0, 0]
    keep = []
    cargo = []
    cargoSum = 0
          
    print(f"\nPlayer #{i+1}'s turn: ")

    #loops rolling the dice 3 times unless the user ends their turn
    for j in range(3):
      dice = roll_dice(dice)
      display_dice("roll", dice)
      cargoSum = 0

      #checks if 6,5,4 are in keep list and if not add them to list and remove from dice list
      if 6 in dice and 6 not in keep:
        dice.remove(6)
        keep.append(6)
        print("You got a ship!")
        
      if 5 in dice and 5 not in keep and 6 in keep:
        dice.remove(5)
        keep.append(5)
        print("You got a captain!")
        
      if 4 in dice and 4 not in keep and 5 in keep and 6 in keep:
        dice.remove(4)
        keep.append(4)
        cargo = dice
        print("You got a crew!") 

      display_dice("keep", keep)

      #if cargo list isnt empty then it will display its contents and compute and display the score
      if len(cargo) > 0:
        for points in range(len(cargo)):
          cargoSum += cargo[points]
        score[i] = cargoSum
        display_dice("cargo", cargo)
        print(f"Player #{i+1} points = {cargoSum}")
      
      print("")
      
      #ask user if they want to roll again
      if j < 2:
        keep_playing = check_input.get_yes_no("Roll again? (Y/N): ")
        if keep_playing == False:
          break

  #displays the point of each player and the final winner
  print("")
  find_winner(score)
  
main()