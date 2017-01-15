from actionitem import ActionItem
import copy

class Link(object):
    """ a link pointing from src to dest
        Upon the fire of src, it triggers the action of dest
        A src is in the form of componentA::action1
        A dest is in the form of componentB::action3
        componentA::action1 -> componentB::action3 
    """
    def __init__(self, src, srcToken, dest, destAction, arg=None):
        self.src = src
        self.srcToken = srcToken
        # create an action item for destination
        self.ai = ActionItem()
        self.ai.setOwner(dest)
        self.ai.setAction(destAction)
        self.ai.passArg(arg)

    def getSrc(self):
        """ return the from component object
        """
        return self.src

    def getDest(self):
        """ return the to component object
        """
        return self.ai.getOwner()

    def checkTokenStr(self, compTokenStr):
        """ token is in the form of string 
            "L1CacheCtrl::cacheMiss"
            L1CacheCtrl is the component name
            cacheMiss is the token name
            When L1CacheCtrl calls function checkTag, it can emit a cacheMiss token 
        """
            # split token string by "::"
        (srcName,tokenName) = str(compTokenStr).split('::')
        if (srcName == self.fromComponent.getName()) and (tokenName == self.srcToken):
            return True
        else:
            return False

    def isTokenMatch(self, token):
        """ token is in the form of [component, Token] 
        """
            # split token string by "::"
        if (token.getComponent() == self.src) and (token.getInfoString() == self.srcToken):
            return True
        else:
            return False

    def activate(self):
        """ once the evalToken returns true, the dest can be activated
        """        
        self.ai.do()
    
    def eval(self, token):
        if self.isTokenMatch(token): # tokenMatch
            self.activate()

    def __repr__(self):
        s = ""
        s = self.src.getName() + "::" + self.srcToken + "----->" +  \
            self.dest.getName() + "." + self.destAction

        return s

# unit test
from test_util import Agent
import random
from token import Token
from token import TokenPool

tokenPool = TokenPool('testTokenPool')

class Cache(Agent):
    def __init__(self, name):
        super().__init__(name)
        random.seed(10)

    def checkTag(self):
        r = random.randint(0,10)
        if r<6: # cache hit
            print('%s cache hit' % self.name)
            emitToken = Token(self, 'cacheHit')
        else: # cache miss
            print('%s cache miss' % self.name)
            emitToken = Token(self, 'cacheMiss')
        
        tokenPool.insert(emitToken)
    
    def serviceMiss(self):
        print('%s is servicing miss' % self.name)

    def serviceHit(self):
        print('%s is servicing hit' % self.name)

l1cache = Cache('L1Cache')
l2cache = Cache('L2Cache')

l1cache.checkTag()

l1miss_action = Link(l1cache,'cacheMiss',l2cache,'serviceMiss')
l1hit_action = Link(l1cache,'cacheHit',l2cache,'serviceHit')

print(l1miss_action)
print(l1hit_action)

token=tokenPool.pop()
while token:
    l1miss_action.eval(token)
    l1hit_action.eval(token)
    token=tokenPool.pop()


    
    
