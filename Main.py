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
                handOneViableCards.append(i)
                handTwoSuits.append(i.suit)
                handTwoViableCards.append(i)
            handOneSuits.append(handOneCardOne.suit)
            handOneSuits.append(handOneCardTwo.suit)
            handOneViableCards.append(handOneCardOne)
            handOneViableCards.append(handOneCardTwo)
            handTwoSuits.append(handTwoCardOne.suit)
            handTwoSuits.append(handTwoCardTwo.suit)
            handTwoViableCards.append(handTwoCardOne)
            handTwoViableCards.append(handTwoCardTwo)

            proceed = self.checkRoyalFlush(handOneSuits, handOneViableCards, handTwoSuits, handTwoViableCards)
            
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
    def checkStraightFlush(self, handOneCardOne, handOneCardTwo, handTwoCardOne, handTwoCardTwo, outcomesList):
        firstHandSFs = 0
        secondHandSFs = 0
        # creating list of suits for first hand
        for a in list(outcomesList):
            handOneSF = False
            handTwoSF = False
            handOneSuits = []
            handOneViableCards = []
            handOneValues = []
            handTwoSuits = []
            handTwoViableCards = []
            handTwoValues = []

            # populating the 7 card hand list
            for i in list(a):
                handOneSuits.append(i.suit)
                handOneViableCards.append(i)
                handTwoSuits.append(i.suit)
                handTwoViableCards.append(i)
            handOneSuits.append(handOneCardOne.suit)
            handOneSuits.append(handOneCardTwo.suit)
            handOneViableCards.append(handOneCardOne)
            handOneViableCards.append(handOneCardTwo)
            handTwoSuits.append(handTwoCardOne.suit)
            handTwoSuits.append(handTwoCardTwo.suit)
            handTwoViableCards.append(handTwoCardOne)
            handTwoViableCards.append(handTwoCardTwo)

            # checking if the hands have five suited cards
            fiveSuited = False
            fiveSuitedSecond = False
            for b in range(1, 5):
                if handOneSuits.count(b) >= 5:
                    fiveSuited = True
                    royalFlushSuit = b
                if handTwoSuits.count(b) >= 5:
                    fiveSuitedSecond = True
                    royalFlushSuitSecond = b


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


