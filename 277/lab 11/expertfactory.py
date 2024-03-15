import random
import enemyfactory
import goblin
import skeleton
import zombie

class ExpertFactory(enemyfactory.EnemyFactory):
  """
  The factory for expert-level enemies.
  """
  def create_random_enemy(self):
    """
    Creates an expert-level enemies.
    Returns:
    An expert-level enemy.
    """
    choice = random.randint(1, 3)
    if choice == 1:
     goblin.Goblin()
    elif choice == 2:
      skeleton.Skeleton()
    else:
      zombie.Zombie()