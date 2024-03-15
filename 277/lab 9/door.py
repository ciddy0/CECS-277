import abc

class Door(abc.ABC):
  """
  Interface for the methods that the different doors have to override
  """
  @abc.abstractmethod
  def examine_door(self): 
    """
    returns a string description of the door
    """
    pass
  @abc.abstractmethod
  def menu_options(self):
    """
    returns string of menu options for the door
    """
    pass
  @abc.abstractmethod
  def get_menu_max(self):
    """
    returns the number of options in the above menu
    """
    pass
  @abc.abstractmethod
  def attempt(self,option):
    """
    passes in the user's selection from the menu
    """
    pass
  @abc.abstractmethod
  def is_unlocked(self):
    """
    checks to see if the door was unlocked. Returns true if it is otherwise false
    """
    pass
  @abc.abstractmethod
  def clue(self):
    """
    Returns a string hint if the user was unsuccesful at their attempt
    """
    pass
  @abc.abstractmethod
  def success(self):
    """
    Returns a string to congratulate user if they were successful
    """
    pass 