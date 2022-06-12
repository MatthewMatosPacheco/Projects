import random

class Food(object):
    def __init__(self,n,v,w):
        self.name= n
        self.value= v
        self.calories= w
    def getValue(self):
        return self.value
    def getCost(self):
        return self.calories
    def density(self):
        return self.getValue()/self.getCost()
    def __str__(self):
        return self.name+ ': <'+ str(self.value) + ', '+ str(self.calories)+">"
def buildMenu(names,values,calories):
    """names, values, calories lists of the same lenght.
    name a kist of strings """ # takes in list of names calories vzlues that are the same lenght
    menu=[]
    for i in range(len(values)):
        menu.append(Food(names[i], values[i], calories[i])) #uses class and makes menu so their in the same ', ,'
    return menu
def buildLargeMenu(numItems, maxVal, maxCost):
    items = []
    for i in range(numItems):
        items.append(Food(str(i),
                          random.randint(1, maxVal),
                          random.randint(1, maxCost)))
    return items


    for numItems in (5, 10, 15, 20, 25, 30, 35, 40, 45):
        print('Try a menu with', numItems, 'items')
        items = buildLargeMenu(numItems, 90, 250)
        testMaxVal(items, 750, False)



def fastMaxVal(toConsider, avail, memo={}):
    """Assumes toConsider a list of subjects, avail a weight
         memo supplied by recursive calls
       Returns a tuple of the total value of a solution to the
         0/1 knapsack problem and the subjects of that solution"""
    #key to the memo is a tuple(items left to be considered and available weight) items represented bylen(toConsider)
    if (len(toConsider), avail) in memo:
        result = memo[(len(toConsider), avail)]
    elif toConsider == [] or avail == 0:
        result = (0, ())
    elif toConsider[0].getCost() > avail:
        # Explore right branch only
        result = fastMaxVal(toConsider[1:], avail, memo)
    else:
        nextItem = toConsider[0]
        # Explore left branch
        withVal, withToTake = \
            fastMaxVal(toConsider[1:],
                       avail - nextItem.getCost(), memo)
        withVal += nextItem.getValue()
        # Explore right branch
        withoutVal, withoutToTake = fastMaxVal(toConsider[1:],
                                               avail, memo)
        # Choose better branch
        if withVal > withoutVal:
            result = (withVal, withToTake + (nextItem,))
        else:
            result = (withoutVal, withoutToTake)
    memo[(len(toConsider), avail)] = result
    return result
#updates memo

def testMaxVal(foods, maxUnits, algorithm, printItems=True):
    print('Menu contains', len(foods), 'items')
    print('Use search tree to allocate', maxUnits,
          'calories')
    val, taken = algorithm(foods, maxUnits)
    if printItems:
        print('Total value of items taken =', val)
        for item in taken:
            print('   ', item)

for numItems in (5, 10, 15, 20, 25, 30, 35, 40, 45, 50):
    items = buildLargeMenu(numItems, 90, 250)
    testMaxVal(items, 750, fastMaxVal, True)
