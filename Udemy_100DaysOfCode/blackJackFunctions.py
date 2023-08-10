#function draws the first hand
import random

def draw(x, cardDeck):
    drawArray = []
    for i in range (x):
        new_card = random.choice(cardDeck)
        drawArray.append(new_card)
    return drawArray

#this will remove a specific card from the deck
def removeCard(hand, card):
    hand.remove(card)

#function checks if that single card exists in the deck of the current hand for either the user or the dealer
def checkDraw(deck, draw):
    for item in deck:
        if item != draw:
            continue
        elif item == draw:
            return True
        else:
            return False

#function compares the hand of the user & and the dealer to see if they match - if they do have a matching item we will remove it with a function
def compareHands(playerHand, dealerHand):
    pos = 0
    for item in playerHand:
        if item != dealerHand[pos]:
            pos+=1
        if item == dealerHand[pos]:
            return True
        else:
            return False