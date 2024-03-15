import check_input
import deck
import player
import dealer
# Author: Diego Cid, Lela Wondafrash, Sarena Hieng
# Date: 10/03/2023
# Description: 

def display_winner(pScore, dScore, points):
  #checks who wons and adds a point
  if(pScore >= 22 and dScore >= 22) or (pScore == dScore):
    print("It's a tie!")
  if (pScore > dScore and pScore <= 22) or (dScore >= 22 and pScore < 22):
    print("The player wins!")
    points[0] += 1
  elif (dScore > pScore and dScore <= 22) or (pScore >= 22 and dScore < 22):
    print("The dealer wins!")
    points[1] += 1

  #prints points of dealer and player
  print("Player score: " +str(points[0]) + "")
  print("Dealer score: " + str(points[1]) + "\n")
  

def main():
  #start
  print("--Blackjack--")
  finished = False
  pointList = [0, 0]
  deck1 = deck.Deck()
  deck1.shuffle()

  #plays until user ends the game
  while (finished == False):
    #checks to see if deck is running out of cards
    if(len(deck1) < 15):
      deck1 = deck.Deck()
      deck1.shuffle()

    #simulate players turn
    player1 = player.Player(deck1)
    print("Player's Card:\n"+str(player1))
    while player1.score() <= 21:
      option = check_input.get_int_range("1. Hit\n2. Stay\nEnter Choice: ", 1, 2)
      print("")
      if option == 1:
        player1.hit()
        print("Player's Card:\n"+str(player1))
      elif option == 2:
        break
      if player1.score() > 21:
        print("Bust!\n")
        break
    #simulate dealers turn
    d = dealer.Dealer(deck1)
    print(d.play())

    #display winner
    display_winner(player1.score(), d.score(), pointList)
    
    if check_input.get_yes_no("Would you like to end the game? (Y/N): "):
      finished = True
      
  
  
main()