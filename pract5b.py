#A program to shuffle deck of cards

#Python code:
import random

deck = []
suits = ["Hearts", "Diamonds", "Clubs", "Spades"]
cardfaces = ["J", "Q", "K", "A"]
for i in range(2, 11):
    cardfaces.append(str(i))

for suit in suits:
    for face in cardfaces:
        card = face + " of " + suit
        deck.append(card)

random.shuffle(deck)

for card in deck:
    print(card)