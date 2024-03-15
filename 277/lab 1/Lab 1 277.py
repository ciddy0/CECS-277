import check_input
import random


# Author: Lela Wondafr
# Date:
# Description: Displays
def main():
  number = random.randint(0, 101)
  count = 1

  print("~ Guessing Game ~")

  user_guess = check_input.get_int_range("Guess a number: ", 0, 100)
  while user_guess != number:
    if user_guess < number:
      print("Too low! Try again")
    else:
      print("Too high! Try again")
    count += 1
    user_guess = check_input.get_int_range("Guess a number: ", 0, 100)

  print("Correct! you got it in " + str(count) + " tries")


main()