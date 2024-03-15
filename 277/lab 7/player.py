
class Player:
  """
  Creates player objects that can hit (draw a card/remove card from deck) and calculate score
  ATTRIBUTES:
  deck - deck object; creates a deck of 52 cards
  hand - deck object; stores players cards in a list
  """
  def __init__(self, deck):
    """
    ARGUEMENTS:
    deck - deck object; 
    """
    self._deck = deck
    self._hand = []
    #gives player 2 cards
    for i in range(2):
      randomCard = self._deck.draw_card()
      self._hand.append(randomCard)
    self._hand.sort()
    
  def hit(self):
    """
    draws a card and removes the card from the deck and sorts their hand
    """ 
    randomCard = self._deck.draw_card()
    self._hand.append(randomCard)
    self._hand.sort()

  def score(self):
    """
    calculates the score of the player
    RETURNS:
    score - int type; the score of the player
    """
    #calculates teh
    score = 0
    ranks = [2,3,4,5,6,7,8,9,10,10,10,10,11]
    for item in self._hand:
      if (item.rank == 12 and score+11 > 22):
        score += 1
      else:
        score += ranks[item.rank]
    return score
        
    
  def __str__(self):
    """
    Returns a string with the cards in players hand and the score
    """
    cards = ""
    for item in self._hand:
      cards += str(item) + "\n"
    return f"{cards}score: {str(self.score())}"