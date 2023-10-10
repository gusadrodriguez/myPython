import random
from blackJackFunctions import draw 
from blackJackFunctions import newDraw
from blackJackFunctions import compareHands
from blackJackFunctions import removeFromDeck
from blackJackFunctions import has22
from blackJackFunctions import replaceAce

cardDict = dict(
    spade2 = 2,
    spade3 = 3,
    spade4 = 4,
    spade5 = 5,
    spade6 = 6,
    spade7 = 7,
    spade8 = 8,
    spade9 = 9,
    spadeJack = 10,
    spadeQueen = 10,
    spadeKing = 10,
    spadeAce = 11,
    heart2 = 2,
    heart3 = 3,
    heart4 = 4,
    heart5 = 5,
    heart6 = 6,
    heart7 = 7,
    heart8 = 8,
    heart9 = 9,
    heartJack = 10,
    heartQueen = 10,
    heartKing = 10,
    heartAce = 11,
    club2 = 2,
    club3 = 3,
    club4 = 4,
    club5 = 5,
    club6 = 6,
    club7 = 7,
    club8 = 8,
    club9 = 9,
    clubJack = 10,
    clubQueen = 10,
    clubKing = 10,
    clubAce = 11,
    dia2 = 2,
    dia3 = 3,
    dia4 = 4,
    dia5 = 5,
    dia6 = 6,
    dia7 = 7,
    dia8 = 8,
    dia9 = 9,
    diaJack = 10,
    diaQueen = 10,
    diaKing = 10,
    diaAce = 11
)

#create a list of values from the dictionary
cardDictList = list(cardDict.values())

#select the first card from the decks .. may have matching cards but we will create a function to test that
playerHand = draw(2,cardDictList)

print(playerHand)

cardDictList = removeFromDeck(playerHand, cardDictList)

dealerHand = draw(2,cardDictList)

print(playerHand, dealerHand)

#test
playerHand = [11,11]

checkDoubleAce = has22(playerHand)
print(checkDoubleAce)
if checkDoubleAce == True:
    aceChoice = input("change ace value to 1? \yn y/n")
    if aceChoice == "y":
        replaceAce(playerHand)

print(playerHand)
#check players hand for 22 or above - give choice to replace card in deck with 1 for 11
#check dealers hand for 22 or above - run RNG for choice

#give choice to hit or fold
#share player total
#share dealer total
#determine winner



