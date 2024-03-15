import door
from random import randint
class ComboDoor(door.Door):
  """
  Combnination door where user has the guess the number
  ATTRUBUTES:
  _correct_value: int; randomized int 1-10
  _input: intl; value user guessed
  """
  def __init__(self):
    """
    The constructor for the ComboDoor class.
    """
    self._correct_value = randint(1,10)
    self._input = 0

  def examine_door(self): 
    """
    Returns a string description of the combo door.
    Returns:
    A string describing the combo door.
    """
    return "You encounter a door with a combination lock. You can spin the dial to a number 1-10."
  pass
  def menu_options(self):
    """
    Returns string of combo range.
    Returns:
    A string for the range of the possible combinations.
    """
    return "Enter number 1-10: "
  pass
  def get_menu_max(self):
    """
    Returns the number of options in the menu.
    Reutrns:
    An integer with the number of options the user can choose from.
    """
    return 10
  pass
  def attempt(self,option):
    """
    Passes in the user's guess.
    Args:
    option (int): The number the user chose to unlock the door.
    Returns:
    A string describing the user's guess attempt.
    """
    self._input = option
    return f"You attempted the number {str(self._input)}"
  pass
  def is_unlocked(self):
    """
    Checks to see if the door was unlocked.
    Returns:
    A boolean of whether or not the door was unlocked.
    """
    if self._input == self._correct_value:
      return True
    else:
      return False
  pass
  def clue(self):
    """
    Returns a string hint based on if their guess was too high or too low.
    Returns:
    A string hinting to the user of whether their guess was too high or low.
    """
    if self._input > self._correct_value:
      return "Too High!"
    else:
      return "Too Low!"
  pass
  def success(self):
    """
    Returns a string to congratulate user if they were successful.
    Returns:
    A string with a congradulatory message.
    """
    return "Congrats you opened the door"
  pass