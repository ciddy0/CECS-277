import plate
class LargePlate(plate.Plate):
  """
  Implements the Plate interface and constructs a large plate
  """
  def description(self):
    """
    Return a description of the plate
    """
    return "Large plate with"
  def area(self):
    """
    Return the area of the plate
    """
    return 113
  def weight(self):
    """
    Returns weight of the plate
    """
    return 24
  def count(self):
    """
    returns 0
    """
    return 0