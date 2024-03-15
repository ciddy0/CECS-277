import abc
class EnemyFactory(abc.ABC):
    """
    abstract class for enemy factory
    """
    @abc.abstractmethod
    def create_random_enemy(self):
      """
      Abstract method to create random enemy
      """
      pass