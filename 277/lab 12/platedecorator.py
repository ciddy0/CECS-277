import abc
import plate
class PlateDecorator(plate.Plate, abc.ABC):
  """
  PlateDecorator is an abstract class that decorates a plate by implementing plate interface and has a instance of that object.
  """
  def __init__(self, p):
    """
    Initializes the plate decorator with the plate object.
    """
    self._plate = p
  def description(self):
    """
    RETURN:
    plate description
    """
    return self._plate.description()
  def area(self):
    """
    RETURN:
    plate area
    """
    return self._plate.area()
  def weight(self):
    """
    RETURNS:
    plate weight
    """
    return self._plate.weight()
  def count(self):
    """
    RETURNS:
    count(items) on plate
    """
    return self._plate.count()
  
  