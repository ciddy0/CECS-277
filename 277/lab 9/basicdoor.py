import door
from random import randint
"""
The constructor for the BasicDoor class.
ATTRIBUTES:
_state: int; the option number for whether the door needs to pushed or pulled in order to open.
_input: int; the option that the user chose in an attempt to open the door.
"""

class BasicDoor(door.Door):

  def __init__(self):
    """
    The constructor for the BasicDoor class.
    """
    self._state = randint(1, 2)
    self._input = 0 
    

  def examine_door(self): 
    """
    Returns a string description of the door
    Returns:
    A string desciption of the basic door.
    """
    return "You encounter a basic door. It can be pushed or pulled."

  
  def menu_options(self):
    """
    Returns string of menu options for the door.
    Returns:
    A string of the menu options the user must pick from to try to open the door.
    """
    return "1. Push\n2. Pull"


  def get_menu_max(self):
    """
    Returns the number of options in the above menu.
    Returns:
    An integer with the number of options in the menu.
    """
    return 2


  def attempt(self,option):
    """
    Passes in the user's selection from the menu.
    Args:
    option (int): The number for the option the user chose.
    Returns:
    A string describing the user's choice.
    """
    self._input = option
    if option == 1:
      return "You push the door"
    else:
      return "You pull the door"
    


  
  def is_unlocked(self):
    """
    Checks to see if the door was unlocked.
    Returns:
    A boolean of whether the door was unlocked or not.
    """
    if self._state == self._input: 
      return True
    else :
      return False
      
  def clue(self):
    """
    Returns a string hint if the user was unsuccesful at their attempt.
    Returns:
    A string hinting the user to try again.
    """
    return "Try the other way."

  
  def success(self):
    """
    Returns a string to congratulate user if they were successful.
    Returns:
    A string with a congradulatory message.
    """
    if self.is_unlocked() == True:
      return "Congratulations, you opened the door."
      
  