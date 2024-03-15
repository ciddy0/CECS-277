import platedecorator
class Potatoes(platedecorator.PlateDecorator):
  """
  A decorator that adds potatoes.
  """
  def description(self):
    """
    RETURNS:
    A description of parent class and potatoes.
    """
    if super().count() > 0: 
      return super().description() + " and potatoes"
    return super().description() + 'potatoes'
  def area(self):
    """
    RETURNS:
    The parent class area - the area of the potatoes.
    """
    return super().area() - 18
  def weight(self):
    """
    RETURNS:
    Ther parent class weight - the weight of the potatoes
    """
    return super().weight() - 6
  def count(self):
    """
    RETURNS:
    Count + 1
    """
    return super().count() + 1