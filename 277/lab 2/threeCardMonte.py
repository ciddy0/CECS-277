import check_input
import random
# Author: Diego Cid, Lela Wondafrash
# Date: 8/31/2023
# Description: Three card monte game, where the user inputs how much money they want to gamble and then has to guess where the queen is. 

def get_users_bet(money):
  """
  Displays to user how much money they currently have and how much they are going to bet
  INPUT:
  - money: int type; the amount of money the user is betting
  """
  
  print(f"You have ${money}.")
  bet  = check_input.get_int_range("How much do you wanna bet? ", 1, money)
  return bet
  


def get_users_choice():
  """
  Displays the cards face down and prompts the user to guess where the Queen is
  """

  print("""
+-----+ +-----+ +-----+
|     | |     | |     |
|  1  | |  2  | |  3  |
|     | |     | |     |
+-----+ +-----+ +-----+
""")
  users_choice  = check_input.get_int_range("Find the queen: ", 1, 3)
  return users_choice


def display_queen_loc(queen_loc):
  """
  displays an image of the cards and reveals wether the user guessed correctly or incorrectly 
  INPUT: 
  - queen_loc: int type; the location of the queen
  """
  if queen_loc == 1:
    print("""
+-----+ +-----+ +-----+
|♕    | |♕    | |♕    |
|  Q  | |  K  | |  K  |
|    ♕| |    ♕| |    ♕|
+-----+ +-----+ +-----+
""")
  elif queen_loc == 2:
    print("""
+-----+ +-----+ +-----+
|♕    | | ♕   | | ♕   |
|  K  | |  Q  | |  K  |
|    ♕| |    ♕| |    ♕|
+-----+ +-----+ +-----+
""")
  else:
    print("""
+-----+ +-----+ +-----+
|♕    | |♕    | |♕    |
|  K  | |  K  | |  Q  |
|    ♕| |    ♕| |    ♕|
+-----+ +-----+ +-----+
""")
  
 



def main():
  
  keep_playing = ""
  money = 100 #initial amount of money 
  print( "Welcome to Three Card Monte")
  
  while money > 0:
    location = random.randint(1, 3) #randomly chooses which of the 3 cards is the queen 
    print("Find the queen to double your bet!")
    
    bet = get_users_bet(money) #calls function to check the users bet money
    users_guess = get_users_choice() #prompts reader to guess the location of the queen
    display_queen_loc(location) #displays the queens location
    
    if users_guess == location: #modifies the users money
      money += bet
      print("Wow you got lucky!")
    else:
      money -= bet
      print("You lose!")
      
    if money <= 0: #user loses game if money reaches zero
      print("You're out of money, try again later loser!")
      break

    #ask the user if they want to keep playing and checks for invalid inputs
    keep_playing = input("Wanna play again? (Y/N): ")
    while keep_playing.upper() not in ("Y", "N"):
      print("Invalid input")
      keep_playing = input("Wanna play again? (Y/N): ")
    if keep_playing.upper() == "Y":
      pass
    else:
      break

    

   
  print("Thanks for playing!")

  
main()
