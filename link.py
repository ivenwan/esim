

class Link(object):
    """ a link pointing from src to dest
        Upon the fire of src, it triggers the action of dest
        A src is in the form of componentA::action1
        A dest is in the form of componentB::action3
        componentA::action1 -> componentB::action3 
    """
    def __init__(self, fromComponent, fromComponentToken, toComponent, fromComponentAction):
        self.fromComponent = fromComponent
        self.fromComponentToken = fromComponentToken
        self.toComponent = toComponennt
        self.toComponentAction = toComponentAction


    def getFromComponent(self):
        """ return the from component object
        """
        return self.fromComponent

    def getToComponent(self):
        """ return the to component object
        """
        return self.toComponent

    def checkToken(self, compTokenStr):
        """ token is in the form of string 
            "L1CacheCtrl::cacheMiss"
            L1CacheCtrl is the component name
            cacheMiss is the token name
            When L1CacheCtrl calls function checkTag, it can emit a cacheMiss token 
        """
            # split token string by "::"
        (compName,tokenName) = str(compTokenStr).split('::')
        if (compName == self.fromComponent.getName()) and (tokenName == self.fromComponentToken):
            return True
        else:
            return False

    def activate(self):
        """ once the evalToken returns true, the toComponent can be activated
        """
        functionToCall = getattr(self.toComponent, self.toComponentAction)
        functionToCall()
    
    def __repr__(self):
        s = ""
        s = self.fromComponent.getName() + "::" + self.fromComponentToken + "----->" +  \
            self.toComponent.getName() + "." + self.toComponentAction

        return s

# unit test
from test_util import Agent
import random

class L1Cache(Agent):
    def __init__(self, name):
        super().__init__(name)
        random.seed(10)

    def checkTag(self):
        r = random.randint(0,10)
        if r<6:
            


l1cache = Agent('L1Cache')
l2cache = Agent('L2Cache')



    
    
