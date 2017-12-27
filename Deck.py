import random
import cards_players
import tkinter as tk


class Deck:
    #constructor
    #initializes 52 cards in the deck in use and player Dealer
    def __init__(self, master):
        self.cards_in_deck = []
        self.players = []
        self.CPU_dealer = cards_players.Players('Dealer')
        self.master = master
        self.num_players = 0

        self.master.minsize(width=1000, height=800)

        rank_count = 2
        suit_count = 1
        for i in range(52):
            if rank_count > 14:
                rank_count = 2
                suit_count += 1

            x = cards_players.Cards(suit_count, rank_count)
            self.cards_in_deck.append(x)

            rank_count += 1

    #logic to play game
    def setup_game(self):

        greet_screen = tk.Frame(self.master)
        greet_screen.pack()

        greetings = tk.Label(greet_screen, text = "Welcome to Blackjack!")
        greetings.pack(side="top")

        tk.Label(greet_screen, text = "How many players?").pack(side="top")

        player_count = tk.IntVar()
        tk.Radiobutton(greet_screen, text="1", variable=player_count, value=1).pack(anchor="w")
        tk.Radiobutton(greet_screen, text="2", variable=player_count, value=2).pack(anchor="w")
        
        tk.Button(greet_screen, text="OK!", command=lambda: self.start_set_player(greet_screen, player_count)).pack()
        
    def start_set_player(self, greet_screen, player_count):
        greet_screen.destroy()
        self.num_players = player_count.get()

        set_player = tk.Frame(self.master)
        set_player.pack()
        e = []
        labels = []

        for i in range(self.num_players):
            labels.append( tk.Label(set_player, text="Player {} Name: ".format(i+1)) )
            e.append( tk.Entry(set_player) )

        for i in range(self.num_players):
            labels[i].pack()
            e[i].pack()

        tk.Button(set_player, text="OK!", command=lambda: self.end_set_player(set_player, e)).pack()

    def end_set_player(self, set_player, e):
        for i in range(self.num_players):
            new_player = cards_players.Players(e[i].get())
            self.players.append(new_player)
        set_player.destroy()
        self.begin_game()


    def begin_game(self):

        dealerCards = tk.Frame(self.master, width="700", height="700")
        dealerCards.pack(side="top")
        
        buttonsFrame = tk.Frame(self.master)
        buttonsFrame.pack(side="bottom")

        #play rounds until player quits
        keep_playing = 1
        while keep_playing == 1:
            self.play_round()
            for i in range(len(self.players)):
                self.CPU_dealer.hand = []
                self.players[i].hand = []
            
            keep_playing = input("Play another round? (y/n): ")
            keep_playing.lower()
            while keep_playing != "y" and keep_playing != "n":
                keep_playing = input("Not a valid action. Please input 'y' for yes or 'n' for no: ")
                keep_playing.lower()
            
        #display score
        print("Thanks for playing!")
        print("Final score: ")
        print("Dealer: ")
        print("Wins: {}".format(self.CPU_dealer.wins) )
        print("Losses: {}".format(self.CPU_dealer.losses) )
        print("")

        for i in range(int(player_count)):
            print("Player {}:".format(i+1) )
            print("Wins: {}".format(self.players[i].wins) )
            print("Losses: {}".format(self.players[i].losses) )
            print("")
    
    #plays one round
    def play_round(self):
        print("")
        #draw cards
        for i in range(2):
            self.CPU_dealer.hand.append(self.draw_card())

        #print("dealers: " + str(len(self.CPU_dealer.hand)))

        for i in range(len(self.players)):
            self.players[i].hand.append(self.draw_card())
            self.players[i].hand.append(self.draw_card())
        
        #show dealer cards
        #only one card is face up
        print("Dealer's cards: ")
        self.CPU_dealer.hand[0].PrintCard()
        print("[HIDDEN]")
        print("")

        #show player cards, both face up
        for i in range(len(self.players)):
            print("Player {}'s cards: ".format(i+1) )
            for j in self.players[i].hand:
                j.PrintCard()
            print("")

        #check if dealer has blackjack
        total = self.total_cards(self.CPU_dealer.hand)
        if total == 21:
            self.dealer_blackjack()
            return
                
        #ask player for hit or stand
        for i in range(len(self.players)):
            action = input("Player {}'s turn. Hit or stand? ".format(i+1) )
            action.lower()
            while action != "hit" and action != "stand":
                action = input("Not a valid action. Hit or stand? ".format(i+1) )
                action.lower()
            print("")
            
            self.hit(i)
            
            print("")
            #stand
            total = self.total_cards(self.players[i].hand)

            if total > 21:
                print("Bust!")
                self.players[i].losses += 1
                
            elif total == 21:
                #blackjack
                print("Player {} has Blackjack!".format(i+1) )
                self.players[i].wins += 1

            else:
                total = self.total_cards(self.players[i].hand)
                dealer_total = self.total_cards(self.CPU_dealer.hand)
                print("Player {}'s hand adds up to {}.".format(i+1, total) )
                print("The dealer's hand adds up to {}.".format(dealer_total) )
                if dealer_total < total:
                    print("Player {} wins!".format(i+1) )
                    self.player[i].wins += 1
                elif dealer_total > total:
                    print("The dealer wins!")
                    self.CPU_dealer.wins += 1
                else:
                    print("It's a tie!")
                    self.player[i].wins += 1
                    self.CPU_dealer.wins += 1

            print("")

    def dealer_blackjack(self):
        print("The dealer has Blackjack!")

        print("Dealer's cards: ")
        for j in self.CPU_dealer.hand:
            j.PrintCard()
        player_win = 0
        winning_player = []
        #check if any players also have blackjack. if not, end the round
        for i in range(len(self.players)):
            total = self.total_cards(self.players[i].hand)
            if total == 21:
                print("Player {} also has Blackjack!".format(i+1) )
                player_win += 1
                winning_player.append(i)
            else:
                print("Player {} loses their bet.".format(i+1) )

            if player_win == 0:
                self.CPU_dealer.wins += 1

            elif player_win == 1:
                print("Player {} and the dealer have tied.".format(player[winning_player]) )
            else:
                print("All players and the dealer have tied.")

            print("")

    #total the values of a player's hand
    def total_cards(self, hand):
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
                if (total + 11) <= 21:
                    total += 11
                else:
                    total += 1
        return total

    #returns a random card out of the cards_in_deck
    #if card is not marked as in the deck in play, another index is generated
    def draw_card(self):
        random.seed(a=None, version=2)
        condition = False
        while (not condition):
            i = random.randrange(52)
            condition = self.cards_in_deck[i].in_deck
        self.cards_in_deck[i].in_deck = False
        return self.cards_in_deck[i]

    #print suit and rank of entire deck
    def print_deck(self):
        for i in range(52):
            self.cards_in_deck[i].PrintCard()


    def hit(self, i):
        action = "hit"
        hit_count = 0
        while action == "hit":
                hit_count += 1
                self.players[i].hand.append(self.draw_card())
                total = self.total_cards(self.players[i].hand)

                print("Player {}'s cards: ".format(i+1) )
                for j in self.players[i].hand:
                    j.PrintCard()
                print("")

                if total > 21:
                    return
                if total == 21:
                    return

                action = input("Hit again, or stand?".format(i+1) )
                action.lower()
                while action != "hit" and action != "stand":
                    action = input("Not a valid action. Hit or stand?".format(i+1) )
                    action.lower()

def main():
    root = tk.Tk()

    obj = Deck(root)
    #obj.print_deck()
    obj.setup_game()


    root.mainloop() 

if __name__ == "__main__":
    main()