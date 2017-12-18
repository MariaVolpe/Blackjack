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
    
    def PlayRound():
        #draw cards

        #show dealer cards, the 0th and 1st elements in cards_on_table
        #only one card is face up

        #show player cards, both face up

        #ask player for hit, stand, or forfeit
        dummy_var = 2
        #if hit, draw card
        #else do nothing

        #if bust, increment lose and return
        #else increment wins, ect
