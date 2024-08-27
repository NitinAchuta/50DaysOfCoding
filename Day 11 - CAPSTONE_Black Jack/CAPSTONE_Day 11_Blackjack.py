############### Blackjack Project #####################

#Difficulty Normal 😎: Use all Hints below to complete the project.
#Difficulty Hard 🤔: Use only Hints 1, 2, 3 to complete the project.
#Difficulty Extra Hard 😭: Only use Hints 1 & 2 to complete the project.
#Difficulty Expert 🤯: Only use Hint 1 to complete the project.

############### Our Blackjack House Rules #####################

## The deck is unlimited in size. 
## There are no jokers. 
## The Jack/Queen/King all count as 10.
## The the Ace can count as 11 or 1.
## Use the following list as the deck of cards:
## cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
## The cards in the list have equal probability of being drawn.
## Cards are not removed from the deck as they are drawn.
## The computer is the dealer.

##################### Hints #####################

#Hint 1: Go to this website and try out the Blackjack game: 
#   https://games.washingtonpost.com/games/blackjack/
#Then try out the completed Blackjack project here: 
#   https://appbrewery.github.io/python-day11-demo/

import random
def check_for_ace(their_cards):
   if 11 in their_cards and sum(their_cards) > 21:
      print('There is an ace, it is being changed to a 1')
      their_cards[their_cards.index(11)] = 1
      return their_cards

play = input('Do you want to play a game of BlackJack? type "y" or "n": ')

while play == 'y':
   cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10] 
   
   your_cards = [cards[random.randint(0, len(cards) - 1)], cards[random.randint(0, len(cards) - 1)]]
   score = sum(your_cards)
   print(f"\tYour cards: {your_cards}, current score: {score}")
   comp_cards = [cards[random.randint(0, len(cards) - 1)], cards[random.randint(0, len(cards) - 1)]]
   print(f"\tComputer's first card: {comp_cards[0]}")
   another_card = input('Type "y" to get another card, type "n" to pass: ')
   over_21 = False

   while another_card == 'y':
      your_cards.append(cards[random.randint(0, len(cards) - 1)])
      check_for_ace(your_cards)
      score = sum(your_cards)
      print(f"\tYour cards: {your_cards}, current score: {score}")
      

      if score > 21:
         over_21 = True
         break
      another_card = input('Type "y" to get another card, type "n" to pass: ')
    
   print(f"\tComputer's final hand: {comp_cards}, final score: {sum(comp_cards)}")
   if over_21:
      print('You went over. You lose')
   elif score > sum(comp_cards):
      print('You win!')
   else:
      print("You lost.")
      
   play = input('Do you want to play a game of BlackJack? type "y" or "n": ')