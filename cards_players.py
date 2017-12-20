class Cards:

    suit = 0
    rank = 0
    in_deck = True

    def __init__(suit, rank):
        self.suit = suit
        self.rank = rank

    #print card
    def PrintCard(card):
        card_name = {14 : 'King', 13 : 'Queen', 12: 'Jack', 11: 'Ace'}
        suit_name = {4 : 'Spades', 3 : 'Hearts', 2: 'Clubs', 1: 'Diamonds'}
        if card.rank > 10:
            print("{} of {}").format(rank_name[card.rank], suit_name[card.suit])
        else:
            print("{} of {}").format(card.rank, suit_name[card.suit])

class Players:
    wins = 0
    losses = 0
    hand = []
    
    def __init__(name):
        self.name = name