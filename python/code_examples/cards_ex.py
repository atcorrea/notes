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
        for _ in range(number):
            card = self.cards[-1]
            self.cards.remove(card)
            cards.append(card)

        return cards
    
    def _load_default_deck(self):
        cards = []

        #Hearts        
        cards.append(Card("Hearts", "A"))
        cards.append(Card("Hearts", "2"))
        cards.append(Card("Hearts", "3"))
        cards.append(Card("Hearts", "4"))
        cards.append(Card("Hearts", "5"))
        cards.append(Card("Hearts", "6"))
        cards.append(Card("Hearts", "7"))
        cards.append(Card("Hearts", "8"))
        cards.append(Card("Hearts", "9"))
        cards.append(Card("Hearts", "10"))
        cards.append(Card("Hearts", "J"))
        cards.append(Card("Hearts", "Q"))
        cards.append(Card("Hearts", "K"))

        #Spades
        cards.append(Card("Spades", "A"))
        cards.append(Card("Spades", "2"))
        cards.append(Card("Spades", "3"))
        cards.append(Card("Spades", "4"))
        cards.append(Card("Spades", "5"))
        cards.append(Card("Spades", "6"))
        cards.append(Card("Spades", "7"))
        cards.append(Card("Spades", "8"))
        cards.append(Card("Spades", "9"))
        cards.append(Card("Spades", "10"))
        cards.append(Card("Spades", "J"))
        cards.append(Card("Spades", "Q"))
        cards.append(Card("Spades", "K"))

        #Cubs
        cards.append(Card("Cubs", "A"))
        cards.append(Card("Cubs", "2"))
        cards.append(Card("Cubs", "3"))
        cards.append(Card("Cubs", "4"))
        cards.append(Card("Cubs", "5"))
        cards.append(Card("Cubs", "6"))
        cards.append(Card("Cubs", "7"))
        cards.append(Card("Cubs", "8"))
        cards.append(Card("Cubs", "9"))
        cards.append(Card("Cubs", "10"))
        cards.append(Card("Cubs", "J"))
        cards.append(Card("Cubs", "Q"))
        cards.append(Card("Cubs", "K"))

        #Diamonds
        cards.append(Card("Diamonds", "A"))
        cards.append(Card("Diamonds", "2"))
        cards.append(Card("Diamonds", "3"))
        cards.append(Card("Diamonds", "4"))
        cards.append(Card("Diamonds", "5"))
        cards.append(Card("Diamonds", "6"))
        cards.append(Card("Diamonds", "7"))
        cards.append(Card("Diamonds", "8"))
        cards.append(Card("Diamonds", "9"))
        cards.append(Card("Diamonds", "10"))
        cards.append(Card("Diamonds", "J"))
        cards.append(Card("Diamonds", "Q"))
        cards.append(Card("Diamonds", "K"))

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