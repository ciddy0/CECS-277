import entity
from random import randint
class Dragon(entity.Entity):
  """
  The Dragon class for the dragons the hero must face.
  """
  def basic_attack(self, other):
    """
    The basic attack of the Dragon object.
    other (object): The object the Dragon is attacking.
    """
    damage = randint(3, 7)
    other.take_damage(damage)
    return f"{self.name} smashes you with its tail for {damage} points!"
 
  def special_attack(self, other):
    """
    The special attack of the Dragon object.
    other (object): The object the Dragon is attacking.
    """
    damage = randint(4, 8)
    other.take_damage(damage)
    return f"{self.name} slashes you with its claw for {damage} points!"
  