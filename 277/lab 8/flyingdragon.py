import dragon
from random import randint

class FlyingDragon(dragon.Dragon):
  """
  call from the dragon superclass
  ATTRIBUTES:
  name, max_hp, hp - from parent class
  swoops - int; number of special attacks they have
  """""
  
  def __init__(self, name, max_hp, swoops):
    """
    Initializes the flying dragon with a name, max hp, and number of swoops
    Args:
    name (String): The name of the dragon.
    max_hp (Integer): The max hp of the dragon.
    swoops (Integer): The number of swoops the dragon should start with.
    """
    super().__init__(name, max_hp)
    self._swoops = swoops

  def special_attack(self, other):
    """
    Oevrrides special attack and displays the flying dragon's special attack
    Args:
    other (object): The object that the dragon is attacking.
    RETURNS:
    string - name of dragon and attack damage done to player
    string - if dragon has no swoops, returns no swoops left
    """
    if self._swoops > 0:
      attack = randint(5,8)
      other.take_damage(attack)
      #woosh
      self._swoops -= 1
      return f"{self._name} swoops you for {attack} damage."
    else:
      #no woosh
      return "Dragon has no swoops left"
  def __str__(self):
    """
     returns the flying dragons stats
     Returns:
     A string with the name, hp, and the number of fire shots the dragon has left.
    """
    return super().__str__() + f"\nSwoop Shots: {self._swoops}"
    
    