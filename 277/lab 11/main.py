import map
import hero
import check_input  
import beginnerfactory
import expertfactory
from random import randint

def fight_monster(player,map, Fac):
  """
  Reveals the moster and gives the player the option to run or fight. If player runs, they will be moved in a random direction on the map. If you fight, you and the monster will take turns taking damage until one reaches hp of 0.
  Args:
  Fac(Factory): The factory that will create the monster.
  player (Hero): The hero.
  map (Map): The map.
  """
  monster = Fac.create_random_enemy() #FIXME no enemy class in this lab
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


def check_room(item, player,map, Fac):
  """
  Checks the location you enter
  Args:
  item (String): A string with a character representing what's in the room.
  player (Hero): The hero.
  map (Map): The map.
  Fac (fac): enemy factory
  """
  if item == 'n':
    print("There is nothing in this room...")
  elif item == 'm':
    fight_monster(player,map, Fac)
  elif item == 'i':
    print("You found a potion, you healed back up!")
    player.heal()
    map.remove_at_loc(player.loc)
  elif item == 's':
    print("You're at the start of the dungeon")

def main():
  """
  The main method that holds the game.
  """
  name = input("What is your name, traveler?: ")
  deadpool = hero.Hero(name)
  main_map = map.Map()
  play_again = True
  difficulty = check_input.get_int_range("Choose your difficulty: \n1. Beginner \n2. Expert \n", 1, 2)
  Fac = ""
  if difficulty == 1:
    Fac = beginnerfactory.BeginnerFactory()
  elif difficulty ==2:
    Fac = expertfactory.ExpertFactory()
  count = 1
  while (deadpool.hp > 0) and (play_again == True):
    print(deadpool)
    print(main_map.show_map(deadpool.loc))
    print("1. Go North\n2. Go South\n3. Go East\n4. Go West \n5. quit")
    direction = check_input.get_int_range("Enter choice: ", 1, 5)
    if direction == 1:
      item = deadpool.go_north()
      if item == 'o':
        print("You can't go that way")
      elif item == 'f':
        print(main_map.show_map(deadpool.loc))
        print("You found the stairs to the next dungeon")
        count += 1
        if count > 3:
          count = 1
        main_map.load_map(count)
      else: 
        check_room(item,deadpool,main_map,Fac)
    elif direction == 2:
      item = deadpool.go_south()
      if item == 'o':
        print("you can't go that way")
      elif item == 'f':
        print(main_map.show_map(deadpool.loc))
        print("You found the stairs to the next dungeon")
        count += 1
        if count > 3:
          count = 1
        main_map.load_map(count)
      else:
        check_room(item,deadpool,main_map, Fac)
        
    elif direction == 3:
      item = deadpool.go_east()
      if item == 'o':
        print("you can't go that way")
      elif item == 'f':
        print(main_map.show_map(deadpool.loc))
        print("You found the stairs to the next Dungeon")
        count += 1
        if count > 3:
          count = 1
        main_map.load_map(count)
      else:
        check_room(item,deadpool,main_map, Fac)
  
    elif direction == 4: 
      item = deadpool.go_west()
      if item == 'o':
        print("you can't go that way")
      elif item == 'f':
        print(main_map.show_map(deadpool.loc))
        print("You found the stairs to the next dungeon")
        count += 1
        if count > 3:
          count = 1
        main_map.load_map(count)
      else:
        check_room(item,deadpool,main_map, Fac)
    else:
      print("You quit the game :(")
      break
    
    main_map.reveal(deadpool.loc)
    print("")
  if deadpool.hp <= 0:
    print("You died...")
    
  
main()
