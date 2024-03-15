import platedecorator
class GreenBeans(platedecorator.PlateDecorator):
  """
  Decorator that adds green beans to a plate.
  """
  def description(self):
    """
    RETURNS:
    parent class description and green beans
    """
    if super().count() > 0: 
      return super().description() + " and green beans"
    return super().description() + 'green beans'
  def area(self):
    """
    RETURNS:
    Subtracts area of green beans with parent area
    """
    return super().area() - 20
  def weight(self):
    """
    RETURNS:
    Subtracts weight of green beans with parent weight
    """
    return super().weight() - 3
  def count(self):
    """
    RETURNS:
    count + 1
    """
    return super().count() + 1
  