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
                rank_count = 2
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
            print("Player {}'s cards: ").format(i+1)
            for j in range(2,5):
                self.PrintCard(cards_on_table[j+i])

        #ask player for hit or stand
        #todo forfeit ?
        #todo error checking on input(capital letters)
        for i in range(len(players)):
            hit_count = 0
            action = raw_input("Player {}'s turn. Hit or stand?").format(i+1)
            while action != "hit" or action != "stand":
                action = raw_input("Not a valid action. Hit or stand?").format(i+1)
            
            while action == "hit":
                hit_count += 1
                cards_on_table.append(self.DrawCard())
                total = self.TotalCards()
                if total > 21:
                    #bust
                    #increment lose and break
                    break
                if total == 21:
                    #blackjack
                    break
                action = raw_input("Hit again, or stand?").format(i+1)
                while action != "hit" or action != "stand":
                    action = raw_input("Not a valid action. Hit or stand?").format(i+1)

            #action here must be stand. todo
            if action == "stand":
                self.Stand()

            if total > 21:
                dummy_var = 0
                #bust
                #increment lose and return
            elif total == 21:
                #blackjack
                dummy_var = 0

    #print card at given index in deck
    def PrintCard(index):
        card_name = {14 : 'King', 13 : 'Queen', 12: 'Jack', 11: 'Ace'}
        suit_name = {4 : 'Hearts', 3 : 'Queen', 2: 'Jack', 1: 'Diamonds'}
        if cards_on_table[index].rank > 10
            print("{} of {}").format(rank_name[cards_on_table[index].rank], suit_name[cards_on_table[index].suit])
        else
            print("{} of {}").format(cards_on_table[index].rank, suit_name[cards_on_table[index].suit])

    #total the values of a player's hand
    def TotalCards():
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