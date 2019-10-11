import random
import pyfiglet
import termcolor

ascii = pyfiglet.figlet_format('cards py 0.1', font='larry3d') 
print(termcolor.colored(ascii, color='red'))

class Card:
    
    def __init__(self, suit, value):
        self.suit = suit
        self.value = value

    def __repr__(self):
        return "{} of {}".format(self.value, self.suit)

class Deck:

    def __init__(self):
        self.cards = self._load_default_deck()

    def __repr__(self):
        return "Deck of {} cards".format(self.count())
    
    def count(self):
        return len(self.cards)

    def shuffle(self):
        random.shuffle(self.cards)

    def deal_card(self):
        return self._deal(1)[0]
    
    def deal_hand(self, number):
        return self._deal(number)
    
    def _deal(self, number):

        current_deck_count = self.count()

        if current_deck_count == 0:
            raise ValueError("All cards have been dealt")
        if number > current_deck_count:
            print("There are only {} cards in the deck!".format(current_deck_count))
            number = current_deck_count

        cards = []
        cards = self.cards[-number:]
        self.cards = self.cards[:-number]

        return cards
    
    def _load_default_deck(self):
        cards = []

        suits = ['Hearts', 'Spades', 'Diamonds', 'Cubs']
        values = ['A', '2','3','4','5','6','7','8','9','10','J','Q','K']

        for suit in suits:
            for value in values:
                cards.append(Card(suit, value))

        return cards

deck = Deck()
deck.shuffle()
print(deck)

print(termcolor.colored("Get a card...", color='red'))
card = deck.deal_card()
print(card)

print(termcolor.colored("Your hand...", color='red'))
hand = deck.deal_hand(5)
print(hand)