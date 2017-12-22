class Cards:

    def __init__(self, suit, rank):
        self.suit = suit
        self.rank = rank
        self.in_deck = True

    #print card
    def PrintCard(self):
        rank_name = {14 : 'King', 13 : 'Queen', 12: 'Jack', 11: 'Ace'}
        suit_name = {4 : 'Spades', 3 : 'Hearts', 2: 'Clubs', 1: 'Diamonds'}
        if self.rank > 10:
            print("{} of {}".format(rank_name[self.rank], suit_name[self.suit]))
        else:
            print("{} of {}".format(self.rank, suit_name[self.suit]))

class Players:
    
    def __init__(self, name):
        self.wins = 0
        self.losses = 0
        self.hand = []
        self.name = name