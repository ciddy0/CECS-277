import puppystate
import stateeat
class StateAsleep(puppystate.PuppyState):
  """
  Inherits from the puppystate class for asleep state for puppy
  """
  def play(self, puppy):
    """
    returns puppy doesnt want to play
    """
    return "Puppy is asleep. It doesn't want to play right now."
  def feed(self, puppy):
    """
    changes state to eating and increments feeds
    RETURNS: string describing the puppy's reaction
    """
    puppy.change_state(stateeat.StateEat())
    puppy.inc_feeds()
    return "Puppy wakes up and comes running to eat."
    
    