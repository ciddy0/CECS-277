import entity
from random import randint

class EasyGoblin(entity.Entity):
  """
  This class contains methods for goblin objects at a beginner level.
  """
  def __init__(self):
    """
    The constructor for the EasyGoblin class
    """
    super().__init__("Green Goblin", randint(4,6))

  def attack(self, entity):
    """
    The method for attacking the hero.
    Args:
    entity (Entity): Who is being attacked, which in this case is the hero.
    Returns:
    A string describing the attack to the player.
    """
    dmg = randint(2,5)
    entity.take_damage(dmg)
    return f"The {self.name} attacked! You took {dmg} damage!"
