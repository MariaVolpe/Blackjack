import random
import cards_players

class Deck:
    cards_in_deck=[]
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
        for i in range(2):
            CPU_dealer.hand.append(self.DrawCard())

        for i in range(len(players)):
            for i in range(2):
                players[i].hand.append(self.DrawCard())
    
        #show dealer cards
        #only one card is face up
        print("Dealer's cards: ")
        cards_players.PrintCard(CPU_dealer.hand[0])
        print("[HIDDEN]")

        #show player cards, both face up
        for i in range(len(players)):
            print("Player {}'s cards: ").format(i+1)
            for j in range(2):
                cards_players.PrintCard(players[i].hand[j])

        #check if dealer has blackjack
        total = self.TotalCards(CPU_dealer.hand)
        if total == 21:
            #blackjack
            print("The dealer has Blackjack!")

            print("Dealer's cards: ")
            for j in range(2):
                cards_players.PrintCard(CPU_dealer.hand[j])
            player_win == 0
            winning_player = []
            #check if any players also have blackjack. if not, end the round
            for i in range(len(players)):
                total = self.TotalCards(players[i].hand)
                if total == 21:
                    print("Player {} also has Blackjack!").format(i+1)
                    player_win += 1
                    winning_player.append(i)
                else:
                    print("Player {} loses their bet.").format(i+1)

            if player_win == 0:
                CPU_dealer[i].wins += 1

            elif player_win == 1:
                print("Player {} and the dealer have tied.").format(player[winning_player])
            else:
                print("All players and the dealer have tied.")
                

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
                player[i].hand.append(self.DrawCard())
                total = self.TotalCards(players[i].hand)
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

            #stand
            total = self.TotalCards(players[i].hand)

            #bust
            #increment lose and return
            if total > 21:
                print("Bust!")
                player[i].losses += 1
                
            elif total == 21:
                #blackjack
                print("Blackjack!")
                player[i].wins += 1

    #total the values of a player's hand
    #todo: improve logic for handling aces
    def TotalCards(hand):
        total = 0
        ace_count = 0
        for i in hand:
            #if ace, do not increment total but increment count of aces in hand
            if hand[i].rank == 11:
                ace_count += 1
            #kings, queens, and jacks are all valued at 10
            elif hand[i].rank > 11:
                total += 10
            else:
                total += hand[i].rank

        if ace_count > 0:
            for j in range(ace_count):
                if total + 11 >= 21:
                    total += 11
                else:
                    total += 1
        return total

    #returns a random card out of the cards_in_deck
    #if card is not marked as in the deck in play, another index is generated
    def DrawCard():
        random.seed(a=None, version=2)
        condition = False
        while (not condition):
            i = random.range(52)
            condition = cards_in_deck[i].in_deck
        return cards_in_deck[i]