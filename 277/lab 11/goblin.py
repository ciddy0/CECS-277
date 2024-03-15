import entity
from random import randint
class Goblin(entity.Entity):
  def __init__(self):
    """
    The constructor for the Goblin class
    """
    super().__init__("Angry Green Goblin", randint(8,12))
  def attack(self, entity):
    """
    The method for attacking the hero.
    Args:
    entity (Entity): Who is being attacked, which in this case is the hero.
    Returns:
    A string describing the attack to the player.
    """
    dmg = randint(6,12)
    entity.take_damage(dmg)
    return f"{self.name} attacks {entity.name} for {dmg} damage."
    
  