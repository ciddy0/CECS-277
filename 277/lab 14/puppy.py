import stateasleep
class Puppy:
  """
  Puppy class that has the state of the puppy and the number of feeds and plays
  """
  def __init__(self):
    self._state = stateasleep.StateAsleep()
    self._feeds = 0
    self._plays = 0
    
  @property
  def feeds(self):
    """
    Returns the number of feeds
    """
    return self._feeds
    
    return self._feeds
  @property
  def plays(self):
    """
    Returns the number of plays
    """
    return self._plays
    
  def change_state(self, new_state):
    """
    Changes the state of the puppy
    """
    self._state = new_state
    
  def throw_ball(self):
    """
    calls the play method from the state class
    """
    return self._state.play(self)
    
  def give_food(self):
    """
    calls the feed method from state class
    """
    return self._state.feed(self)
    
  def inc_feeds(self):
    """
    increments the number of feeds
    """
    self._feeds += 1
  def inc_plays(self):
    """
    increments the number of plays
    """
    self._plays += 1
    
  def reset(self):
    """
    resets feeds and plays 
    """
    self._feeds = 0
    self._plays = 0
  
  
    