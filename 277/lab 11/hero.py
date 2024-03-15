import entity
import map
from random import randint
class Hero(entity.Entity):
  """
  The hero class, which represents the player.
  Attributes:
  _name (String): The name of the enemy. See the entity class for more information
  _max_hp (int): The maximum health for the enemy. See the entity class for more information.
  _hp (int): The enemy's current health. See the entity class for more information.
  """
  def __init__(self, name):
    """
    The constructor for the Hero class.
    Args:
    name (String): The name of the hero.
    """
    super().__init__(name,500)
    self._loc = [0,0]

  def attack(self, entity):
    """
    The method for attacking enemies
    Args:
    entity (Entity): The enemy being attacked. This should be an enemy.
    Returns:
    A string describing the hero's attack.
    """
    damage = randint(2,5)
    entity.take_damage(damage)
    return f"{self.name} attacks {entity.name} for {damage} damage."
  @property
  def loc(self):
    """
    Returns the hero's location.
    Returns:
    The hero's location.
    """
    return self._loc
  def go_north(self):
    """
    Moves the hero north on the map.
    Returns:
    Either 'o' if the hero can't move north or the coordinates of the new location of the hero.
    """
    mapp = map.Map()
    if self._loc[0] - 1 < 0:
      return 'o'
    else:
      self._loc[0] -= 1
      return mapp[self._loc[0]][self._loc[1]]

  def go_south(self):
    """
    Moves the hero south on the map.
    Returns:
    Either 'o' if the hero can't move south or the coordinates of the new location of the hero.
    """
    mapp = map.Map()
    if self._loc[0] + 1 < len(mapp):
      self._loc[0] += 1
      return mapp[self._loc[0]][self._loc[1]]
    else:
      return 'o'

  def go_east(self):
    """
    Moves the hero east on the map.
    Returns:
    Either 'o' if the hero can't move east or the coordinates of the new location of the hero.
    """
    mapp = map.Map()
    if self._loc[1] + 1 < len(mapp):
      self._loc[1] += 1
      return mapp[self._loc[0]][self._loc[1]]
    else:
      return 'o'

  def go_west(self):
    """
    Moves the hero west on the map.
    Returns:
    Either 'o' if the hero can't move west or the coordinates of the new location of the hero.
    """
    mapp = map.Map()
    if self._loc[1]-1 < 0:
      return 'o'
    else:
      self._loc[1] -= 1
      return mapp[self._loc[0]][self._loc[1]]
