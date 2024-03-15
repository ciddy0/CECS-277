class Rectangle:
  """
  The rectangle class, which can create a rectangle on a grid.
  
  Attributes:
    w (int): the width of the rectangle
    h (int): the height of the rectangle
    x (int): the x-value of the top left corner of the rectangle
    y (int): the y-value of the top left corner of the rectangle.
  """
  
  def __init__(self, w, h):
    """
    The constructor for the rectangle object.

    Arguments:
      w (int): the width of the rectangle
      h (int): the height of the rectangle
    """
    self.w = w
    self.h = h
    self.x = 0
    self.y = 0

  def get_coords(self):
    """
    Returns the coordinates of the rectangle's top left corner in the form of a list.

    Returns:
      coords: the list with the x-value and y-value of the coordinates of the rectangle's top left corner.
    """
    coords = [self.x,self.y]
    return coords
    
  def get_dimensions(self):
    """
    Returns the dimensions of the rectangle.

    Returns:
      dimensions: the list with the width and height of the rectangle.
    """
    dimensions = [self.w, self.h]
    return dimensions
    
  def move_up(self):
    """
    Moves the rectangle up the grid by 1 space by changing the y-coordinate of the rectangle's top left corner.
    """
    self.y -= 1
    
  def move_down(self):
    """
    Moves the rectangle down the grid by 1 space by changing the y-coordinate of the rectangle's top left corner.
    """
    self.y += 1
    
  def move_right(self):
    """
    Moves the rectangle right on the grid by 1 space by changing the x-coordinate of the rectangle's top left corner.
    """
    self.x += 1
    
  def move_left(self):
    """
    Moves the rectangle left on the grid by 1 space by changing the x-coordinate of the rectangle's top left corner.
    """
    self.x -= 1