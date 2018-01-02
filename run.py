import tkinter as tk
from game import cards_players
from game import deck

def main():
    root = tk.Tk()

    obj = deck.Deck(root)
    obj.setup_game()


    root.mainloop() 

if __name__ == "__main__":
    main()