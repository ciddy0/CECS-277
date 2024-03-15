import check_input
from combodoor import ComboDoor
from basicdoor import BasicDoor
from lockeddoor import LockedDoor
from random import randint

# Author: Diego Cid, Lela Wondafrash, Sarena Hieng
# Date: 10/12/2023
# Description: This program simulates an escape room by generating a random combination of 3 doors. The user attempts to pass each room given the clues give until all 3 rooms are unlocked and they win the game.

#interface then basic door then test then rest of dorrs
def open_door(door):
  """
  Passes in a door the user will try to unlock. It displays a desciption of the door and its menu. Then, the user will be prompted to return an option and the desciption of that option will be displayed as well. If the user's attempt fails, a clue is displayed and the function loops. If the user succeeds, a congradulatory message is displayed.
  Args:
  door (object): The door the user will attempt to open.
  """
  print(door.examine_door())
  print(door.menu_options())
  user_input = check_input.get_int_range("Enter your choice: ", 1, door.get_menu_max())
  print(door.attempt(user_input))
  while door.is_unlocked() == False:
    print(door.clue() + "\n")
    
    print(door.menu_options())
    user_input = check_input.get_int_range("Enter your choice: ", 1, door.get_menu_max())
    print(door.attempt(user_input))

  print(door.success())

def main():
  #creates a list of doors
  doors = [ComboDoor(), BasicDoor(), LockedDoor()]

  #iterates through the list and removes it if the player opens the door
  for i in range(len(doors)):
    if len(doors) == 0:
      num = 0
    else: 
      num = randint(0,len(doors)-1)
    open_door(doors[num])
    doors.pop(num)
    print("")

  print("You've Escaped!!!!")
  
    
    
    
    
  
  
main()