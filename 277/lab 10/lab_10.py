import map
import hero
import enemy
import check_input
from random import randint

def fight_monster(player,map):
  """
  Reveals the moster and gives the player the option to run or fight. If player runs, they will be moved in a random direction on the map. If you fight, you and the monster will take turns taking damage until one reaches hp of 0.
  Args:
  player (Hero): The hero.
  map (Map): The map.
  """
  monster = enemy.Enemy()
  print(f"You encounter a {monster.name}\n{monster}")
  choice = check_input.get_int_range("1. Fight Monster\n2. Run\n", 1, 2)
  if choice == 1:
    while monster.hp != 0 and player.hp != 0:
      print(player.attack(monster))
      if monster.hp != 0:
        print(monster.attack(player))
      elif monster.hp == 0:
        print("you have defeated the monster")
        map.remove_at_loc(player.loc)
  if choice == 2:
    dire = randint(1,4)
    if dire == 1:
      player.go_north()
    elif dire == 2:
      player.go_south()
    elif dire == 3:
      player.go_east()
    elif dire == 4:
      player.go_west()

def check_room(item, player,map):
  """
  Checks the location you enter
  Args:
  item (String): A string with a character representing what's in the room.
  player (Hero): The hero.
  map (Map): The map.
  """
  if item == 'n':
    print("There is nothing in this room...")
  elif item == 'm':
    fight_monster(player,map)
  elif item == 'i':
    print("You found a potion, you healed back up!")
    player.heal()
    map.remove_at_loc(player.loc)
  elif item == 's':
    print("You're at the start of the dungeon")
  elif item == 'f':
    print(map.show_map(player.loc))
    print("You completed the dungeon")
    exit()

def main():
  """
  The main method that holds the game.
  """
  name = input("What is your name, traveler?: ")
  spiderman = hero.Hero(name)
  main_map = map.Map()
  play_again = True 
  
  while (spiderman.hp > 0) and (play_again == True):
    print(spiderman)
    print(main_map.show_map(spiderman.loc))
    print("1. Go North\n2. Go South\n3. Go East\n4. Go West \n5. quit")
    direction = check_input.get_int_range("Enter choice: ", 1, 5)
    if direction == 1:
      item = spiderman.go_north()
      if item == 'o':
        print("You cant go that way")
      else: 
        check_room(item,spiderman,main_map)
    elif direction == 2:
      item = spiderman.go_south()
      if item == 'o':
        print("you cant go that way")
      else:
        check_room(item,spiderman,main_map)
    elif direction == 3:
      item = spiderman.go_east()
      if item == 'o':
        print("you cant go that way")
      else:
        check_room(item,spiderman,main_map)
    elif direction == 4: 
      item = spiderman.go_west()
      if item == 'o':
        print("you cant go that way")
      else:
        check_room(item,spiderman,main_map)
    else:
      print("You quit the game :(")
      break
    main_map.reveal(spiderman.loc)
    print("")
  if spiderman.hp <= 0:
    print("You died...")
      
  
main()