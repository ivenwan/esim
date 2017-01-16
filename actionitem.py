from test_util import Agent
import copy
class ActionItem(object):
    """ A class create/maintain/process action item
    """

    def __init__(self, owner, action, arg=None):
        self.setOwner(owner)
        self.setAction(action)
        self.passArg(arg)


    def setOwner(self, owner):
        self.owner = owner

    def setAction(self, action):
        """ action is a function name of the owner
        """
        self.action = action
    
    def getOwner(self):
        return self.owner

    def getAction(self):
        return self.action
    
    def getArg(self):
        return self.arg

    def passArg(self, arg):
        self.arg = copy.deepcopy(arg)

    def do(self):
        result = getattr(self.owner, self.action)(self.arg)
        return True

    def __repr__(self):
        return "ai:  %s::%s" % (self.owner, self.action)

class ScheduledActionItem(ActionItem):
    
    def __init__(self, owner, action, delay=0, arg=None):
        super().__init__(owner, action, arg)
        self.delay = delay
    
    def setDelay(self, delay):
        self.delay = delay

    
    def step(self):
        self.delay = self.delay - 1
    
    def do(self):
        """ When return True means the action item is done
            When return False means the action item is not done
        """
        if self.delay == 0:
            super().do()
            self.delay = -1
            return True
        else:
            self.step()
            return False
    
    def __repr__(self):
        s = ''
        if (self.delay >= 0):
            s = s + 'delay[%d] ' % self.delay + super().__repr__()
        return s

from random import random
class RandomActionItem(ActionItem):
    """ an ai is randomized triggered by an random event based on specified probability
    """

    def __init__(self, owner, action, probability=0.5, arg=None):
        super().__init__(owner, action, arg)
        self.probability = probability
        self.p = 0
    
    def setProbability(self, requiredProbability):
        self.probability = requiredProbability

    def toss(self):
        self.p = random()
        
        if self.p <= self.probability:
            return True
        else:
            return False
        

    def do(self):
        """ When return True means the action item is done
            When return False means the action item is not done
        """
        if self.toss():  # probability allows
            super().do()
            return True
        else:
            return False

    def __repr__(self):
        s = 'required probability=%f current p=%f ' % (self.probability, self.p) + super().__repr__()
        return s

# unit test


agent = Agent("dummy")

print('### test basic ai')
ai = ActionItem(agent, 'open')
ai.do()

print('### test scheduled ai')
sch_ai = ScheduledActionItem(agent, 'open', 4)

for i in range(0,5):
    print ("test shcedule ai clock %d:" % i)
    sch_ai.do()
    
print ("### test random ai:")
rand_ai = RandomActionItem(agent, 'open', 0.2)

while (not rand_ai.do()):
    print (rand_ai)

print('[finish rand ai] %s' % rand_ai)


