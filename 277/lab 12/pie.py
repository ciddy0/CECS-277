import platedecorator
class Pie(platedecorator.PlateDecorator):
  """
  Decorator that adds pie to a plate
  """
  def description(self):
    """
    RETURNS:
    a description of parent class and pie
    """
    if super().count() > 0: 
      return super().description() + " and pie"
    return super.description() + ' pie'
  def area(self):
    """
    RETURNS:
    the parent class area - the area of pie
    """
    return super().area() - 19
  def weight(self):
    """
    RETURNS:
    the parent class weight - the weight of pie
    """
    return super().weight() - 8
  def count(self):
    """
    RETURNS:
    count + 1
    """
    return super().count() + 1