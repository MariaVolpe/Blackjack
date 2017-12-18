import Cards
import Players

class Deck:
    cards_in_deck=[]
    cards_on_table=[]
    players=[]
    CPU_dealer = Players.Players('Dealer')

    #constructor
    #initializes 52 cards in the deck in use
    def __init__():
        rank_count = 1
        suit_count = 1

        for i in range(52):
            if rank_count >= 14
                rank_count = 1
            if suit_count >= 4
                suit_count = 1

            x = Cards.Cards(suit_count, rank_count)
            cards_in_deck.append(x)

            rank_count += rank_count
            suit_count += suit_count