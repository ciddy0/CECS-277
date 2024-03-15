import puppystate
import stateplay
import stateasleep
class StateEat(puppystate.PuppyState):
  """
  Inherits from puppystate class to create a eat state for the puppy.
  """
  def play(self, puppy):
    """
    changes the state to play and increments play
    RETURNS: string describing the puppy's reaction
    """
    puppy.change_state(stateplay.StatePlay())
    puppy.inc_plays()
    return "Puppy stops eating and chases the ball."
  def feed(self, puppy):
    """
    increments feeds and checks if puppy is full
    RETURNS: string describing the puppy's reaction
    """
    puppy.inc_feeds()
    if puppy.feeds == 3:
      puppy.reset()
      puppy.change_state(stateasleep.StateAsleep())
      return "Puppy continues to eat.\n Puppy is too full and falls asleep."
    else:
      return "Puppy continues to eat."

