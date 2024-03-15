import entity
from random import randint
class Zombie(entity.Entity):
  def __init__(self):
    """
    The constructor for the Zombie class
    """
    super().__init__("Huge Zombie", randint(8,10))

  def attack(self, entity):
    """
    The method for attacking the hero.
    Args:
    entity (Entity): Who is being attacked, which in this case is the hero.
    Returns:
    A string describing the attack to the player.
    """
    dmg = randint(5,12)
    entity.take_damage(dmg)
    return f"The {self.name} attacked! You took {dmg} damage!"