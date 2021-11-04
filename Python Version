import itertools

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
    splits = 0
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
        #for c in list(outcomesList):
           # for i in list(c):
            #    i.printCard()
        #implement way to calculate winning hands based on each outcome

    def checkRoyalFlush(self, handOneCardOne, handOneCardTwo, handTwoCardOne, handTwoCardTwo, outcomesList):
        firstHandRoyals = 0
        secondHandRoyals = 0
        handOneRoyalFlush = False
        handTwoRoyalFlush = False
        #creating list of suits for first hand
        for a in list(outcomesList):
            ## put checking the second hand under this for loop so that way you can evaluate conditions
            handOneSuits = []
            handOneViableCards = []
            handOneValues = []
            for i in list(a):
                handOneSuits.append(i.suit)
                handOneViableCards.append(i)
            handOneSuits.append(handOneCardOne.suit)
            handOneSuits.append(handOneCardTwo.suit)
            handOneViableCards.append(handOneCardOne)
            handOneViableCards.append(handOneCardTwo)

            #checking if first hand has at least 5 of same suit
            fiveSuited = False
            for b in range(1, 5):
                if handOneSuits.count(b) >= 5:
                    fiveSuited = True
                    royalFlushSuit = b

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


        # checking second hand now:
        for a in list(outcomesList):
            handTwoSuits = []
            handTwoViableCards = []
            handTwoValues = []
            for i in list(a):
                handTwoSuits.append(i.suit)
                handTwoViableCards.append(i)
            handTwoSuits.append(handTwoCardOne.suit)
            handTwoSuits.append(handTwoCardTwo.suit)
            handTwoViableCards.append(handTwoCardOne)
            handTwoViableCards.append(handTwoCardTwo)

            # checking if first hand has at least 5 of same suit
            fiveSuitedSecond = False
            for b in range(1, 5):
                if handTwoSuits.count(b) >= 5:
                    fiveSuitedSecond = True
                    royalFlushSuitSecond = b

            # checking if first hand has royal flush
            if (fiveSuitedSecond == True):
                for c in list(handTwoViableCards):
                    if c.suit != royalFlushSuitSecond:
                        handTwoViableCards.remove(c)
                    elif int(c.value) <= 9:
                        handTwoViableCards.remove(c)
                if len(list(handTwoViableCards)) == 5:
                    handTwoRoyalFlush = True
                    secondHandRoyals += 1

        print (firstHandRoyals)
        print (secondHandRoyals)







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

deck.checkRoyalFlush(handOneCardOne, handOneCardTwo, handTwoCardOne, handTwoCardTwo, outcomes)

