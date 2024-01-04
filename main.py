import random
suits = ['♥', '♦', '♠', '♣'] # Feel free to use these symbols to represent the different suits.

class Card:
    def __init__(self, suit, rank):
        if suit == 'hearts':
            self.suit = suits[0]
        elif suit == 'spades':
            self.suit = suits[3]
        elif suit == 'clubs':
            self.suit = suits[2]
        else:
            self.suit = suits[1]
        self.rank = rank

    def __str__(self):
        list = [self.suit, self.rank]
        return "".join(list) # replace with an implementation

class CardCollection:
    def __init__(self):
        self.cards = []

    def add_card(self, card):
        self.cards = self.cards + [card]  # replace this with an implementation

    def draw_card(self):
        return self.cards.pop()  # replace this, must remove and return a Card instance from self.cards

    def make_deck(self):
        suits = ['hearts', 'spades', 'clubs', 'diamonds']
        nums = [2,3,4,5,6,7,8,9,10,'J','Q','K','A']
        x=0
        for x in suits:
            m=0
            for m in nums:
                self.cards = self.cards + [Card(x, m)] ## is this initialized into a separate variable orrrrrrrrrrr
        random.shuffle(self.cards)  # replace this, initialize self.cards with a fresh list of the 52 playing cards in random order.

    def value(self):
        sum = 0
        aces = 0
        for card in self.cards:
            if str.isnumeric(card.rank):
                sum += card.rank
            else:
                if card.rank == 'K':
                    sum+=10
                elif card.rank == 'Q':
                    sum+=10
                elif card.rank == 'J':
                    sum+=10
                else:
                    aces +=1

        for ace in aces:
            if sum <= 10:
                sum += 1
            else:
                sum += 11
        return sum  # replace this, must return an int representing the total value of cards in this collection.

def main():
    deck = CardCollection()
    deck.make_deck() # initialize a fresh deck
    player_hand = CardCollection()
    sum_p = 0
    sum_d = 0
    dealer_hand = CardCollection()
    on = True
    # player is dealt cards until players score reaches 21, exceeds 21, or the player decides to stay
    # if the player stays, the dealer draws cards until their sum is 17 or higher then,
    # dealers score reaches 21, exceeds 21, or the sum of their card values is equal, its a "push" and no one wins
    # or person w highest score wins
    # dealer must take another card if value is <17 or stay if value exceeds 17
    while on:
        c = deck.draw_card()
        player_hand.add_card(c)
        print("You drew", c)
        sum_p += player_hand.value()
        print("Sum:", sum_p)
        if sum_p == 21:
            print("You Won!!!!")
            on = False
        elif sum_p < 21:
            i = input("Do you want another card? (y/n)\n")
            if i == "n":
                on = False
        else:
            print("You lost :-(")
            on = False
    if sum_p < 21:
        deal = True
        while deal:
            if sum_d < 17:
                c = deck.draw_card()
                dealer_hand.add_card(c)
                print("I drew", c)
                sum_d += dealer_hand.value()
                print("My sum:", sum_d)
            if sum_d > 21:
                print("I lost :-(")
                deal = False
            elif sum_d == 21:
                print("I Win :-) !!!!")
                deal = False
            elif sum_d == sum_p:
                print("Push.... No winners here.")
            else:
                if sum_p < sum_d:
                    print("You lost :-(")
                    deal = False
                else:
                    print("I Win :-) !!!!")
                    deal = False



# complete the main method
if __name__ == "__main__":
    main()
