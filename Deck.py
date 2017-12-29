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

        self.play_round(1)

        keep_playing_frame = tk.Frame(self.master)
        keep_playing_frame.pack()
        #empty hands
        for i in range(self.num_players):
            self.CPU_dealer.hand = []
            self.players[i].hand = []
            
        keep_playing = tk.Label(keep_playing_frame,text="Play another round?")
        tk.Button(keep_playing_frame, text="Play Again", command=self.begin_game).pack()
        tk.Button(keep_playing_frame, text="Quit", command=self.end_game).pack()
        

    def end_game(self):
        #display score

        end_game_frame = tk.Frame(self.master)
        end_game_frame.grid()


        tk.Label(text="Thanks for playing!").pack()
        tk.Label(text="Final score: ").pack()
        tk.Label(text="Dealer:").pack()
        tk.Label(text="Wins: {}".format(self.CPU_dealer.wins) ).pack()
        tk.Label(text="Losses: {}".format(self.CPU_dealer.losses) ).pack()

        for i in range(int(player_count)):
            print("Player {}:".format(i+1) )
            print("Wins: {}".format(self.players[i].wins) )
            print("Losses: {}".format(self.players[i].losses) )
            print("")
    

    #plays one round
    def play_round(self, i):

        if self.num_players == 1:
            # dealer_cards_frame = tk.Frame(self.master, width="1000", height="350")
            # dealer_cards_frame.grid(rowspan=5)
            # dealer_cards_frame.grid_propagate(0)


            # player1_cards_frame = tk.Frame(self.master, width="1000", height="350")
            # player1_cards_frame.grid(row=5, rowspan=4)
            # player1_cards_frame.grid_propagate(0)

            # buttons1_frame = tk.Frame(self.master, width="1000", height="100")
            # buttons1_frame.grid(row=9, rowspan=1)
            # buttons1_frame.grid_propagate(0)

            dealer_cards_frame = tk.Frame(self.master, width="1000", height="350")
            dealer_cards_frame.pack(anchor="n")
 

            player1_cards_frame = tk.Frame(self.master, width="1000", height="350")
            player1_cards_frame.pack(anchor="center")

            buttons1_frame = tk.Frame(self.master, width="1000", height="100")
            buttons1_frame.pack(anchor="s")


        elif self.num_players == 2:
            # dealer_cards_frame = tk.Frame(self.master, width="1000", height="0")
            # dealer_cards_frame.grid_propagate(0)
            # dealer_cards_frame.grid(rowspan="1", sticky = "N")

            # player1_cards_frame = tk.Frame(self.master)
            # #width="1000", height="250")
            # player1_cards_frame.grid(row="4", rowspan="3", sticky = "N")
            # buttons1_frame = tk.Frame(self.master)
            # #width="1000", height="25")
            # buttons1_frame.grid(row="7", rowspan="1", sticky = "N")

            # player2_cards_frame = tk.Frame(self.master)
            # # width="1000", height="250")
            # player2_cards_frame.grid(row="8", rowspan="3", sticky = "N")
            # buttons2_frame = tk.Frame(self.master, width="1000", height="25")
            # buttons2_frame.grid(row="11",rowspan="1", sticky = "N")


            dealer_cards_frame = tk.Frame(self.master, width="1000", height="0")
            dealer_cards_frame.pack()

            player1_cards_frame = tk.Frame(self.master)
            #width="1000", height="250")
            player1_cards_frame.pack()
            buttons1_frame = tk.Frame(self.master)
            #width="1000", height="25")
            buttons1_frame.pack()

            player2_cards_frame = tk.Frame(self.master)
            # width="1000", height="250")
            player2_cards_frame.pack()
            buttons2_frame = tk.Frame(self.master, width="1000", height="25")
            buttons2_frame.pack()
            
        print(self.master.grid_size())
        
        
        #draw cards
        for i in range(2):
            self.CPU_dealer.hand.append(self.draw_card())

        for i in range(self.num_players):
            self.players[i].hand.append(self.draw_card())
            self.players[i].hand.append(self.draw_card())
        
        #show dealer cards
        #only one card is face up
        dealer_label = tk.Label(dealer_cards_frame, text="Dealer's cards:")
        dealer_label.pack()

