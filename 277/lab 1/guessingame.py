
import check_input
import random
# Author: Diego Cid, Lela Wondafrash
# Date: 8/22/2023
# Description: Prompts user to repeatedly guess a randomly generated number between 1 and 100 until they guess the correct number.

def main():
  #declare varaibles and prompt users
  number = random.randint(0, 100)
  count = 1
  
  print("~ Guessing Game ~")
  user_guess = check_input.get_int_range("I’m thinking of a number. Make a  guess (1-100): ", 1, 100)

  #repeat unitl user guess the number right
  while user_guess != number:
    if user_guess < number:
      print("Too low!")
    else:
      print("Too high!")
    count+=1
    user_guess = check_input.get_int_range("Guess again (1-100): ", 1, 100)

  #print results
  print("Correct! you got it in " + str(count) + " tries")

  
main()