import player

class Dealer(player.Player):
  """
  Simulates a round for the dealer.
  RETURNS:
  string of the dealer's hand, score, hits, and whether or not they busted
  """
  def play(self):
    self.score()
    hand = str(self)
    dealer_hits = ""
    dealers_play = f"Dealer's Card:\n{hand}\n"
    while self.score() <= 16: 
      self.hit()
      
      #dealer_hits += str(self) 
      dealers_play += f"Dealer Hits!\n\nDealer's Cards:\n{str(self)}\n"
    if self.score() > 21:
      return f"{dealers_play}Dealer Bust!\n"
    else:
      return f"{dealers_play}Dealer Stays!\n"
    



