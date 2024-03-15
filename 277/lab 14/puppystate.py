import abc
class PuppyState(abc.ABC):
  """
  Interface for state classes
  """
  @abc.abstractmethod
  def feed(self, puppy):
    """
    Abstract method for feed
    """
    pass
  def play(self, puppy):
    """
    Abstract method for play
    """
    pass
  