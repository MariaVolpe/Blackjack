import random
import tkinter as tk
import game.cards_players

class Deck:
    #constructor
    #initializes 52 cards in the deck in use and player Dealer
    def __init__(self, master):
        self.cards_in_deck = []
        self.players = []
        self.CPU_dealer = game.cards_players.Players('Dealer')
        self.master = master
        self.num_players = 0
        
        self.master.title("Blackjack")
        self.master.minsize(width=1024, height=750)
        self.master.maxsize(width=1024, height=750)
        self.master.tk_setPalette(background='#ddffdd')

        self.display_card1 = game.cards_players.Cards(3, 13)
        self.display_card2 = game.cards_players.Cards(4, 11)

        #frame to hold all elements. can be destroyed to quickly clear screen
        self.container_frame = tk.Frame(self.master)
        self.container_frame.pack()

        self.card_count = 0

        rank_count = 2
        suit_count = 1
        for i in range(52):
            if rank_count > 14:
                rank_count = 2
                suit_count += 1

            x = game.cards_players.Cards(suit_count, rank_count)
            self.cards_in_deck.append(x)

            rank_count += 1

    #greets players and gets information about player number
    #calls start_set_player() when player selects an option
    def setup_game(self):
        self.container_frame.destroy()
        self.container_frame = tk.Frame(self.master)
        self.container_frame.pack()

        self.headerimage = tk.PhotoImage(file="game/images/header.gif")

        greet_screen = tk.Frame(self.container_frame)
        greet_screen.pack()
        
        header_canvas = tk.Canvas(greet_screen, width = 500, height = 250)
        header_canvas.pack(pady=(100,0))

        header_canvas.create_image(0, 0, image = self.headerimage, anchor = "nw")
    
        button_canvas = tk.Canvas(greet_screen, width = 350)
        button_canvas.pack()

        self.display_card1.print_card(button_canvas,15, 25)
        self.display_card2.print_card(button_canvas,250, 25)
        tk.Button(greet_screen, text="Rules", width = 7, command=self.rules).pack(side="right",  padx = (0, 85),)
        tk.Button(greet_screen, text="Play", width = 7, command=self.get_player_info).pack(side="left", padx = (95, 0))

        
    def rules(self):
        self.container_frame.destroy()
        self.container_frame = tk.Frame(self.master)
        self.container_frame.pack()

        rules_screen = tk.Frame(self.container_frame)
        rules_screen.pack()

        tk.Label(rules_screen, text = "Rules of Blackjack:").pack(anchor="w")

        tk.Label(rules_screen, text = "• Players compete against the dealer: ").pack(anchor="w")
        tk.Label(rules_screen, text = "         • A player's hand's worth is compared against the worth of the dealer's hand.").pack(anchor="w")
        tk.Label(rules_screen, text = "         • Whoever's hand is closest to 21, but not greater than 21, wins.").pack(anchor="w")
        tk.Label(rules_screen, text = "• If a player's hand is worth more than 21, the player \"busts\" and loses.").pack(anchor="w")
        tk.Label(rules_screen, text = "• If a player's hand is worth exactly 21, the player has Blackjack and wins unless the dealer also has Blackjack.").pack(anchor="w")
        tk.Label(rules_screen, text = "• Any time the dealer and a player have a hand worth the same but not over 21, there is a tie.").pack(anchor="w")
        tk.Label(rules_screen, text = "• Everyone in the game is initially dealt 2 cards.").pack(anchor="w")
        tk.Label(rules_screen, text = "         • The dealer's second card is dealt face down and at first, only the dealer is allowed to know its value.").pack(anchor="w")
        tk.Label(rules_screen, text = "         • All player cards are dealt face up.").pack(anchor="w")
        tk.Label(rules_screen, text = "         • Players can choose to \"hit\" and have another card added to their hand.").pack(anchor="w")
        tk.Label(rules_screen, text = "         • Players can hit as many times as they like until they bust.").pack(anchor="w")
        tk.Label(rules_screen, text = "         • Players can also choose to \"stand\", or to not have any cards added to their hand.").pack(anchor="w")
        tk.Label(rules_screen, text = "         • The dealer moves after all other players have moved, revealing the hidden card and then choosing hit or stand.").pack(anchor="w")
        tk.Label(rules_screen, text = "• Numbered cards are worth their face value.").pack(anchor="w")
        tk.Label(rules_screen, text = "• Jacks, Queens, and Kings are worth 10.").pack(anchor="w")
        tk.Label(rules_screen, text = "• An Ace is worth either 1 or 11, depending on which value is more advantageous.").pack(anchor="w")
        tk.Label(rules_screen, text = "• The deck reshuffles after 50% of it has been used.").pack(anchor="w")
        tk.Label(rules_screen, text = "• This game uses a S17 rule for the dealer:").pack(anchor="w")
        tk.Label(rules_screen, text = "         • The dealer will stand if their hand value is 17 or above.").pack(anchor="w")

        tk.Button(rules_screen, text="Back", command=self.setup_game).pack()

    def get_player_info(self):
        self.container_frame.destroy()
        self.container_frame = tk.Frame(self.master)
        self.container_frame.pack()
        
        player_info_frame = tk.Frame(self.container_frame)
        player_info_frame.pack()

        tk.Label(player_info_frame, text = "How many players?").pack(pady=(253,0), anchor="center")

        player_count = tk.IntVar(None, 1)
        tk.Radiobutton(player_info_frame, text="1", variable=player_count, value=1).pack(anchor="w")
        tk.Radiobutton(player_info_frame, text="2", variable=player_count, value=2).pack(anchor="w")
        
        tk.Button(player_info_frame, text="OK!", command=lambda: self.start_set_player(player_count)).pack()

    #gets player names from user(s)
    #call end_set_player() when finished
    def start_set_player(self, player_count):
        self.container_frame.destroy()
        self.container_frame = tk.Frame(self.master)
        self.container_frame.pack()

        self.num_players = player_count.get()

        set_player = tk.Frame(self.container_frame)
        set_player.pack()
        e = []
        labels = []

        for i in range(self.num_players):
            labels.append( tk.Label(set_player, text="Player {} Name: ".format(i+1)) )
            e.append( tk.Entry(set_player) )
            e[i].config(background = "white")

        labels[0].pack(pady=(253,0))
        e[0].insert(0,"Player {}".format(1))
        e[0].pack()
        if self.num_players == 2:
            labels[1].pack()
            e[1].insert(0,"Player {}".format(2))
            e[1].pack()

        tk.Button(set_player, text="OK!", command=lambda: self.end_set_player(set_player, e)).pack()


    #intializes vector of Player objects with user inputted names from start_set_player()
    #calls begin_game() when finished
    def end_set_player(self, set_player, e):
        for i in range(self.num_players):
            new_player = game.cards_players.Players(e[i].get())
            self.players.append(new_player)
        set_player.destroy()
        self.play_round(1)
    

    #begins to play one round
    #for a two player game, if turn == 1 it is player 1's turn
    #if turn == 2 it is player 2's turn
    def play_round(self, turn):

        self.container_frame.destroy()
        self.container_frame = tk.Frame(self.master)
        self.container_frame.pack()

        self.dealer_cards_frame = tk.Frame(self.container_frame)
        self.dealer_cards_frame.pack()

        self.player1_cards_frame = tk.Frame(self.container_frame)
        self.player1_cards_frame.pack()

        self.buttons1_frame = tk.Frame(self.container_frame)
        self.buttons1_frame.pack()

        canvas_height = 250

        if self.num_players == 2:
            self.player2_cards_frame = tk.Frame(self.container_frame)
            self.player2_cards_frame.pack()
            
            self.buttons2_frame = tk.Frame(self.container_frame)
            self.buttons2_frame.pack(side="bottom")

            canvas_height = 180
        
        
        #draw cards
        for i in range(2):
            self.CPU_dealer.hand.append(self.draw_card())

        for i in range(self.num_players):
            self.players[i].hand.append(self.draw_card())
            self.players[i].hand.append(self.draw_card())
        
        #show dealer cards
        #only one card is face up
        dealer_label = tk.Label(self.dealer_cards_frame, text="Dealer's cards:")
        dealer_label.pack(anchor="w", pady=(10,0))

        self.dealer_card_canvas = tk.Canvas(self.dealer_cards_frame, width="1000", height=canvas_height)
        self.dealer_card_canvas.pack()

        self.dealer_card_1 = self.CPU_dealer.hand[0].print_card(self.dealer_card_canvas,25,25)

        #30 pixels in between dealer_card_1 and hidden card
        #print dealer card, which is shown face down
        #card begins at (180, 25) and ends at (280, 175)
        self.dealer_card_hidden = self.dealer_card_canvas.create_rectangle(180, 25, 180+100, 25+150, fill="blue")
        
        #draw back of card
        self.lines=[]
        self.lines.append(self.dealer_card_canvas.create_line(180+75, 25, 180+100, 25+(75/2), fill="light blue"))
        #self.dealer_card_canvas.create_line(180, 25, 180+100, 25+150, fill="light blue")
        self.lines.append(self.dealer_card_canvas.create_line(180+25, 25, 180+100, 25+75+(75/2), fill="light blue"))
        self.lines.append(self.dealer_card_canvas.create_line(180, 25+75, 180+50, 25+150, fill="light blue"))
        self.lines.append(self.dealer_card_canvas.create_line(180+50, 25, 180+100, 25+75, fill="light blue"))
        self.lines.append(self.dealer_card_canvas.create_line(180, 25+110, 180+25, 25+150, fill="light blue"))

        #show player 1 cards
        player1_label = tk.Label(self.player1_cards_frame, text="{}'s cards: ".format(self.players[0].name))
        player1_label.pack(side="top",anchor="w")
            
        self.player1_card_canvas = tk.Canvas(self.player1_cards_frame, width="1000", height=canvas_height)
        self.player1_card_canvas.pack(side="top")

        player1_card_recs = []
        xoffset = 0
        for i, j in enumerate(self.players[0].hand):
            player1_card_recs.append( j.print_card(self.player1_card_canvas,25+xoffset, 25) )
                # width of a card (125) + number of pixels between cards (20)
            xoffset += 155

        if self.num_players == 2:

            player2_label = tk.Label(self.player2_cards_frame, text="{}'s cards: ".format(self.players[1].name))
            player2_label.pack(anchor="w")
            
            self.player2_card_canvas = tk.Canvas(self.player2_cards_frame, width="1000", height=canvas_height)
            self.player2_card_canvas.pack()

            player2_card_recs = []
            xoffset = 0
            for i, j in enumerate(self.players[1].hand):
                player2_card_recs.append( j.print_card(self.player2_card_canvas,25+xoffset, 25) )
                # width of a card (125) + number of pixels between cards (20)
                xoffset += 155
        
            self.take_turn(1)
        else:
            self.take_turn_p1()

    #begin turn for one player
    def take_turn_p1(self):
        total = self.total_cards(self.CPU_dealer.hand)
        if total == 21:
            self.dealer_blackjack()
            return
        #ask player for hit or stand
        self.turn_label = tk.Label(self.buttons1_frame, text="{}'s turn.".format(self.players[0].name))
        self.turn_label.pack()
        self.stand_button = tk.Button(self.buttons1_frame, text="Stand", command=self.end_round)
        self.stand_button.pack(side="right")
        self.hit_button = tk.Button(self.buttons1_frame, text="Hit", command=self.hit_p1)
        self.hit_button.pack(side="left")


    #begin turn for 2 players
    def take_turn(self, turn):
        #check if dealer has blackjack
        total = self.total_cards(self.CPU_dealer.hand)
        if total == 21:
            self.dealer_blackjack()
            return

        if turn == 1:
            #ask player for hit or stand
            self.turn_label = tk.Label(self.buttons1_frame, text="{}'s turn:".format(self.players[turn-1].name))
            self.turn_label.pack(anchor = "w")
            self.stand_button = tk.Button(self.buttons1_frame, text="Stand", command=lambda: self.take_turn(turn+1))
            self.stand_button.pack(side="right")
            self.hit_button = tk.Button(self.buttons1_frame, text="Hit", command=lambda: self.hit(turn))
            self.hit_button.pack(side="left")

            self.waitlabel = tk.Label(self.buttons2_frame, text="[WAITING]")
            self.waitlabel.pack(pady=(0,50))

        if turn == 2:
            self.waitlabel.destroy()
            self.stand_button.destroy()
            self.hit_button.destroy()
            self.turn_label.destroy()

            self.turn_label = tk.Label(self.buttons2_frame, text="{}'s turn:".format(self.players[turn-1].name))
            self.turn_label.pack()
            self.stand_button = tk.Button(self.buttons2_frame, text="Stand", command=self.end_round)
            self.stand_button.pack(side="right")
            self.hit_button = tk.Button(self.buttons2_frame, text="Hit", command=lambda: self.hit(turn) )
            self.hit_button.pack(side="left")


    #after players are done making decisions, calculate scores and if they won or lost
    def end_round(self):
        self.stand_button.destroy()
        self.hit_button.destroy()
        self.turn_label.destroy()

        #show hidden dealer card
        xoffset = 2*155
        
        self.dealer_card_canvas.delete(self.dealer_card_hidden)
        for i in self.lines:
            self.dealer_card_canvas.delete(i)
        self.dealer_card_hidden = self.CPU_dealer.hand[1].print_card(self.dealer_card_canvas,180,25)

        #dealer takes hits until dealer's hand reaches a total of 17
        dealer_total = self.total_cards(self.CPU_dealer.hand)
        while dealer_total < 17:
            self.CPU_dealer.hand.append(self.draw_card())
            self.CPU_dealer.hand[-1].print_card(self.dealer_card_canvas,25+xoffset, 25)
            xoffset += 155
            dealer_total = self.total_cards(self.CPU_dealer.hand)
        self.dealer_card_canvas.create_text(xoffset+30, 25+145, text="Hand value: {}".format(dealer_total))

        p1_total = self.total_cards(self.players[0].hand)
        xoffset = 155*(len(self.players[0].hand))
        self.player1_card_canvas.create_text(xoffset+30, 25+145, text="Hand value: {}".format(p1_total))

        if self.num_players == 2:
            p2_total = self.total_cards(self.players[1].hand)
            xoffset = 155*(len(self.players[1].hand))
            self.player2_card_canvas.create_text(xoffset+30, 25+145, text="Hand value: {}".format(p2_total))

        if dealer_total > 21:
            dealer_total = 0
            xoffset = 155*(len(self.CPU_dealer.hand))
            self.dealer_card_canvas.create_text(xoffset+100, 25+145, text=" - BUST")

        xoffset = 155*(len(self.players[0].hand))
        #if p1 busts
        if p1_total > 21:
            self.players[0].losses += 1                
            self.player1_card_canvas.create_text(xoffset+100, 25+145, text="- LOSE")
        #dealer wins against p1
        elif dealer_total > p1_total:
            self.players[0].losses += 1              
            self.player1_card_canvas.create_text(xoffset+100, 25+145, text="- LOSE")
        elif dealer_total == p1_total:
            self.player1_card_canvas.create_text(xoffset+100, 25+145, text="- TIE")
        else:
            self.players[0].wins += 1
            self.player1_card_canvas.create_text(xoffset+100, 25+145, text="- WIN")

        if self.num_players == 2:
            xoffset = 155*(len(self.players[1].hand))
            #if p2 busts
            if p2_total > 21:
                self.players[1].losses += 1
                self.player2_card_canvas.create_text(xoffset+100, 25+145, text="- LOSE")
            #dealer wins against p2
            elif dealer_total > p2_total:
                self.players[1].losses += 1
                self.player2_card_canvas.create_text(xoffset+100, 25+145, text="- LOSE")
            elif dealer_total == p2_total:
                self.player2_card_canvas.create_text(xoffset+100, 25+145, text="- TIE")
            else:
                self.players[1].wins += 1
                self.player2_card_canvas.create_text(xoffset+100, 25+145, text="- WIN")

        next_button = tk.Button(self.container_frame, text="-->", font=("TkDefaultFont", 25), command =self.end_game)
        next_button.pack(side="right")


    #after a round is finished, resets player hands and asks if user will keep playing
    #if player chooses to quit, exit_screen()
    #if player chooses to continue playing, call play_round() set to turn 1
    def end_game(self):

        #clear the screen
        self.container_frame.destroy()

        self.container_frame = tk.Frame(self.master)
        self.container_frame.pack()

        keep_playing_frame = tk.Frame(self.container_frame)
        keep_playing_frame.pack()
        #empty hands
        for i in range(self.num_players):
            self.CPU_dealer.hand = []
            self.players[i].hand = []
            
        keep_playing = tk.Label(keep_playing_frame,text="Play another round?", font=("TkDefaultFont", 35))
        keep_playing.pack(anchor="center", pady = (150,30))
        
        button_canvas = tk.Canvas(keep_playing_frame, width = 500)
        button_canvas.pack()

        self.display_card1.print_card(button_canvas,5, 25)
        self.display_card2.print_card(button_canvas,390, 25)
        tk.Button(keep_playing_frame, text="Play Again", width = 7, command=lambda: self.play_round(1)).pack(side="left",  padx = (10, 0),)
        tk.Button(keep_playing_frame, text="Quit", width = 7, command=self.exit_screen).pack(side="right", padx = (0, 20))
        
    #ends game and displays scores
    def exit_screen(self):
        
        self.container_frame.destroy()

        exit_screen = tk.Frame(self.master)
        exit_screen.pack()

        #display scores
        tk.Label(exit_screen, text="Thanks for playing!").pack(pady=(0,50))
        tk.Label(exit_screen, text="Final score: ").pack()

        for i in range(self.num_players):
            tk.Label(exit_screen, text="Player {}:".format(i+1)).pack()
            tk.Label(exit_screen, text="Wins: {}".format(self.players[i].wins) ).pack()
            tk.Label(exit_screen, text="Losses: {}".format(self.players[i].losses) ).pack(pady=(0,20))

        #quit button
        tk.Button(exit_screen, text="Quit", command=self.master.destroy).pack()
        
    
    def dealer_blackjack(self):

        self.dealer_card_canvas.delete(self.dealer_card_hidden)
        for i in self.lines:
            self.dealer_card_canvas.delete(i)
        self.dealer_card_hidden = self.CPU_dealer.hand[1].print_card(self.dealer_card_canvas,180,25)

        xoffset = 155*(len(self.CPU_dealer.hand))
        self.dealer_card_canvas.create_text(xoffset+30, 25+145, text="- Blackjack!")
        
        #check if any players also have blackjack. if not, end the round
        for i in range(self.num_players):
            total = self.total_cards(self.players[i].hand)
            xoffset = 155*(len(self.players[i].hand))
            if i == 0:
                self.player1_card_canvas.create_text(xoffset+30, 25+145, text="Hand value: {}".format(total))
                if total == 21:
                    self.player1_card_canvas.create_text(xoffset+100, 25+145, text="- TIE")
                else:
                    self.player1_card_canvas.create_text(xoffset+100, 25+145, text="- LOSE")
            else:
                self.player2_card_canvas.create_text(xoffset+30, 25+145, text="Hand value: {}".format(total))
                if total == 21:
                    self.player2_card_canvas.create_text(xoffset+100, 25+145, text="- TIE")
                else:
                    self.player2_card_canvas.create_text(xoffset+100, 25+145, text="- LOSE")


        next_button = tk.Button(self.container_frame, text="-->", font=("TkDefaultFont", 25), command =self.end_game)
        next_button.pack(side="right")

