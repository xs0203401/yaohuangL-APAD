import random
import gofish

def new_deck():
    rank=["2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K", "A"]
    suit=["spades", "hearts", "diamonds", "clubs"]
    deck = [(r, s) for r in rank for s in suit]
    return deck

if __name__ == "__main__":
    deck = new_deck()
    random.shuffle(deck)
    print(deck)
    hand = {}
    name = "Henry"
    for _ in range(len(deck)):
        gofish.drawCard(name, deck, hand)
