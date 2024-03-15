import puppystate
import stateasleep
class StatePlay(puppystate.PuppyState):
  """
  Inherites from the puppystate class for play state for the puppy
  """
  def play(self, puppy):
    """
    increments plays and checks if puppy is tired
    """
    puppy.inc_plays()
    if puppy.plays == 4:
      puppy.reset()
      puppy.change_state(stateasleep.StateAsleep())
      return "You throw the ball again and the puppy excitedly chases it.\n Puppy is too tired to play and falls asleep"
    else:
      return "You throw the ball again and the puppy excitedly chases it."
  def feed(self, puppy):
    """
    returns a string of the puppys reaction to being fed
    """
    return "The puppy is too busy playing with the ball to eat right now."

