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
        firstHandWins = 0
        secondHandWins = 0

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
            handOneValues.append(handOneCardOne.value)
            handOneValues.append(handOneCardTwo.value)
            handOneViableCards.append(handOneCardOne)
            handOneViableCards.append(handOneCardTwo)
            handTwoSuits.append(handTwoCardOne.suit)
            handTwoSuits.append(handTwoCardTwo.suit)
            handTwoValues.append(handTwoCardOne.value)
            handTwoValues.append(handTwoCardTwo.value)
            handTwoViableCards.append(handTwoCardOne)
            handTwoViableCards.append(handTwoCardTwo)

            if (self.checkRoyalFlush(handOneSuits, handOneViableCards, handTwoSuits, handTwoViableCards) == False):
                self.checkStraightFlush()

        print("First hand wins: " + str(Deck.handOneWins))
        print("Second hand wins: " + str(Deck.handTwoWins))
        print("Ties: " + str(Deck.ties))
    def checkRoyalFlush(self, handOneSuits, handOneViableCards, handTwoSuits, handTwoViableCards):
        winner = False
        firstHandRoyals = 0
        secondHandRoyals = 0
        handOneRoyalFlush = False
        handTwoRoyalFlush = False

        #checking if the hands have five suited cards
        fiveSuited = False
        fiveSuitedSecond = False
        for b in range(1, 5):
            if handOneSuits.count(b) >= 5:
                fiveSuited = True
                royalFlushSuit = b
            if handTwoSuits.count(b) >= 5:
                fiveSuitedSecond = True
                royalFlushSuitSecond = b

        #checking if first hand has royal flush
        if (fiveSuited == True):
            #Editing the seven cards in the hand to remove those that aren't suited
            for c in list(handOneViableCards):
                if c.suit != royalFlushSuit:
                    handOneViableCards.remove(c)
                elif int(c.value) <= 9:
                    handOneViableCards.remove(c)
            if len(list(handOneViableCards)) == 5:
                handOneRoyalFlush = True
                firstHandRoyals += 1

        #checking if second hand has royal flush
        if (fiveSuitedSecond == True):
            for c in list(handTwoViableCards):
                if c.suit != royalFlushSuitSecond:
                    handTwoViableCards.remove(c)
                elif int(c.value) <= 9:
                    handTwoViableCards.remove(c)
            if len(list(handTwoViableCards)) == 5:
                handTwoRoyalFlush = True
                secondHandRoyals += 1

        #Evaluating which hand won
        if (handOneRoyalFlush == True and handTwoRoyalFlush == False):
            Deck.handOneWins += 1
            winner = True
        if (handOneRoyalFlush == False and handTwoRoyalFlush == True):
            Deck.handTwoWins += 1
            winner = True
        if (handOneRoyalFlush == True and handTwoRoyalFlush == True):
            Deck.ties += 1
            winner = True

        return winner

    #checking straight flush
    def checkStraightFlush(self, handOneSuits, handOneViableCards, handTwoSuits, handTwoViableCards, handOneValues, handTwoValues):
        winner = False
        handOneStraightFlush = False
        handTwoStraightFlush = False

        #checking if the hands have five suited cards
        fiveSuited = False
        fiveSuitedSecond = False
        for b in range(1, 5):
            if handOneSuits.count(b) >= 5:
                fiveSuited = True
                straightFlushSuit = b
            if handTwoSuits.count(b) >= 5:
                fiveSuitedSecond = True
                straightFlushSuitSecond = b

        # checking if first hand has straight flush
        if (fiveSuited == True):
            # Editing the seven cards in the hand to remove those that aren't suited
            for c in list(handOneViableCards):
                if c.suit != straightFlushSuit:
                    handOneViableCards.remove(c)
                    handOneValues.remove(c)
            #if Ace is present, add a temporary card with value of 1 to accomodate possibility of wheel
            handOneValues.sort()
            if (14 in handOneValues):
                handOneValues.remove(handOneValues.length - 1)
                handOneValues.append(1)

            #checking bottom 2 and top 2 cards to see if they are part of SF
            handOneValues.sort()
            if (handOneValues[0] != handOneValues[1] - 1):
                del handOneValues[0]
            if (handOneValues[0] != handOneValues[1] - 1):
                del handOneValues[0]
            if (handOneValues[len(handOneValues)- 1] != handOneValues[len(handOneValues) - 2] + 1):
                del handOneValues[len(handOneValues) - 1]
            if (handOneValues[len(handOneValues) - 1] != handOneValues[len(handOneValues) - 2] + 1):
                del handOneValues[len(handOneValues) - 1]

            handOneValues.sort()
            minValue = min(handOneValues)
            maxValue = max(handOneValues)
            if ((maxValue - minValue + 1) == len(handOneValues)):
                handOneStraightFlush = True

        # checking if second hand has straight flush
        if (fiveSuitedSecond == True):
            for c in list(handTwoViableCards):
                if c.suit != straightFlushSuitSecond:
                    handTwoViableCards.remove(c)
                elif int(c.value) <= 9:
                    handTwoViableCards.remove(c)
            if len(list(handTwoViableCards)) == 5:
                handTwoRoyalFlush = True


    #def checkQuads(self, handOneCardOne, handOneCardTwo, handTwoCardOne, handTwoCardTwo, outcomesList):

    #def checkFullHouse(self, handOneCardOne, handOneCardTwo, handTwoCardOne, handTwoCardTwo, outcomesList):

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


