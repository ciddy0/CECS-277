class Card:
  """
  Creates a card 
  Attributes:
  suit - an integer index 0-3, representing the card suits of [‘Clubs’, ‘Diamonds’, ‘Hearts’,   
  ‘Spades’]
  rank - an integer; index 0-12, representing the card ranks of [‘2’, ‘3’, ‘4’, ‘5’, ‘6’, ‘7’, ‘8’, 
  ‘9’, ‘10’, ‘Jack’, ‘Queen’, ‘King’, ‘Ace’].
  """
  def __init__(self, suit, rank):
    self._suit = suit
    self._rank = rank
  @property
  def suit(self):
    """
    Access the card's suit
    """
    return self._suit
  @property
  def rank(self):
    """
    Access the card's rank
    """
    return self._rank
  def __str__(self):
    """
    Displays the card in the format rank of suit
    """
    card_ranks =  ['2','3','4','5','6','7','8','9','10','Jack','Queen','King', 'Ace']
    card_suits = ['Clubs', 'Diamonds', 'Hearts', 'Spades']
    return f"{card_ranks[self._rank]} of {card_suits[self._suit]}"
  def __lt__(self, other):
    """
    compares two card objects. Compares their rank and returns true if self rank is less than
    other rank
    """
    return(self._rank < other._rank)
    
  
    
  
  