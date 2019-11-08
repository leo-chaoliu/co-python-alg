from enum import Enum
import random

"""
For IT5003 - by SYJ 

Version 1.0 (2019 October)
- For Lab 

"""

class Suit(Enum):
    SPADE = 1
    HEART = 2
    CLUB = 3
    DIAMOND = 4

class Rank(Enum):
    ACE = 1
    TWO = 2
    THREE = 3
    FOUR = 4
    FIVE = 5
    SIX = 6
    SEVEN = 7
    EIGHT = 8
    NINE = 9
    TEN = 10
    JACK = 11
    QUEEN = 12
    KING = 13

class Card():
    """ A simple class to represent a poker card """
    def __init__(self, suit, rank):
        """ Take a Suit enum and a Rank enum to create a Card object """
        self._suit = suit
        self._rank = rank
    
    def toString(self):
        """ Print the Card with Rank followed by Suit, e.g. \"ACE SPADE\" """
        return self._rank.name + " " + self._suit.name

class Deck():
    """ A class representing a deck of Cards """
    def __init__(self):
        """ Create a new deck of cards, with 52 unique cards 
        
            The cards are ordered (from top of deck): ACE to KING in each Suit {SPADE, HEART, CLUB, DIAMOND}
        """
        self.cards = self._initCards()
    
    def _initCards(self):
        # contain 52 Card object(instance) in the list 
        cards = []
        
        for i in Suit:
            for j in Rank:
                card = Card(i,j)
                cards.append(card)
        
        return cards
    
    def shuffle(self):
        """ Randomize the cards in the deck """
        randomCards=[]
       
    #    for i range(51,-1,-1):
    #         random_index=random.randint(0,i)
    #         randomCards.append(self.cards[random_index])
    #         self.cards.remove(self.cards[random_index])

        i=51
        while i >-1:
            random_index=random.randint(0,i)
            randomCards.append(self.cards[random_index])
            self.cards.remove(self.cards[random_index])
            i=i-1
        
        # return randomCards
        self.cards = randomCards

    def takeCard(self):
        """ Return one Card from the top of deck. Card is removed from Deck. """
        
        return_card=self.cards[-1]
        self.cards.remove(self.cards[-1])
        return return_card
        # return self.cards.pop()

    def getSize(self):
        """ Return the number of remaining cards in the deck """ 
        # return self.cards
        return len(self.cards)

    def toString(self):
        """ Print the deck from top to bottom.

            Shows the card position (top = 1). 

            Format example " 1. ACE SPADE"
        """
        result=[]
        index=0
        for card in self.cards:
            result.append(" {0}. {1} {2}".format(index+1, card._rank.name, card._suit.name))
            index=index+1

        return result
        
def main():

    # Show how to loop through all enumerations
    # for s in Suit:
    #     for r in Rank:
    #         print(s.name+ " : "+ r.name)


    # Basic card game that shows two poker hands (5 cards each)
    d = Deck()
    # Can uncomment to check the original ordering
    # print(d.toString())
    print("Deck has %d cards at the start\n"%(d.getSize()))
    
    d.shuffle()
    # Uncomment to check whether shuffling works properly
    print(d.toString())

    # #Simple code to get two power hands
    pokerhand = [d.takeCard() for i in range(5)]
    
    # hand = []
    # for i in range(5):
    #     hand.append(d.takeCard())

    print("First poker hand:")
    # card object
    for c in pokerhand:
        print(c.toString())
    

    pokerhand = [d.takeCard() for i in range(5)]
    print("\nSecond poker hand:")
    for c in pokerhand:
        print(c.toString())
    
    
    print("Deck has %d cards at the end"%(d.getSize()))


if __name__ == "__main__":
    main()