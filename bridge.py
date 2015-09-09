# This program will calculate the number of points a bridge hand has and determine the best opening bid

import random

# This function returns a random bridge hand 
def randomHand():
    deck = [] # list of all 52 possible cards, as 2-character strings
    for suit in "SHDC":
        for rank in "234567890JQKA":
            deck.append(rank+suit)

    random.shuffle(deck) # put deck in random order

    # take the first 13 cards from the shuffled deck
    handString = ""
    for i in range(13):
        handString += deck[i][0] + deck[i][1]

    return handString

# Calculates how many high card points the player has on hand
# precondition: The user has typed in (or been dealt) their hand of cards
# postcondition: The user's high card points score has been calculated
def highCardPoints(hand):
# counts the number of cards the user has and multiplies it by its point value
    acePoints = hand.count('A')*4 
    kingPoints = hand.count('K')*3
    queenPoints = hand.count('Q')*2
    jackPoints = hand.count('J')
# calculates the total amount of high card points the user has and returns that value
    highPoints = acePoints + kingPoints + queenPoints + jackPoints
    return highPoints


# Calculates how many distribution points the player has
# precondition: The user has typed in (or been dealt) their hand of cards
# postcondition: The user's distribution points have been calculated
def distPoints(hand):
    voidPoints = 0
    singlePoints = 0
    doublePoints = 0
# calculates the number of points for Spades
    if hand.count('S') == 0:
        voidPoints += 3
    elif hand.count('S') == 1:
        singlePoints += 2
    elif hand.count('S') == 2:
        doublePoints += 1   
# calculates the number of points for Hearts
    if hand.count('H') == 0:
        voidPoints += 3
    elif hand.count('H') == 1:
        singlePoints += 2
    elif hand.count('H') == 2:
        doublePoints += 1
# calculates the number of points for Diamonds
    if hand.count('D') == 0:
        voidPoints += 3
    elif hand.count('D') == 1:
        singlePoints += 2
    elif hand.count('D') == 2:
        doublePoints += 1
# calculates the number of points for Clubs
    if hand.count('C') == 0:
        voidPoints += 3
    elif hand.count('C') == 1:
        singlePoints += 2
    elif hand.count('C') == 2:
        doublePoints += 1
# calculates the total number of distribution points and returns the value
    distributionPoints = voidPoints + singlePoints + doublePoints
    return distributionPoints

# Adds the total distribution points and the total high card points for an overall total score
# precondition: Both the high card points and the distribution points have been calculated
# postcondition: The high card points and the distribution points have been added together
def totalPoints(hand):
    totalPoints = highCardPoints(hand) + distPoints(hand)
    return totalPoints

# Determines which bid the user should make based on their total points and overall hand
# precondition: The user has been dealt a hand and their total score has been calculated
# postcondition: The user knows which bid they should make based on their hand
def bid(hand):
    if totalPoints(hand) < 14:
        return "pass"
    elif totalPoints(hand) >= 14 and distPoints(hand) == 0 or distPoints(hand) == 1:
        return "1 notrump"
    elif hand.count('S') >= hand.count('H') and hand.count('S') >= hand.count('D') and hand.count('S') >= hand.count('C'):
        return "1 spade"
    elif hand.count('H') >= hand.count('S') and hand.count('H') >= hand.count('D') and hand.count('H') >= hand.count('C'):
        return "1 heart"
    elif hand.count('D') >= hand.count('S') and hand.count('D') >= hand.count('H') and hand.count('D') >= hand.count('C'):
        return "1 diamond"
    elif hand.count('C') >= hand.count('S') and hand.count('C') >= hand.count('H') and hand.count('C') >= hand.count('D'):
        return "1 club"
