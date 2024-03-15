import abc
class Plate(abc.ABC):
  """
  Plate interface with abstract methodds
  """
  @abc.abstractmethod
  def description(self):
    """
    description of plate
    """
    pass
    
  @abc.abstractclassmethod
  def area(self):
    """
    Area of plate
    """
    pass
    
  @abc.abstractmethod
  def weight(self):
    """
    Weigth of plate
    """
    pass
    
  @abc.abstractmethod
  def count(self):
    """
    return count as 0
    """
    pass
  