import random, pylab

# set line width
pylab.rcParams['lines.linewidth'] = 4
# set font size for titles
pylab.rcParams['axes.titlesize'] = 20
# set font size for labels on axes
pylab.rcParams['axes.labelsize'] = 20
# set size of numbers on x-axis
pylab.rcParams['xtick.labelsize'] = 16
# set size of numbers on y-axis
pylab.rcParams['ytick.labelsize'] = 16
# set size of ticks on x-axis
pylab.rcParams['xtick.major.size'] = 7
# set size of ticks on y-axis
pylab.rcParams['ytick.major.size'] = 7
# set size of markers, e.g., circles representing points
# set numpoints for legend
pylab.rcParams['legend.numpoints'] = 1


class Location(object):
    def __init__(self, x, y):
        """x and y are numbers"""
        self.x = x
        self.y = y

    def move(self, deltaX, deltaY):
        """deltaX and deltaY are numbers"""
        return Location(self.x + deltaX, self.y + deltaY)

    def getX(self):
        return self.x

    def getY(self):
        return self.y

    def distFrom(self, other):
        xDist = self.x - other.getX()
        yDist = self.y - other.getY()
        return (xDist ** 2 + yDist ** 2) ** 0.5

    def __str__(self):
        return '<' + str(self.x) + ', ' + str(self.y) + '>'


class Field(object): # maps drunk to his location on the field
    def __init__(self):
        self.drunks = {}

    def addDrunk(self, drunk, loc):
        if drunk in self.drunks:
            raise ValueError('Duplicate drunk') # if drunk already their were not gonna put the drunk in
        else:
            self.drunks[drunk] = loc # otherwise ser drunk to loc location ( key in dictionary thats why he has to be immutable)

    def moveDrunk(self, drunk): # use this to move the immutable drunk.( this mutuable were changing value of the fiel ( key of dict))
        if drunk not in self.drunks:
            raise ValueError('Drunk not in field')
        xDist, yDist = drunk.takeStep()
        # use move method of Location to get new location
        self.drunks[drunk] = \
            self.drunks[drunk].move(xDist, yDist)

    def getLoc(self, drunk):
        if drunk not in self.drunks:
            raise ValueError('Drunk not in field')
        return self.drunks[drunk]


class Drunk(object): # not usefull by itself just a class to be inherited ( many types of drunk)
    def __init__(self, name=None):
        """Assumes name is a str"""
        self.name = name

    def __str__(self):
        if self != None:
            return self.name
        return 'Anonymous'

#still immutable cuz nothing changes when stepping still same choices, same goes with location
class UsualDrunk(Drunk):
    def takeStep(self):
        stepChoices = [(0, 1), (0, -1), (1, 0), (-1, 0)] # this is x, y or in other words: East/West , North/South
        return random.choice(stepChoices)


class MasochistDrunk(Drunk): # always goes north because of bias
    def takeStep(self):
        stepChoices = [(0.0, 1.1), (0.0, -0.9), #bias to north
                       (1.0, 0.0), (-1.0, 0.0)]
        return random.choice(stepChoices)


def walk(f, d, numSteps):
    """Assumes: f a Field, d a Drunk in f, and numSteps an int >= 0.
       Moves d numSteps times, and returns the distance between
       the final location and the location at the start of the
       walk."""
    start = f.getLoc(d)
    for s in range(numSteps):
        f.moveDrunk(d)
    return start.distFrom(f.getLoc(d))


def simWalks(numSteps, numTrials, dClass): # simulationg multiple walks, D class stands for deunk class cuz we could have as many types as we want
    """Assumes numSteps an int >= 0, numTrials an int > 0,
         dClass a subclass of Drunk
       Simulates numTrials walks of numSteps steps each.
       Returns a list of the final distances for each trial"""
    Homer = dClass('Homer')
    origin = Location(0, 0)
    distances = []
    for t in range(numTrials):
        f = Field()
        f.addDrunk(Homer, origin)
        distances.append(round(walk(f, Homer,
                                    numSteps), 1))
    return distances


def drunkTest(walkLengths, numTrials, dClass):
    """Assumes walkLengths a sequence of ints >= 0
         numTrials an int > 0, dClass a subclass of Drunk
       For each number of steps in walkLengths, runs simWalks with
         numTrials walks and prints results"""
    for numSteps in walkLengths:
        distances = simWalks(numSteps, numTrials, dClass)
        print(dClass.__name__, 'random walk of', numSteps, 'steps')
        print(' Mean =', round(sum(distances) / len(distances), 4))
        print(' Max =', max(distances), 'Min =', min(distances))

# at the end it just prints some stats
random.seed(0)
drunkTest((0, 100, 1000, 10000), 100, UsualDrunk) # you can test both
#is answer plausible?
#suspiscious cuz if you say 0 steps wrong answer = bug in code
# bug is numb trials should be num steps in line 118 we switched it soo it now works
def simAll(drunkKinds, walkLengths, numTrials):
    for dClass in drunkKinds:
        drunkTest(walkLengths, numTrials, dClass)

#simAll((UsualDrunk, MasochistDrunk), (1000, 10000), 100)