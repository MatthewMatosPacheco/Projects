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

def maxVal(toConsider, avail):  # decision tree part, TC= list of items, avail is an index to know if theirs anything left
    """Assumes toConsider a list of items, avail a weight
       Returns a tuple of the total value of a solution to the
         0/1 knapsack problem and the items of that solution"""
    if toConsider == [] or avail == 0: #if too consider is empty or avial ==0
        result = (0, ()) # base of recursion, either nothing left to consider or no more weight
    elif toConsider[0].getCost() > avail: # if the get cost of to consider > avail cant aford right path
        #Explore right branch only
        result = maxVal(toConsider[1:], avail)
        # result = remiander of the lis[1:](with first one sliced off, and avail unchanged cuz we didnt choose the path notice we recalled max val
    else: # if not at base or not overweight
        nextItem = toConsider[0]
        #Explore left branch
        withVal, withToTake = maxVal(toConsider[1:],
                                     avail - nextItem.getCost()) # take the item in this scenario have to take out the weight
        withVal += nextItem.getValue() # add value to measure
        #Explore right branch
        withoutVal, withoutToTake = maxVal(toConsider[1:], avail) #recalling max val for the rest of the list, what happens if we dont take it
        #Choose better branch
        if withVal > withoutVal: # this is where we see if its better, recursive go all the way to the bottom and go back up till base
            result = (withVal, withToTake + (nextItem,))
        else:
            result = (withoutVal, withoutToTake)
    return result

def testMaxVal(foods, maxUnits, printItems = True):
    print('Use search tree to allocate', maxUnits,
          'calories')
    val, taken = maxVal(foods, maxUnits)
    print('Total value of items taken =', val)
    if printItems:
        for item in taken:
            print('   ', item)

names = ['wine', 'beer', 'pizza', 'burger', 'fries',
         'cola', 'apple', 'donut', 'cake']
values = [89,90,95,100,90,79,50,10]
calories = [123,154,258,354,365,150,95,195]
foods = buildMenu(names, values, calories)
testMaxVal(foods, 1200)