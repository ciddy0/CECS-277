import entity
from random import randint

class EasySkeleton(entity.Entity):
  """
  This class contains methods for skeleton objects at a beginner level.
  """
  def __init__(self):
    """
    The constructor for the EasySkeleton class.
    """
    super().__init__("Skeletor", randint(3,4))
    
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
    #Needs a return string