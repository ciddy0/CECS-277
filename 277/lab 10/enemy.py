import entity
from random import randint
class Enemy(entity.Entity):
  """
  The enemy class. This is for all the enemies the hero is supposed to defeat
  Attributes:
  _name (String): The name of the enemy. See the entity class for more information
  _max_hp (int): The maximum health for the enemy. See the entity class for more information.
  _hp (int): The enemy's current health. See the entity class for more information.
  """
  def __init__(self):
    """
    The constructor for the entity class.
    """
    nameList = ["Goblin", "Vampire", "Ghost", "Zombie", "Skeleton", "Werewolf", "Witch"]
    super().__init__(nameList[randint(0,6)], randint(4,8))
    
  def attack(self, entity):
    """
    The method for attacking the hero.
    Args:
    entity (Entity): Who is being attacked, which in this case is the hero.
    Returns:
    A string describing the attack to the player.
    """
    dmg = randint(1,4)
    entity.take_damage(dmg)
    return f"The {self.name} attacked! You took {dmg} damage!"