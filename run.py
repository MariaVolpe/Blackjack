import deck
import tkinter as tk

def main():
    root = tk.Tk()

    obj = deck.Deck(root)
    obj.setup_game()


    root.mainloop() 

if __name__ == "__main__":
    main()