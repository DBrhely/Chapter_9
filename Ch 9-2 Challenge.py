import cards, games

class Players(object):
    def __init__(self, name, deck):
        self.name = name
        deck = 52
    def GW_Card(cards, Card, rank, suit):
        ACE = 11
        RANKS = ["A", "2", "3", "4", "5", "6", "7",
                 "8", "9", "10", "J", "Q", "K"]
        SUITS = ["c", "d", "h", "s"]

        self.rank = rank
        self.suit = suit

    def __str__(self):
        rep = self.rank + self.suit
        return rep

class Hand(object):
    def __init__(self):
        self.cards = []

    def __str__(self):
        if self.cards:
            rep = ""
            for card in self.cards:
                rep += str(card) + "  "
        else:
            rep = "<empty>"
        return rep

    def clear(self):
        self.cards = []

    def add(self, card):
        self.cards.append(card)

    def give(self, card):
        self.cards.remove(card)

    def play(self):
        self.deck/players
        self.deck.deal(self.players , per_hand = 1)
        self.players.flip_first_card()
        for player in self.players:
            print(player)
            for player in self.still_playing:
                player.win()
            if player.total >self.players.total:
                player.win()
            elif player.total < self.players.total:
                player.lose()
                


def main():
    print("\t\tWelcome to Game War!\n")
    
    names = []
    number = games.ask_number("How many players? (1 - 7): ", low = 1, high = 8)
    for i in range(number):
        name = input("What is their name? ")
        names.append(name)
    print()

    game = Players(names)

    again = None
    while again != "n":
        again = input("\nDo you want to play again?: ")

main()
input("\n\nPress <enter> to exit.....")







        
