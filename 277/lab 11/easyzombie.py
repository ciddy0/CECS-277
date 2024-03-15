import entity
from random import randint
class EasyZombie(entity.Entity):
    """
    The constructor for the EasyZombie class.
    """
    def __init__(self):
      """
      Initializes the EasyZombie class.
      """
      super().__init__("Zombie", randint(4,5))

    def attack(self, entity):
      """
      The method for attacking the hero.
      Args:
      entity (Entity): Who is being attacked, which in this case is the hero.
      Returns:
      A string describing the attack to the player.
      """
      dmg = randint(1,5)
      entity.take_damage(dmg)
      return f"The {self.name} attacked! You took {dmg} damage!"
    