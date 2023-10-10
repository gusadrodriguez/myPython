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

def check17(dealerHand):
    total = 0
    for card in dealerHand:
        total = card + total
    if total >= 17:
        return True
    else:
        False    

def has22(hand):
    counter = 0
    for card in hand:
        if card == 11:
            counter++
            if counter > 1:
                #!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!! left off here - trying to make an iterative way to count for the number of 11's and replace ONE with a 1 value marker only when 22 is drawn the first time

    #check the items in the array
    #if they equal 22 then change 11 to 1
    #draw a single card and add to the deck
    #if draw 11 request if player wants to count as 1 or 11
    #if < 21 ask if the player wishes to draw or stay