#PUT THE HEIGHTS RIGHT AND USE VARIABLES TO SET THEM INSTEAD OF IF STATEMENTS IM SICK OF HTIS

        dealer_card_canvas = tk.Canvas(dealer_cards_frame, width="1000", height="250")
        dealer_card_canvas.pack()

        #returns rectangle that begins top left corner at (25, 25) and ends bottom right at (150,220)
        dealer_card_1 = self.CPU_dealer.hand[0].PrintCard(dealer_card_canvas,25,25)

        #30 pixels in between dealer_card_1 and hidden card
        #begins top left corner at (190, 25) and ends bottom right at (315, 220)
        dealer_card_hidden = dealer_card_canvas.create_rectangle(190, 25, 190+125, 25+195, fill="blue")


        if self.num_players == 1:
            #show player cards, both face up
            player1_label = tk.Label(player1_cards_frame, text="{}'s cards: ".format(self.players[0].name))
            player1_label.pack(side="top")
            
            player1_card_canvas = tk.Canvas(player1_cards_frame, width="1000", height="430")
            player1_card_canvas.pack(side="top")

            player1_card_recs = []
            xoffset = 0
            for i, j in enumerate(self.players[0].hand):
                player1_card_recs.append( j.PrintCard(player1_card_canvas,25+xoffset, 25) )
                    # width of a card (125) + number of pixels between cards (30)
                xoffset += 165
            
        #ask player for hit or stand
            tk.Label(buttons1_frame, text="{}'s turn.".format(self.players[i-1].name)).pack()
            stand_button1 = tk.Button(buttons1_frame, text="Stand", command=lambda: play_round2(i))
            stand_button1.pack()
            hit_button1 = tk.Button(buttons1_frame, text="Hit", command=lambda: self.hit(i))
            hit_button1.pack()

        if self.num_players == 2:

            player1_label = tk.Label(player1_cards_frame, text="{}'s cards: ".format(self.players[0].name))
            player1_label.pack(side="top")
            
            player1_card_canvas = tk.Canvas(player1_cards_frame, width="1000", height="350")
            player1_card_canvas.pack(side="top")

            player1_card_recs = []
            xoffset = 0
            for i, j in enumerate(self.players[0].hand):
                player1_card_recs.append( j.PrintCard(player1_card_canvas,25+xoffset, 25) )
                    # width of a card (125) + number of pixels between cards (30)
                xoffset += 165
            
        #ask player for hit or stand
            tk.Label(buttons1_frame, text="{}'s turn.".format(self.players[i-1].name)).pack()
            stand_button1 = tk.Button(buttons1_frame, text="Stand", command=lambda: play_round2(i))
            stand_button1.pack()
            hit_button1 = tk.Button(buttons1_frame, text="Hit", command=lambda: self.hit(i))
            hit_button1.pack()


            player2_label = tk.Label(player2_cards_frame, text="{}'s cards: ".format(self.players[0].name))
            player2_label.pack()
            
            player2_card_canvas = tk.Canvas(player2_cards_frame, width="1000", height="350")
            player2_card_canvas.pack()

            player2_card_recs = []
            xoffset = 0
            for i, j in enumerate(self.players[1].hand):
                player2_card_recs.append( j.PrintCard(player2_card_canvas,25+xoffset, 25) )
                # width of a card (125) + number of pixels between cards (30)
                xoffset += 165
            

        tk.Label(buttons2_frame, text="{}'s turn.".format(self.players[i-1].name)).pack()
        
        stand_button2 = tk.Button(buttons2_frame, text="Stand", command=lambda: play_round2(i))
        stand_button2.pack()
        hit_button2 = tk.Button(buttons2_frame, text="Hit", command=lambda: self.hit(i))
        hit_button2.pack()


        #check if dealer has blackjack
        total = self.total_cards(self.CPU_dealer.hand)
        if total == 21:
            self.dealer_blackjack()
            return
        

    def play_round2(i):
        if self.num_players == 2 and i !=2:
            self.play_round(2)
            

        print("")
        #stand
        total = self.total_cards(self.players[i-1].hand)

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
                self.players[i].wins += 1
            elif dealer_total > total:
                print("The dealer wins!")
                self.CPU_dealer.wins += 1
            else:
                print("It's a tie!")
                self.players[i].wins += 1
                self.CPU_dealer.wins += 1
            print("")
            

    # def end_round(self):
    #     dealer_cards_frame.destroy()
    #     player1_cards_frame.destroy()
    #     buttons1_frame.destroy()
    #     if self.num_players == 2:
    #         player2_cards_frame.destroy()
    #         buttons2_frame.destroy()
        
    
    def dealer_blackjack(self):
        print("The dealer has Blackjack!")

        print("Dealer's cards: ")
        #for j in self.CPU_dealer.hand:
            #j.PrintCard()
        player_win = 0
        winning_player = []
        #check if any players also have blackjack. if not, end the round
        for i in range(self.num_players):
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
                #for j in self.players[i].hand:
                    #j.PrintCard()
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