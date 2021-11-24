import itertools
#Q-Learning to learn about ML
#KNN, SVM, Random Forest, Elastic Net, to see pre made prediction models
    #My task is to find how to store data and read it
#probably will need to use heaps data structure


class Card:

    def __init__(self, value, suit):
        self.value = value
        self.suit = suit
        
    def printCard(self):
        if (int(self.value) == 14):
            value = "Ace"
        elif (int(self.value) == 13):
            value = "King"
        elif (int(self.value) == 12):
            value = "Queen"
        elif (int(self.value) == 11):
            value = "Jack"
        else:
            value = self.value

        if self.suit == 1:
            suit = "Spades"
        if self.suit == 2:
            suit = "Clubs"
        if self.suit == 3:
            suit = "Hearts"
        if self.suit == 4:
            suit = "Diamonds"
        print(value, suit)

    def getCardValue(self):
        cardOneValueMenu = "Enter the card's value:\r\n"
        cardValue = input(cardOneValueMenu)
        if cardValue == "Jack":
            cardValue = 11
        if cardValue == "Queen":
            cardValue = 12
        if cardValue == "King":
            cardValue = 13
        if cardValue == "Ace":
            cardValue = 14
        return cardValue

    def getCardSuit(self):
        cardOneSuitMenu = "Enter the card's suit: \r\n"
        cardSuit = input(cardOneSuitMenu)
        if cardSuit == "Spades":
            cardSuit = 1
        if cardSuit == "Clubs":
            cardSuit = 2
        if cardSuit == "Hearts":
            cardSuit = 3
        if cardSuit == "Diamonds":
            cardSuit = 4
        return cardSuit


