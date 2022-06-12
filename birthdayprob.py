import random


def rollDie():
    """returns a random int between 1 and 6"""
    return random.choice([1, 2, 3, 4, 5, 6])  # chooses 1 member of list uniform distribution


def testRoll(n=10):
    result = ''
    for i in range(n):
        result = result + str(rollDie())
    print(result)


# testRoll(5)
def sameDate(numPeople, numSame):
    possibleDates = range(366)
#    possibleDates = 4*list(range(0, 57)) + [58]\ # realistic distributions of births
#                    + 4*list(range(59, 366))\
#                    + 4*list(range(180, 270))
    birthdays = [0]*366
    for p in range(numPeople): #random choice off possible dates
        birthDate = random.choice(possibleDates)
        birthdays[birthDate] += 1 # increment element of the list by 1
    return max(birthdays) >= numSame

def birthdayProb(numPeople, numSame, numTrials):
    numHits = 0
    for t in range(numTrials):
        if sameDate(numPeople, numSame):
            numHits += 1 # increment by 1 number of sames
    return numHits/numTrials

import math

for numPeople in [10, 20, 40, 100]:
    print('For', numPeople,
          'est. prob. of a shared birthday is',
          birthdayProb(numPeople, 2, 10000))# can change 2 for any number to find how many people share birthday
    numerator = math.factorial(366) # factorial implementation faster then recursive
    denom = (366**numPeople)*math.factorial(366-numPeople)
    print('Actual prob. for N = 100 =',
          1 - numerator/denom)
