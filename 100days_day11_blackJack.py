import random

card_dict = dict(
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

#check key value pairs
for key, value in my_dictionary.items():
    print(f"{key}: {value}")

cardDict_list = list(card_dict.values())


userHand = []
dealerHand = []

endGame = False

while endgame == False:
    for i in range(2):
        sel_card = random.choice(cardDict_list)
        for item in userHand:
            if item == sel_card:
                sel_card = random.choice(cardDict_list)
            else:
                userHand.append(sel_card)
        sel_card = random.choice(cardDict_list)
        for item in dealerHand:
            if item == sel_card:
                sel_card = random.choice(cardDict_list)
            else:
                dealerHand.append(sel_card)
    




