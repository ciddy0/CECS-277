import door
import random
class LockedDoor(door.Door):
  """
  A locked door that the player needs to find the key for.
  ATTRIBUTES:
  _key_location: int; a randomized integer from 1 to 3 (inclusive)
  _input: int; the user's choice for where they'll search for the key
  """

  def __init__(self):
    """
    The constructor for the LockedDoor class.
    """
    self._key_location = random.randint(1,3)
    self._input = 0
  
  def examine_door(self):
    """
    Returns a string descibing the locked door.
    Returns:
    A strin desciption of the locked door.
    """
    return "You encounter a locked door. Look around for the key."

  def menu_options(self):
    """
    Returns a string of menu options to look for the locked door's key.
    Returns:
    A string for the options of where the user can look for th ekey to the door.
    """
    return "1. Look under mat\n2. Look under flower pot\n3. Look under fake rock"

  def get_menu_max(self):
    """
    Returns the number of menu options
    Returns:
    An integer for the number of menu options.
    """
    return 3

  def attempt(self, option):
    """
    Store's the user's chosen option of where they'll be searching and returns a desciption of where they searched.
    Args:
    option (int): The number of the option of where they'll search.
    Returns:
    A string describing where the user searched.
    """
    self._input = option
    if option == 1:
      return "You looked under the mat."
    elif option == 2:
      return "You looked under the flower pot."
    elif option == 3:
      return "You looked under the fake rock."

  def is_unlocked(self):
    """
    Checks whether the door has been unlocked.
    Returns:
    A boolean value based on whether or not the door was unlocked.
    """
    if self._input == self._key_location:
      return True
    else:
      return False
      
  def clue(self):
    """
    Returns a clue for when the user fails to find the key.
    Returns:
    A string hinting the user to try again.
    """
    return "Look somewhere else."

  def success(self):
    """
    Returns a congradulatory message for when the user unlocks the door.
    Returns:
    A string with a congradulatory message for the user.
    """
    return "You found the key and opened the door!"

  