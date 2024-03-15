import abc
class Entity(abc.ABC):
  """
  The abstract class for Entity objects (hero objects, dragon objects, etc.).
  Attributes:
    _name (String): The name of the entity
    _hp (Integer): The current health points of the entity
    _max_hp (Integer): The max health points of the enitity
  """
  def __init__(self,name,max_hp):
    """
    Initializes the entity with a name and max hp
    Args:
    name (String): The name of the entity
    max_hp (Integer): The max health points of the entity
    """
    self._name = name
    self._max_hp = max_hp
    self._hp = max_hp
    
  def take_damage(self,damage):
    """
    lowers the entities hp by amount of damage passed in
    Args:
    damage (Integer): The amount of damge the entity takes
    """""
    self._hp -= damage
    if self._hp < 0:
      self._hp = 0
      
  def __str__(self):
    """
    returns the entities name and hp
    Returns:
    A string containing the entity's name and their current hp compared to their max hp.
    """
    return f"{self._name}: ({self._hp}/{self._max_hp})"
  @property
  def name(self):
    """returns name"""
    return self._name
  @property
  def hp(self):
    """returns hp"""
    return self._hp

  @abc.abstractmethod
  def basic_attack(self,other):
    """abstract method for basic attack of entity"""
    pass
  @abc.abstractmethod
  def special_attack(self,other):
    """abstract method for special attack of entity"""
    pass
