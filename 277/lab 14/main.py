import puppy
import check_input
# Author: Diego Cid, Lela Wondafrash, Sarena Hieng
# Date: 12/07/2023
# Description: Puppy simulation where user can feed or play with the puppy.


def main():
  userChoice = 0
  fido = puppy.Puppy()
  print("Congratulations on your new puppy!")

  #repeatedly ask user to feed or play with puppy until user quits
  while userChoice != 3:
    userChoice = check_input.get_int_range("What would you like to do?\n1. Feed the puppy\n2. Play with the puppy\n3. Quit\n", 1, 3)
    if userChoice == 1:
      print(fido.give_food())
    elif userChoice == 2:
      print(fido.throw_ball())
      

main()