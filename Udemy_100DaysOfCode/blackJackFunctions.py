#function draws the first hand
import random

#draw card from deck
def draw(x, cardDeck):
    condition = True
    drawArray = []
    newCard = random.choice(cardDeck)
    drawArray.append(newCard)
    for i in range (x-1):
        while condition: 
            newCard = random.choice(cardDeck)
            if newCard not in drawArray:
                drawArray.append(newCard)
                condition = False
            else:
                condition = True
    return drawArray

#draw card from deck
def newDraw(x, cardDeck):
    drawArray = []
    for i in range(x):
        newCard = random.choice(cardDeck)
        drawArray.append(newCard)
    return drawArray

#Check the hand and remove all of items in hand from deck
def removeFromDeck(hand, deck):
    length = len(hand)
    for i in range (length):
        if hand[i] in deck:
            deck.remove(hand[i])
        else:
            continue
    return deck

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

#checks if the total is equal to or above 17 for the dealers hand, if it is then the dealer will stay
def check17(dealerHand):
    total = 0
    for card in dealerHand:
        total = card + total
    if total >= 17:
        return True
    else:
        False    

#checks if either dealer or player has 22 then gives player a choice to chose to convert the ACE from 11 to 1, with an additional draw - for the dealer in order to automate we will have the RNG choose if it stays 22 the game is over, if less than the dealer draws one more
def has22(hand):
    counter = 0
    for card in hand:
        if card == 11:
            counter += 1
    if counter >1:
        return True
    else:
        return False
    
def replaceAce(hand):
      for card in hand:
        if card == 11:
            hand.remove(card)
            hand.append(1)
            return hand