import abc 

class Entity(abc.ABC):
  """
  The Entity class. It is mainly used for the enemies and the hero so that they can inherit necessary methods.
  Attributes:
  _name (String): The name of the entity.
  _max_hp (int): The entity's max hp.
  _hp (int): The current hp of the entity.
  """
  def __init__(self, name, max_hp):
    """
    The constructor for the Entity class.
    Args:
    name (String): The name of the entity.
    max_hp (int): The max hp of the entity.
    """
    self._name = name
    self._max_hp = max_hp
    self._hp = max_hp
    
  def take_damage(self, damage):
    """
    Allows the entity to take damage.
    Args:
    damage (int): The amount of damage the entity will take.
    """
    if self._hp - damage < 0:
      self._hp = 0
    else:
      self._hp -= damage

  def heal(self):
    """
    Allows the entity to heal itself to its max hp.
    """
    self._hp = self._max_hp

  @property
  def name(self):
    """
    Returns the entity's name.
    Returns:
    The entity's name.
    """
    return self._name
    
  @property
  def hp(self):
    """
    Returns the entity's current hp.
    Returns:
    The entity's current hp.
    """
    return self._hp
      
  def __str__(self):
    """
    The string representing the entity.
    Returns:
    A string with the entity's name, max hp, and current hp.
    """
    return f"Name: {self._name}\nHP: {self._hp}/{self._max_hp}"

  @abc.abstractmethod
  def attack(self, entity):
    """
    An abstract method for an entity attacking another entity.
    Args:
    entity (Entity): The entity being attacked.
    """
    pass
      