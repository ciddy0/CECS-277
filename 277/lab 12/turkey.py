import platedecorator
class Turkey(platedecorator.PlateDecorator):
  """
  Decorater that adds turkey
  """
  def description(self):
    """
    RETURNS:
    parent class description and turkey
    """
    if super().count() > 0: 
      return super().description() + " and turkey"
    return super().description() + " turkey"
  def area(self):
    """
    RETURNS:
    parent class area - turkey area
    """
    return super().area() - 15
  def weight(self):
    """
    RETURNS:
    parent class weight - turkey weight
    """
    return super().weight() - 4
  def count(self):
    """
    RETURNS:
    count + 1
    """
    return super().count() + 1