class Deck:
    handOneWins = 0
    handTwoWins = 0
    ties = 0
    def __init__(self):
        self.cards = []
        self.createDeck()


    def createDeck(self):
        for s in range(1, 5):
            for v in range(2, 15):
                self.cards.append(Card(v, s))

    def printDeck(self):
        for c in self.cards:
            c.printCard()

    def removeDealtCard(self, card):
        for c in self.cards:
            if int(card.value) == int(c.value) and int(card.suit) == int(c.suit):
                self.cards.remove(c)

    def calculateOutcomes(self):
        outcomesList = list(itertools.combinations(self.cards, 5))
        return outcomesList


    def checkOutcomes(self, handOneCardOne, handOneCardTwo, handTwoCardOne, handTwoCardTwo, outcomesList):

        #creating helper lists
        for i in list(outcomesList):
            handOneSuits = []
            handOneViableCards = []
            handOneValues = []
            handTwoSuits = []
            handTwoViableCards = []
            handTwoValues = []

            #populating the 7 card hand list
            for i in list(i):
                handOneSuits.append(i.suit)
                handOneValues.append(i.value)
                handOneViableCards.append(i)
                handTwoSuits.append(i.suit)
                handTwoValues.append(i.value)
                handTwoViableCards.append(i)
            handOneSuits.append(handOneCardOne.suit)
            handOneSuits.append(handOneCardTwo.suit)
            handOneValues.append(int(handOneCardOne.value))
            handOneValues.append(int(handOneCardTwo.value))
            handOneViableCards.append(handOneCardOne)
            handOneViableCards.append(handOneCardTwo)
            handTwoSuits.append(handTwoCardOne.suit)
            handTwoSuits.append(handTwoCardTwo.suit)
            handTwoValues.append(int(handTwoCardOne.value))
            handTwoValues.append(int(handTwoCardTwo.value))
            handTwoViableCards.append(handTwoCardOne)
            handTwoViableCards.append(handTwoCardTwo)

            handOneRoyal = self.checkRoyalFlush(handOneSuits, handOneViableCards)
            handTwoRoyal = self.checkRoyalFlush(handTwoSuits, handTwoViableCards)

            winner = False
            if (handOneRoyal == True and handTwoRoyal == False):
                Deck.handOneWins += 1
                winner = True
            if (handOneRoyal == False and handTwoRoyal == True):
                Deck.handTwoWins += 1
                winner = True
            if (handOneRoyal == True and handTwoRoyal == True):
                Deck.ties += 1
                winner = True

            if (winner == False):
                handOneSF = self.checkStraightFlush(handOneSuits, handOneValues, handOneViableCards)
                handTwoSF = self.checkStraightFlush(handTwoSuits, handTwoValues, handTwoViableCards)
                winner = False
                if (handOneSF == True and handTwoSF == False):
                    Deck.handOneWins += 1
                    winner = True
                if (handOneSF == False and handTwoSF == True):
                    Deck.handTwoWins += 1
                    winner = True
                if (handOneSF == True and handTwoSF == True):
                    Deck.ties += 1
                    winner = True

                if (winner == False):
                    handOneQuads = self.checkQuads(handOneValues)
                    handTwoQuads = self.checkQuads(handTwoValues)
                    winner = False
                    if (handOneQuads == True and handTwoQuads == False):
                        Deck.handOneWins += 1
                        print(handOneValues)
                        winner = True
                    if (handOneQuads == False and handTwoQuads == True):
                        Deck.handTwoWins += 1
                        winner = True
                    if (handOneQuads == True and handTwoQuads == True):
                        Deck.ties += 1
                        winner = True

        print("First hand wins: " + str(Deck.handOneWins))
        print("Second hand wins: " + str(Deck.handTwoWins))
        print("Ties: " + str(Deck.ties))

    def checkRoyalFlush(self, handSuits, handCards):
        royalFlush = False

        #checking if the hands have five suited cards
        fiveSuited = False
        for b in range(1, 5):
            if handSuits.count(b) >= 5:
                fiveSuited = True
                royalFlushSuit = b

        #checking if hand has royal flush
        if (fiveSuited == True):
            #Editing the seven cards in the hand to remove those that aren't suited
            for c in list(handCards):
                if c.suit != royalFlushSuit:
                    handCards.remove(c)
                elif int(c.value) <= 9:
                    handCards.remove(c)
            if len(list(handCards)) == 5:
                royalFlush = True

        return royalFlush

    #checking straight flush
    def checkStraightFlush(self, handSuits, handValues, handCards):
        straightFlush = False

        #checking if the hands have five suited cards
        fiveSuited = False
        for b in range(1, 5):
            if handSuits.count(b) >= 5:
                fiveSuited = True
                straightFlushSuit = b

        # checking if hand has straight flush
        if (fiveSuited == True):
            # Editing the seven cards in the hand to remove those that aren't suited
            for c in list(handCards):
                if c.suit != straightFlushSuit:
                    handCards.remove(c)
                    handValues.remove(c)
            #if Ace is present, add a temporary card with value of 1 to accomodate possibility of wheel
            handValues.sort()
            for c in list(handValues):
                if c == 14:
                    handValues.remove(c)

            #checking bottom 2 and top 2 cards to see if they are part of SF
            handValues.sort()
            if (handValues[0] != handValues[1] - 1):
                del handValues[0]
            if (handValues[0] != handValues[1] - 1):
                del handValues[0]
            if (handValues[len(handValues)- 1] != handValues[len(handValues) - 2] + 1):
                del handValues[len(handValues) - 1]
            if (handValues[len(handValues) - 1] != handValues[len(handValues) - 2] + 1):
                del handValues[len(handValues) - 1]

            if (sorted(handValues) == list(range(min(handValues), max(handValues) + 1)) and len(handValues) >= 5):
                straightFlush = True

        return straightFlush


    def checkQuads(self, cardValues):
        quads = False
        for b in range(2, 15):
            if cardValues.count(b) == 4:
                quads = True
        return quads

    def checkFullHouse(self, cardValues):
        fullHouse = False
        for a in range(2, 15):
            if cardValues.count(a) == 3:
                

    #def checkFlush(self, handOneCardOne, handOneCardTwo, handTwoCardOne, handTwoCardTwo, outcomesList):

    #def checkStraight(self, handOneCardOne, handOneCardTwo, handTwoCardOne, handTwoCardTwo, outcomesList):

    #def checkTrips(self, handOneCardOne, handOneCardTwo, handTwoCardOne, handTwoCardTwo, outcomesList):

    #def checkTwoPair(self, handOneCardOne, handOneCardTwo, handTwoCardOne, handTwoCardTwo, outcomesList):

    #def checkPair(self, handOneCardOne, handOneCardTwo, handTwoCardOne, handTwoCardTwo, outcomesList):

    #def checkHighCard(self, handOneCardOne, handOneCardTwo, handTwoCardOne, handTwoCardTwo, outcomesList):








#Creating First Hand
tempCard = Card("tempValue", "tempSuit")
print("First Hand:")
print("First Card Info:")
handOneCardOneValue = tempCard.getCardValue()
handOneCardOneSuit = tempCard.getCardSuit()
handOneCardOne = Card(handOneCardOneValue, handOneCardOneSuit)
print("Second Hand Info:")
handOneCardTwoValue = tempCard.getCardValue()
handOneCardTwoSuit = tempCard.getCardSuit()
handOneCardTwo = Card(handOneCardTwoValue, handOneCardTwoSuit)

#Creating Second Hand
print("Second Hand:")
print("First Card Info:")
handTwoCardOneValue = tempCard.getCardValue()
handTwoCardOneSuit = tempCard.getCardSuit()
handTwoCardOne = Card(handTwoCardOneValue, handTwoCardOneSuit)
print("Second Hand Info:")
handTwoCardTwoValue = tempCard.getCardValue()
handTwoCardTwoSuit = tempCard.getCardSuit()
handTwoCardTwo = Card(handTwoCardTwoValue, handTwoCardTwoSuit)

#Removing those cards from the deck
deck = Deck()
deck.removeDealtCard(handOneCardOne)
deck.removeDealtCard(handOneCardTwo)
deck.removeDealtCard(handTwoCardOne)
deck.removeDealtCard(handTwoCardTwo)

#running all possible outcomes
outcomes = deck.calculateOutcomes()

#calling the methods to check all the outcomes
deck.checkOutcomes(handOneCardOne, handOneCardTwo, handTwoCardOne, handTwoCardTwo, outcomes)