#####
# utility functions 
#####

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
    #if more than 26 cards (50% of deck) have been drawn, reset the deck
    def draw_card(self):
        random.seed(a=None, version=2)
        condition = False
        while (not condition):
            i = random.randrange(52)
            condition = self.cards_in_deck[i].in_deck
        self.cards_in_deck[i].in_deck = False

        self.card_count += 1
        if self.card_count > 26:
            self.reshuffle()

        return self.cards_in_deck[i]

    #reshuffle deck in use by flagging all cards as being in the deck
    def reshuffle(self):
        for i in self.cards_in_deck:
            i.in_deck = True

    def hit_p1(self):
        xoffset = 155*len(self.players[0].hand)
        self.players[0].hand.append(self.draw_card())
        total = self.total_cards(self.players[0].hand)
            
        #print new card
        self.players[0].hand[-1].print_card(self.player1_card_canvas,25+xoffset, 25)
    
        self.stand_button.destroy()
        self.hit_button.destroy()
        
        #stop player from choosing to take another hit if player busts or has blackjack
        if total > 21:
            self.turn_label.destroy()
            statuslabel = tk.Label(self.buttons1_frame, text="BUST")
            statuslabel.pack()
            self.end_round()
           
        elif total == 21:
            self.turn_label.destroy()
            statuslabel = tk.Label(self.buttons1_frame, text="Blackjack!")
            statuslabel.pack()
            self.end_round()
            
        else:
            self.stand_button = tk.Button(self.buttons1_frame, text="Stand", command=self.end_round)
            self.stand_button.pack(side="right")
            self.hit_button = tk.Button(self.buttons1_frame, text="Hit", command=self.hit_p1)
            self.hit_button.pack(side="left")



    #logic for if a player chooses a hit
    #draw a card and add it to player's hand
    #allow player to continue choosing to hit until player busts
    def hit(self,turn):
        xoffset = 155*len(self.players[turn-1].hand)
        self.players[turn-1].hand.append(self.draw_card())
        total = self.total_cards(self.players[turn-1].hand)
            
        #print new card
        if turn == 1:
            self.players[0].hand[-1].print_card(self.player1_card_canvas,25+xoffset, 25)
        else:
            self.players[1].hand[-1].print_card(self.player2_card_canvas,25+xoffset, 25)

        self.stand_button.destroy()
        self.hit_button.destroy()
        
        #stop player from choosing to take another hit if player busts or has blackjack
        if total > 21:
            self.turn_label.destroy()
            if turn == 1:
                statuslabel = tk.Label(self.buttons1_frame, text="BUST")
                statuslabel.pack()
                self.take_turn(turn+1)
            else:
                statuslabel = tk.Label(self.buttons2_frame, text="BUST")
                statuslabel.pack()
                self.end_round()
        elif total == 21:
            self.turn_label.destroy()
            if turn == 1:
                statuslabel = tk.Label(self.buttons1_frame, text="Blackjack!")
                statuslabel.pack()
                self.take_turn(turn+1)
            else:
                statuslabel = tk.Label(self.buttons2_frame, text="Blackjack!")
                statuslabel.pack()
                self.end_round()
        else:
            if turn == 1:
                self.stand_button = tk.Button(self.buttons1_frame, text="Stand", command=lambda: self.take_turn(turn+1))
                self.stand_button.pack(side="right")
                self.hit_button = tk.Button(self.buttons1_frame, text="Hit", command=lambda: self.hit(turn))
                self.hit_button.pack(side="left")
            else:
                self.stand_button = tk.Button(self.buttons2_frame, text="Stand", command=self.end_round)
                self.stand_button.pack(side="right")
                self.hit_button = tk.Button(self.buttons2_frame, text="Hit", command=lambda: self.hit(turn))
                self.hit_button.pack(side="left")
