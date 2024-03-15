import dragon
from random import randint
class FireDragon(dragon.Dragon):
  """
  The class for Fire Dragon objects.
  Attributes:
  name, max_hp, hp: from the parent class
  _f_shots (Integer): The number of fire shots the Fire Dragon has left.
  """
  def __init__(self, name, max_hp, f_shots):
    """
    The constructor for the Fire Dragon object.
    Args:
    name (String): The name of the Fire Dragon.
    max_hp (Integer): The max_hp of the Fire Dragon.
    f_shots (Integer): The number of fire shots the Fire Dragon should have.
    """
    super().__init__(name, max_hp)
    self._f_shots = f_shots

  def special_attack(self, other):
    """Displays the fire dragons special attack and attacks the other object.
    Args:
    other (object): The object the Fire Dragon is attacking.
    Returns:
    A string of whether the dragon's attack failed (no fire shots left) or succeeded and with how much damage.
    """
    if self._f_shots > 0:
      attack = randint(5, 9)
      other.take_damage(attack)

      self._f_shots -= 1
      return f"{self._name} engulfs you in flames for {attack} damage."
    else:
      return "Dragon has no more fire shots left"
      
  def __str__(self):
    """
    returns the fire dragons stats
    Returns:
    A string with the dragon's name, hp, and how many fire shots it has left.
    """
    
    return super().__str__() + f"\nFire Shots: {self._f_shots}"