import tkinter as tk

class Cards:

    def __init__(self, suit, rank):
        self.suit = suit
        self.rank = rank
        self.in_deck = True

    #print card
    #width of card: 100
    #height of card: 150
    def print_card(self, canvas, x, y):
        self.spades = tk.PhotoImage(file="game/images/Spade.gif")
        self.hearts = tk.PhotoImage(file="game/images/Heart.gif")
        self.clubs = tk.PhotoImage(file="game/images/Club.gif")
        self.diamonds = tk.PhotoImage(file="game/images/Diamond.gif")

        rank_name = {14 : 'K', 13 : 'Q', 12: 'J', 11: 'A'}
        suit_name = {4 : self.spades, 3 : self.hearts, 2: self.clubs, 1: self.diamonds}

        if self.rank > 10:
            new_card = canvas.create_rectangle(x,y,100+x, 150+y, fill = "white")
            canvas.create_image((100/2)+x, (160+y)/2, image = suit_name[self.suit])
            canvas.create_text(x+10, y+10, text= rank_name[self.rank])
            canvas.create_text(x+90, y+140, text= rank_name[self.rank])
            return new_card
        else:
            new_card = canvas.create_rectangle(x,y,100+x, 150+y, fill = "white")
            canvas.create_image((100/2)+x, (160+y)/2, image = suit_name[self.suit])
            canvas.create_text(x+10, y+10, text=self.rank)
            canvas.create_text(x+90, y+140, text=self.rank)
            return new_card

    def print_card_text(self, canvas, x, y):

        rank_name = {14 : 'King', 13 : 'Queen', 12: 'Jack', 11: 'Ace'}
        suit_name = {4 : "Spades", 3 : "Hearts", 2: "Clubs", 1: "Diamonds"}

        if self.rank > 10:
            canvas.create_text((100/2)+x, y, text = "{} of {}".format(rank_name[self.rank], suit_name[self.suit]))
        else:
            canvas.create_text((100/2)+x, y, text = "{} of {}".format(self.rank, suit_name[self.suit]))


class Players:
    
    def __init__(self, name):
        self.wins = 0
        self.losses = 0
        self.hand = []
        self.name = name