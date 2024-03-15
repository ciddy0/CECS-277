import entity
from random import randint
class Hero(entity.Entity): 
  """
  The class for the Hero, who the user plays as.
  Attributes:
  name, max_hp, hp: from the parent class
  """
  def basic_attack(self,other):
    """
    displays the players attack move onto the dragon
    other (object): The object the player is attacking.
    """""
    attack = randint(1,6) + randint(1,6)
    other.take_damage(attack)
    return f"You slash the {other.name} with your sword for {attack} damage"
    
  def special_attack(self,other):
    """
    displays the players special attack move onto the dragon
    other (object): The object the player is attacking.
    """
    attack = randint(1,12)
    other.take_damage(attack)
    return f"You hit the {other.name} with an arrow for {attack} damage"