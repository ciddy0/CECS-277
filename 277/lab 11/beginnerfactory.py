from random import randint
import enemyfactory
import easygoblin
import easyskeleton
import easyzombie
class BeginnerFactory(enemyfactory.EnemyFactory):
  """
  The factory for the beginner-level enemies.
  """
  def create_random_enemy(self):
    """
    Creates a random beginner-level enemy.
    Returns:
    A beginner-level enemy.
    """
    choice = randint(1, 3)
    if choice == 1:
      return easygoblin.EasyGoblin()
    elif choice == 2:
      return easyskeleton.EasySkeleton()
    else:
      return easyzombie.EasyZombie()
    
    