import platedecorator
class Stuffing(platedecorator.PlateDecorator):
  """
  A decorator that adds stuffing.
  """
  def description(self):
    """
    A desciption of the parent class and stuffing.
    """
    if super().count() > 0: 
      return super().description() + " and stuffing"
    return super().description() + 'stuffing'
  def area(self):
    """
    RETURNS:
    The parent class area - the area of the stuffing
    """
    return super().area() - 18
  def weight(self):
    """
    RETURNS:
    The parent class weight - the weight of the stuffing.
    """
    return super().weight() - 7
  def count(self):
    """
    RETURNS:
    Count + 1
    """
    return super().count() + 1