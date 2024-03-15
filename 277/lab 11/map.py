class Map:
  """
  Creates singleton class so that other classes can access the global map.
  Attributes:
  _instance (Map): Stores a singleton instance of Map.
  _initialize (boolean): A boolean representing whether a map object was initialized or not.
  _map (list): A 2D list representing the map.
  _revealed (boolean): A boolean representing if a specifc space on the map was revealed or not.
  """
  _instance = None
  _initialize = False
  def __new__(cls):
    """
    Creates a new object of Map.
    Args:
    cls (Map): The class that is being created.
    Returns:
    A new Map object.
    """
    if cls._instance is None:
      cls._instance = super().__new__(cls)
    return cls._instance

  def __init__(self):
    """
    The constructor for the class.
    """
    if not Map._initialize:
      self.load_map(1)
      Map._initialize = True

  def load_map(self, map_num):
    """
    ARGUEMENTS:
    map_num - int; map level
    Loads a map from a file given the map level
    """
    map_file = "map" + str(map_num) + ".txt"
    file = open(map_file)
    self._map = []
    for row in file:
      list = []
      for item in row:
        if item!= '\n':
          list.append(item)
      self._map.append(list)
    self._revealed = [[False for _ in row] for row in self._map] 

  def __getitem__(self, row):
    """
    Gets a list based on the row specified.
    Args:
    row (int): The index for where the row is in the outer list.
    Returns:
    The list in the 2D map at the specified location.
    """
    return self._map[row]

  def __len__(self):
    """
    Gets the length of the current map (the number of rows map has.)
    Returns:
    The length of map.
    """
    return len(self._map)

  def show_map(self,loc):
    """
    Prints the map into the console.
    Args:
    loc (list): The list with the hero's location.
    Returns:
    A string showing the map.
    """
    #set x and y of location
    x = loc[0]
    y = loc[1]

    #use list comphrension to creates a copy of the map and displays x if the location is not revelaed
    show_map = [['x' if not self._revealed[row][col] else self._map[row][col] for col in range(len(self._map[row]))] for row in range(len(self._map))]
    show_map[x][y] = '*'

    #itertates and adds to our map string
    map_string = ""
    for row in range(len(show_map)):
      for col in range(len(show_map[row])):
        map_string += show_map[row][col]
      map_string += '\n'
    return map_string

  def reveal(self, loc):
    """
    Reveals the location specified on the map.
    Args:
    loc (list): The list with the location meant to be revealed.
    """
    x = loc[1]
    y = loc[0]
    self._revealed[y][x] = True

  def remove_at_loc(self, loc):
    """
    Removes the enemy from the map.
    Args:
    loc (list): The list with the location of the enemy.
    """
    x = loc[0]
    y = loc[1]
    self._map[x][y] = 'n'




