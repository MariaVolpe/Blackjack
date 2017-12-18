import Cards
import Players
import random

class Deck:
    cards_in_deck=[]
    cards_on_table=[]
    players=[]

    #constructor
    #initializes 52 cards in the deck in use and player Dealer
    def __init__():
        CPU_dealer = Players.Players('Dealer')

        rank_count = 1
        suit_count = 1
        for i in range(52):
            if rank_count >= 14:
                rank_count = 1
            if suit_count >= 4:
                suit_count = 1

            x = Cards.Cards(suit_count, rank_count)
            cards_in_deck.append(x)

            rank_count += rank_count
            suit_count += suit_count

    #logic to play game
    def Game():
        #output greeting text

        #set player count
        player_count = input("How many players? ")

        #todo: validate user input 
        
        for i in range(player_count):
            player_name = raw_input("Please enter the name of Player {} :").format(i+1)
            new_player = Player.Player(player_name)
            players.append(new_player)


        #play rounds until player quits
        keep_playing = "y"
        while keep_playing == "y":
            self.PlayRound()
            keep_playing = raw_input("Play another round? (y/n)")


        #display score

        print("Thanks for playing!")
        print("Final score:")
        print("Dealer: ")
        print("Wins: {}").format(CPU_dealer.wins)
        print("Losses: {}").format(CPU_dealer.losses)

        for i in range(player_count):
            print("Player {}: ").format(i+1)
            print("Wins: {}").format(players[i].wins)
            print("Losses: {}").format(players[i].losses)
    
    #plays one round
    def PlayRound():
        #draw cards
        for i in range((len(players)*2)+2):
            cards_on_table.append(self.DrawCard())
    
        #show dealer cards, the 0th and 1st elements in cards_on_table
        #only one card is face up
        print("Dealer's cards: ")
        self.PrintCard(cards_on_table[0])
        print("[HIDDEN]")

        #show player cards, both face up
        for i in range(len(players)):
            print("Player {}'s cards: ").format(i)
            for j in range(2,5):
                self.PrintCard(cards_on_table[j+i])

        #ask player for hit, stand, or forfeit
        #if hit, draw card
        #else do nothing

        #if bust, increment lose and return
        #else increment wins, ect

    def PrintCard(index):
        dummy_var = 0

    #returns the index of a random card out of the cards_in_deck
    #if card is not marked as in the deck in play, another index is generated
    def DrawCard():
        random.seed(a=None, version=2)
        condition = False
        while (not condition):
            i = random.range(52)
            condition = cards_on_table[i].in_deck
        return i
