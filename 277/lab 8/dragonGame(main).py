import check_input
from random import randint
import hero
import dragon
import firedragon
import flyingdragon

# Author: Diego Cid, Lela Wondafrash, Sarena Hieng
# Date: 10/12/2023
# Description: A dragon game where the player must defeat 3 dragons to win, after each turn a random dragon will attack back. If the player defeats all three dragons before they run out of HP they win, otherwise, the dragons win. :D


def attack_move(p, drag):
  """
  displays the players attack move onto the dragon
  the object: the player, other: the dragon
  """
  weapon = check_input.get_int_range(
    "\nAttack with: \n1. Sword (2 D6)\n2. Arrow (1 D12)\nEnter weapon: \n", 1,
    2)
  if weapon == 1:
    print("\n" + p.basic_attack(drag))
  if weapon == 2:
    print("\n" + p.special_attack(drag))


def main():
  regDragon = dragon.Dragon("Bob", 15)
  pyroDragon = firedragon.FireDragon("Firey", 20, 5)
  windDragon = flyingdragon.FlyingDragon("Spirit Airlines", 25, 3)
  lizardList = [regDragon, pyroDragon, windDragon]

  name = input("What is your name, challenger? \n")
  player = hero.Hero(name, 50)
  print(f"\nWelcome to dragon training {name}\nYou must defeat 3 dragons.\n")

  while len(
      lizardList
  ) != 0 and player.hp > 0:  #loop continues as long as there are dragons left and the player is alive
    print(player)
    for i in range(
        len(lizardList)):  #for each dragon left alive, display their stats
      print(f"{i+1}. {lizardList[i]}")
    dragonn = check_input.get_int_range(
      "\nChoose a dragon to attack: ", 1,
      len(lizardList))  #player chooses dragon to attack and weapon of choice
    if (dragonn == 1):
      attack_move(player, lizardList[0])
      if lizardList[0].hp <= 0:
        lizardList.pop(0)
    elif (dragonn == 2):
      attack_move(player, lizardList[1])
      if lizardList[1].hp <= 0:
        lizardList.pop(1)
    elif (dragonn == 3):
      attack_move(player, lizardList[2])
      if lizardList[2].hp <= 0:
        lizardList.pop(2)

    random_attack = randint(
      1,
      2)  #after each of players attack a random dragon will attack the player
    if len(lizardList) > 0:
      random_drag = randint(0, len(lizardList) - 1)
      if random_attack == 1:
        print(lizardList[random_drag].basic_attack(player))
      elif random_attack == 2:
        print(lizardList[random_drag].special_attack(player))

  if player.hp <= 0:  #displays the winner of the game
    print("You have been defeated")
  else:
    print(
      f"Congratulations {player}, you have defeated all 3 dragons, you have passed the trials."
    )


main()
