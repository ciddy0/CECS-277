import random
import card
class Deck:  
  """
  Creates a deck of 52 cards and stores it in a list
  ATTRIBUTES:
  cards - card[]; a list of 52 card objects
  """
  def __init__(self):
    
    self._cards = []
    for i in range(13):
      for j in range(4):
        self._cards.append(card.Card(j,i))
        
  def shuffle(self):
    """
    Shuffles the deck of cards
    """
    random.shuffle(self._cards)

  def draw_card(self):
    """
    Removes the top card and displays it
    RETURNS:
    string of the top card
    """
    topCard = self._cards[0]
    self._cards.pop(0)
    return topCard
    

  def __len__(self):
    """
    Returns the length of the cards list.
    RETURNS:
    length of cards list
    """
    return len(self._cards)
     
    
              
  