import entity
from random import randint
class Skeleton(entity.Entity):
  def __init__(self):
    """
    The constructor for the Skeleton class
    """
    super().__init__("Enraged Skeletor", randint(6,10))

  def attack(self, entity):
    """
    The method for attacking the hero.
    Args:
    entity (Entity): Who is being attacked, which in this case is the hero.
    Returns:
    A string describing the attack to the player.
    """
    dmg = randint(6,10)
    entity.take_damage(dmg)
    return f"The {self.name} attacked! You took {dmg} damage!"