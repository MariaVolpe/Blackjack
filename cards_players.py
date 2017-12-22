class Cards:

    suit = 0
    rank = 0
    in_deck = True

    def __init__(self, suit, rank):
        self.suit = suit
        self.rank = rank

    #print card
    def PrintCard(self):
        rank_name = {14 : 'Kinag', 13 : 'Queen', 12: 'Jack', 11: 'Ace'}
        suit_name = {4 : 'Spades', 3 : 'Hearts', 2: 'Clubs', 1: 'Diamonds'}
        if self.rank > 10:
            print("{} of {}".format(rank_name[self.rank], suit_name[self.suit]))
        else:
            print("{} of {}".format(self.rank, suit_name[self.suit]))

class Players:
    wins = 0
    losses = 0
    hand = []
    
    def __init__(self, name):
        self.name = name