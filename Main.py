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
        if cardSuit == "s":
            cardSuit = 1
        if cardSuit == "c":
            cardSuit = 2
        if cardSuit == "h":
            cardSuit = 3
        if cardSuit == "d":
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


            handOneRoyal = self.checkRoyalFlush(handOneSuits.copy(), handOneViableCards.copy())
            handTwoRoyal = self.checkRoyalFlush(handTwoSuits.copy(), handTwoViableCards.copy())


            #checking royal flush
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

            #checking straight flush
            if (winner == False):
                handOneSF = self.checkStraightFlush(handOneSuits.copy(), handOneValues.copy(), handOneViableCards.copy())
                handTwoSF = self.checkStraightFlush(handTwoSuits.copy(), handTwoValues.copy(), handTwoViableCards.copy())
                winner = False
                if (handOneSF > handTwoSF):
                    Deck.handOneWins += 1
                    winner = True
                if (handOneSF < handTwoSF):
                    Deck.handTwoWins += 1
                    winner = True
                if (handOneSF > 0 and handTwoSF > 0 and handOneSF == handTwoSF):
                    Deck.ties += 1
                    winner = True

                #checking quads
                if (winner == False):
                    handOneQuads = self.checkQuads(handOneValues.copy())
                    handTwoQuads = self.checkQuads(handTwoValues.copy())
                    winner = False
                    if (handOneQuads > handTwoQuads):
                        Deck.handOneWins += 1
                        winner = True
                    if (handOneQuads < handTwoQuads):
                        Deck.handTwoWins += 1
                        winner = True
                    if (handOneQuads > 0 and handTwoQuads > 0 and handOneQuads == handTwoQuads):
                        Deck.ties += 1
                        winner = True

                    #checking Full House
                    if (winner == False):
                        handOneFullHouse = self.checkFullHouse(handOneValues.copy())
                        handTwoFullHouse = self.checkFullHouse(handTwoValues.copy())
                        winner = False
                        if (handOneFullHouse[0] == 0 and handTwoFullHouse[0] == 0):
                            winner = False
                        elif (handOneFullHouse[0] > handTwoFullHouse[0] and handOneFullHouse[1] != 0 and handTwoFullHouse[1] != 0):
                            Deck.handOneWins += 1
                            winner = True
                        elif (handOneFullHouse[0] < handTwoFullHouse[0] and handOneFullHouse[1] != 0 and handTwoFullHouse[1] != 0):
                            Deck.handTwoWins += 1
                            winner = True
                        elif (handOneFullHouse[0] == handTwoFullHouse[0]):
                            if (handOneFullHouse[1] == 0 and handTwoFullHouse[1] == 0):
                                winner = False
                            elif (handOneFullHouse[1] > handTwoFullHouse[1]):
                                Deck.handOneWins += 1
                                winner = True
                            elif (handOneFullHouse[1] < handTwoFullHouse[1]):
                                Deck.handTwoWins += 1
                                winner = True
                            elif (handOneFullHouse[1] == handTwoFullHouse[1]):
                                Deck.ties += 1
                                winner = True

                        #checking Flush
                        if (winner == False):
                            handOneFlush = self.checkFlush(handOneSuits.copy(), handOneViableCards.copy())
                            handTwoFlush = self.checkFlush(handTwoSuits.copy(), handTwoViableCards.copy())
                            winner = False
                            if (handOneFlush == None and handTwoFlush != None):
                                Deck.handTwoWins += 1
                                winner = True
                            elif (handTwoFlush == None and handOneFlush != None):
                                Deck.handOneWins += 1
                                winner = True
                            elif (handOneFlush != None and handTwoFlush != None):
                                tieFlushCards = 0
                                handOneFlush.sort(reverse = True)
                                handTwoFlush.sort(reverse = True)
                                for i in range(0, 5):
                                    if (handOneFlush[i] > handTwoFlush[i]):
                                        Deck.handOneWins += 1
                                        winner = True
                                    elif (handTwoFlush[i] > handTwoFlush[i]):
                                        Deck.handTwoWins += 1
                                        winner = True
                                    elif (handOneFlush[i] == handTwoFlush[i]):
                                        tieFlushCards += 1
                                if (tieFlushCards == 5):
                                    Deck.ties += 1
                                    winner = True

                            #checking straight
                            if (winner == False):
                                handOneStraight = self.checkStraight(handOneValues.copy())
                                handTwoStraight = self.checkStraight(handTwoValues.copy())
                                winner = False
                                if (handOneStraight == None and handTwoStraight != None):
                                    Deck.handTwoWins += 1
                                    winner = True
                                elif (handTwoStraight == None and handOneStraight != None):
                                    Deck.handOneWins += 1
                                    winner = True
                                elif (handOneStraight != None and handTwoStraight != None):
                                    tieStraightCards = 0
                                    handOneStraight.sort(reverse = True)
                                    handTwoStraight.sort(reverse = True)
                                   # print(handOneStraight)
                                   # print(handTwoStraight)
                                   # print("BREAK---------------")
                                    for i in range(0, 5):
                                        if (handOneStraight[i] > handTwoStraight[i]):
                                            Deck.handOneWins += 1
                                            winner = True
                                        elif (handTwoStraight[i] > handTwoStraight[i]):
                                            Deck.handTwoWins += 1
                                            winner = True
                                        elif (handOneStraight[i] == handTwoStraight[i]):
                                            tieStraightCards += 1
                                    if (tieStraightCards == 5):
                                        Deck.ties += 1
                                        winner = True

                                #checking trips
                                if (winner == False):
                                    handOneTrips = self.checkTrips(handOneValues.copy())
                                    handTwoTrips = self.checkTrips(handTwoValues.copy())
                                    winner = False
                                    if (handOneTrips > handTwoTrips):
                                        Deck.handOneWins += 1
                                        winner = True
                                    if (handOneTrips < handTwoTrips):
                                        Deck.handTwoWins += 1
                                        winner = True
                                    if (handOneTrips > 0 and handTwoTrips > 0 and handOneTrips == handTwoTrips):
                                        handOneTripHand = handOneValues.copy()
                                        handTwoTripHand = handOneValues.copy()
                                        for i in range(0, 15):
                                            if (handOneTripHand.count(i) == 3):
                                                handOneTripHand.remove(i)
                                            if (handTwoTripHand.count(i) == 3):
                                                handTwoTripHand.remove(i)
                                        handOneTripHand.sort(reverse = True)
                                        handTwoTripHand.sort(reverse = True)
                                        tripCounter = 0
                                        for i in range(0, 2):
                                            if (handOneTripHand[i] > handTwoTripHand[i]):
                                                Deck.handOneWins += 1
                                                winner = True
                                            elif (handTwoTripHand[i] > handOneTripHand[i]):
                                                Deck.handTwoWins += 1
                                                winner = True
                                            elif (handOneTripHand[i] == handTwoTripHand[i]):
                                                tripCounter += 1
                                        if (tripCounter == 2):
                                            Deck.ties += 1
                                            winner = True


                                    #checking two pair
                                    if (winner == False):
                                        handOneTwoPair = self.checkTwoPair(handOneValues.copy())
                                        handTwoTwoPair = self.checkTwoPair(handTwoValues.copy())
                                        winner = False
                                        if (handOneTwoPair[0] == 0 and handTwoTwoPair[0] == 0):
                                            winner = False
                                        elif (handOneTwoPair[0] > handTwoTwoPair[0] and handOneTwoPair[1] != 0 and
                                              handTwoTwoPair[1] != 0):
                                            Deck.handOneWins += 1
                                            winner = True
                                        elif (handOneTwoPair[0] < handTwoTwoPair[0] and handOneTwoPair[1] != 0 and
                                              handTwoTwoPair[1] != 0):
                                            Deck.handTwoWins += 1
                                            winner = True
                                        elif (handOneTwoPair[0] == handTwoTwoPair[0]):
                                            if (handOneTwoPair[1] == 0 and handTwoTwoPair[1] == 0):
                                                winner = False
                                            elif (handOneTwoPair[1] > handTwoTwoPair[1]):
                                                Deck.handOneWins += 1
                                                winner = True
                                            elif (handOneTwoPair[1] < handTwoTwoPair[1]):
                                                Deck.handTwoWins += 1
                                                winner = True
                                            elif (handOneTwoPair[1] == handTwoTwoPair[1]):
                                                handOneTwoPairHand = handOneValues.copy()
                                                handTwoTwoPairHand = handTwoValues.copy()
                                                handOneCounter = 0
                                                handTwoCounter = 0
                                                for i in range(15, 1, -1):
                                                    if (handOneCounter <= 2):
                                                        if handOneTwoPairHand.count(i) == 2:
                                                            handOneCounter += 1
                                                            handOneTwoPairHand.remove(i)
                                                    if (handTwoCounter <= 2):
                                                        if handTwoTwoPairHand.count(i) == 2:
                                                            handTwoCounter += 1
                                                            handTwoTwoPairHand.remove(i)
                                                handOneTwoPairHand.sort(reverse = True)
                                                handTwoTwoPairHand.sort(reverse = True)
                                                if (handOneTwoPairHand[0] > handTwoTwoPairHand[0]):
                                                    Deck.handOneWins += 1
                                                    winner = True
                                                elif (handTwoTwoPairHand[0] > handOneTwoPairHand[0]):
                                                    Deck.handTwoWins += 1
                                                    winner = True
                                                elif (handOneTwoPairHand[0] == handTwoTwoPairHand[0]):
                                                    Deck.ties += 1
                                                    winner = True

                                        #checking pair
                                        if (winner == False):
                                            handOnePair = self.checkPair(handOneValues.copy())
                                            handTwoPair = self.checkPair(handTwoValues.copy())
                                            winner = False
                                            if (handOnePair > handTwoPair):
                                                Deck.handOneWins += 1
                                                winner = True
                                            if (handOnePair < handTwoPair):
                                                Deck.handTwoWins += 1
                                                winner = True
                                            if (handOnePair > 0 and handTwoPair > 0 and handOnePair == handTwoPair):
                                                handOnePairHand = handOneValues.copy()
                                                handTwoPairHand = handTwoValues.copy()
                                                pairCounter = 0
                                                for i in range(15, 1, -1):
                                                    if (handOnePairHand.count(i) == 2):
                                                        handOnePairHand.remove(i)
                                                    if (handTwoPairHand.count(i) == 2):
                                                        handTwoPairHand.remove(i)
                                                handOnePairHand.sort(reverse = True)
                                                handTwoPairHand.sort(reverse = True)
                                                for i in range (0, 3):
                                                    if (handOnePairHand[i] > handTwoPairHand[i]):
                                                        Deck.handOneWins += 1
                                                        winner = True
                                                    elif (handTwoPairHand[i] > handOnePairHand[i]):
                                                        Deck.handTwoWins += 1
                                                        winner = True
                                                    elif (handOnePairHand[i] == handTwoPairHand[i]):
                                                        pairCounter += 1
                                                if (pairCounter == 3):
                                                    Deck.ties += 1
                                                    winner = True

                                            #checking high card
                                            if (winner == False):
                                                handOneValues.sort(reverse = True)
                                                handTwoValues.sort(reverse = True)
                                                highCardTie = 0
                                                for i in range (0, 8):
                                                    if (handOneValues[i] > handTwoValues[i]):
                                                        Deck.handOneWins += 1
                                                    elif (handTwoValues[i] > handOneValues[i]):
                                                        Deck.handTwoWins += 1
                                                    elif (handOneValues[i] == handTwoValues[i]):
                                                        highCardTie += 1
                                                if (highCardTie == 7):
                                                    Deck.ties += 1













        print("First hand wins: " + str(Deck.handOneWins))
        print("Second hand wins: " + str(Deck.handTwoWins))
        print("Ties: " + str(Deck.ties))

    def checkRoyalFlush(self, handSuitsParameter, handCardsParameter):
        handSuits = handSuitsParameter
        handCards = handCardsParameter
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
        straightFlush = 0

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

            handValues = []
            for i in list(handCards):
                handValues.append(int(i.value))
            #if Ace is present, add a temporary card with value of 1 to accommodate possibility of wheel
            handValues.sort()
            for c in list(handValues):
                if c == 14:
                    handValues.remove(c)
                    handValues.append(1)


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

            if (len(handValues) >= 5):
                if (sorted(handValues) == list(range(min(handValues), max(handValues) + 1))):
                    straightFlush = max(handValues)

        return straightFlush


    def checkQuads(self, cardValues):
        quads = 0
        for b in range(2, 15):
            if cardValues.count(b) == 4:
                quads = b
        return quads

    def checkFullHouse(self, cardValues):
        fullHouseTrip = 0
        fullHousePair = 0
        for a in range(15, 1, -1):
            if cardValues.count(a) == 3:
                fullHouseTrip = a
                for b in itertools.chain(range(15, a, -1), range(a - 1, 1, -1)):
                    if cardValues.count(b) >= 2:
                        fullHousePair = b
        return fullHouseTrip, fullHousePair


    def checkFlush(self, handSuits, handCards):
        flushValues = None
        fiveSuited = False
        for b in range(1, 5):
            if handSuits.count(b) >= 5:
                fiveSuited = True
                flushSuit = b

        if (fiveSuited == True):
            # Editing the seven cards in the hand to remove those that aren't suited
            for c in list(handCards):
                if c.suit != flushSuit:
                    handCards.remove(c)

            handValues = []
            for i in list(handCards):
                handValues.append(int(i.value))

            flushValues = list(handValues)
            flushValues.sort(reverse = True)
            while (len(flushValues) > 5):
                flushValues.pop()
            return flushValues
        return flushValues


    def checkStraight(self, handValues):
        handValuesNoDups = []
        handValues.sort()
        for c in list(handValues):
            if c == 14:
                handValues.append(1)

        #removing duplicates
        for i in handValues:
            if i not in handValuesNoDups:
                handValuesNoDups.append(i)

        handValuesNoDups.sort()
        #removing cards not part of straight
        if (len(handValuesNoDups) >= 5):
            if (handValuesNoDups[0] != handValuesNoDups[1] - 1):
                del handValuesNoDups[0]
            if (handValuesNoDups[0] != handValuesNoDups[1] - 1):
                del handValuesNoDups[0]
            if (handValuesNoDups[len(handValuesNoDups) - 1] != handValuesNoDups[len(handValuesNoDups) - 2] + 1):
                del handValuesNoDups[len(handValuesNoDups) - 1]
            if (handValuesNoDups[len(handValuesNoDups) - 1] != handValuesNoDups[len(handValuesNoDups) - 2] + 1):
                del handValuesNoDups[len(handValuesNoDups) - 1]

        #evaluating consecutivity
        if (len(handValuesNoDups) >= 5):
            handValuesNoDups.sort(reverse = True)
            if (sorted(handValuesNoDups) == list(range(min(handValuesNoDups), max(handValuesNoDups) + 1))):
                return handValuesNoDups
        else:
            handValuesNoDups = None
            return handValuesNoDups

    def checkTrips(self, handValues):
        trips = 0
        for b in range(14, 1, -1):
            if handValues.count(b) == 3:
                trips = b
        return trips

    def checkTwoPair(self, handValues):
        highPair = 0
        lowPair = 0
        for b in range(15, 1, -1):
            if handValues.count(b) == 2:
                highPair = b
                for a in itertools.chain(range(15, b, -1), range(b - 1, 1, -1)):
                    if handValues.count(a) == 2:
                        lowPair = a
        return highPair, lowPair

    def checkPair(self, handValues):
        pair = 0
        for b in range(15, 1, -1):
            if handValues.count(b) == 2:
                pair = b
        return pair










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


