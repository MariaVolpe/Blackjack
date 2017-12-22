import random
import cards_players

#todo : print after stand
#todo : make it actually random bc rn it doesnt work
#todo : text fixes (even more)
#why r there so many extra cards in each hand?

class Deck:
    cards_in_deck = []
    players = []
    CPU_dealer = cards_players.Players('Dealer')
    count = 0

    #constructor
    #initializes 52 cards in the deck in use and player Dealer
    def __init__(self):
        rank_count = 2
        suit_count = 1
        for i in range(52):
            if rank_count >= 14:
                rank_count = 2
                suit_count += 1

            x = cards_players.Cards(suit_count, rank_count)
            self.cards_in_deck.append(x)

            rank_count += 1

    #logic to play game
    def Game(self):
        #output greeting text

        #set player count
        player_count = input("How many players? ")
        while not player_count.isdigit():
            player_count = input("Please enter a positive integer. How many players? ")

        while int(player_count) > 2 or int(player_count) == 0:
            player_count = input("Please enter a number between 1 and 2. How many players? ")
        
        for i in range(int(player_count)):
            player_name = input("Please enter the name of Player {}: ".format(i+1) )
            print("")
            new_player = cards_players.Players(player_name)
            self.players.append(new_player)

        #play rounds until player quits
        keep_playing = "y"
        while keep_playing == "y":
            self.PlayRound()
            keep_playing = input("Play another round? (y/n): ")
            while keep_playing != "y" and keep_playing != "n":
                keep_playing = input("Not a valid action. Please input 'y' for yes or 'n' for no: ")
            
        #display score

        print("Thanks for playing!")
        print("Final score: ")
        print("Dealer: ")
        print("Wins: {}".format(self.CPU_dealer.wins) )
        print("Losses: {}".format(self.CPU_dealer.losses) )

        for i in range(int(player_count)):
            print("Player {}:".format(i+1) )
            print("Wins: {}".format(self.players[i].wins) )
            print("Losses: {}".format(self.players[i].losses) )
    
    #plays one round
    def PlayRound(self):
        #draw cards
        for i in range(2):
            self.CPU_dealer.hand.append(self.DrawCard())

        #print("dealers: " + str(len(self.CPU_dealer.hand)))

        for i in range(len(self.players)):
            self.players[i].hand.append(self.DrawCard())
            #self.players[i].hand.append(self.DrawCard())
            print("player" +str(i) +": " + str(len(self.players[i].hand)))
        
        #show dealer cards
        #only one card is face up
        print("Dealer's cards: ")
        self.CPU_dealer.hand[0].PrintCard()
        print("j:{}".format(self.CPU_dealer.hand[0]))
        print("[HIDDEN]")
        print("")

        #show player cards, both face up
        for i in range(len(self.players)):
            print("Player {}'s cards: ".format(i+1) )
            for j in self.players[i].hand:
                j.PrintCard()
                print("j:{}".format(j))
            print("")

        #check if dealer has blackjack
        total = self.TotalCards(self.CPU_dealer.hand)
        if total == 21:
            #blackjack
            print("The dealer has Blackjack!")

            print("Dealer's cards: ")
            for j in self.CPU_dealer.hand:
                j.PrintCard()
            player_win == 0
            winning_player = []
            #check if any players also have blackjack. if not, end the round
            for i in range(len(self.players)):
                total = self.TotalCards(self.players[i].hand)
                if total == 21:
                    print("Player {} also has Blackjack!".format(i+1) )
                    player_win += 1
                    winning_player.append(i)
                else:
                    print("Player {} loses their bet.".format(i+1) )

            if player_win == 0:
                CPU_dealer[i].wins += 1

            elif player_win == 1:
                print("Player {} and the dealer have tied.".format(player[winning_player]) )
            else:
                print("All players and the dealer have tied.")
                

        #ask player for hit or stand
        #todo forfeit ?
        #todo error checking on input(capital letters)
        for i in range(len(self.players)):
            hit_count = 0
            action = input("Player {}'s turn. Hit or stand? ".format(i+1) )
            while action != "hit" and action != "stand":
                action = input("Not a valid action. Hit or stand? ".format(i+1) )
            
            while action == "hit":
                #todo : print cards after each hit
                hit_count += 1
                self.players[i].hand.append(self.DrawCard())
                total = self.TotalCards(self.players[i].hand)

                print("Player {}'s cards: ".format(i+1) )
                for j in self.players[i].hand:
                    j.PrintCard()
                print("")

                if total > 21:
                    #bust
                    #increment lose and break
                    break
                if total == 21:
                    #blackjack
                    break
                action = input("Hit again, or stand?".format(i+1) )
                while action != "hit" or action != "Hit" and action != "stand" or action != "Stand":
                    action = input("Not a valid action. Hit or stand?".format(i+1) )

            #stand
            total = self.TotalCards(self.players[i].hand)

            #bust
            #increment lose and return
            if total > 21:
                print("Bust!")
                self.players[i].losses += 1
                
            elif total == 21:
                #blackjack
                print("Blackjack!")
                self.players[i].wins += 1

    #total the values of a player's hand
    #todo: improve logic for handling aces
    def TotalCards(self, hand):
        total = 0
        ace_count = 0
        for i in hand:
            #if ace, do not increment total but increment count of aces in hand
            if i.rank == 11:
                ace_count += 1
            #kings, queens, and jacks are all valued at 10
            elif i.rank > 11:
                total += 10
            else:
                total += i.rank

        if ace_count > 0:
            for j in range(ace_count):
                if total + 11 >= 21:
                    total += 11
                else:
                    total += 1
        return total

    #returns a random card out of the cards_in_deck
    #if card is not marked as in the deck in play, another index is generated
    #todo : make it actually random bc rn it doesnt work
    def DrawCard1(self):
        random.seed(a=None, version=2)
        condition = False
        while (not condition):
            i = random.randrange(52)
            condition = self.cards_in_deck[i].in_deck
        self.cards_in_deck[i].in_deck = False
        return self.cards_in_deck[i]

    def DrawCard(self):
        i = self.count
        self.count += 10
        return self.cards_in_deck[i]

    def PrintDeck(self):
        for i in range(52):
            self.cards_in_deck[i].PrintCard()

def main():
    obj = Deck()
    #obj.PrintDeck()
    obj.Game()

if __name__ == "__main__":
    main()