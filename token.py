
class Token(object):
    """ A token is the command an componennt object emit to trigger chain action
        A token is of form:
        (componentObject, tokenString),
        For example, when L1 Cache check tag if can emit the following tokens:
        (L1Cache, 'cacheMiss'), or (L1Cache, 'cacheHit')
    """
    def __init__(self, component, infoString):
        self.component = component
        self.infoString = infoString
    
    def getComponent(self):
        return self.component

    def getInfoString(self):
        return self.infoString
    
    def __repr__(self):
        s = self.component.getName() + '::' + self.getInfoString()
        return s


class TokenPool(object):
    """ TokenPool is where each component object can deposite token    
    """

    def __init__(self, name):
        self.name = name
        self.tokenPool = []

    def insertToken(self, token):
        self.tokenPool.append(token)
    
    def hasToken(self, component, infoString):
        for token in self.tokenPool:
            if (token.getComponent() == component) and (token.getInfoString() == infoString):
                return token
            
        return None
        
    def findAndRemoveToken(self, component, infoString):
        """ find if token exist by component and infoString
        """
        token = self.hasToken(component, infoString)
        if token: # not None
            self.tokenPool.remove(token)

    def findAndRemoveTokenAll(self, component, infoString):
        """ find if token exist by component and infoString
        """
        token = self.hasToken(component, infoString)
        while (token):
            self.tokenPool.remove(token)
            token = self.hasToken(component, infoString)

    def __repr__(self):
        s = ''
        for token in self.tokenPool:
            s += str(token) + '\n'
        return s

# unit test
from test_util import Agent

l1cache = Agent('L1Cache')
l2cache = Agent('L2Cache')

token_l1miss = Token(l1cache, 'cacheMiss')
token_l1hit = Token(l1cache,'cacheHit')

token_l2miss = Token(l2cache, 'cacheMiss')
token_l2hit = Token(l2cache,'cacheHit')

tokenPool = TokenPool('globalTokenPool')
tokenPool.insertToken(token_l1hit)
tokenPool.insertToken(token_l1miss)
tokenPool.insertToken(token_l2hit)
tokenPool.insertToken(token_l2miss)
print("*****Simple token test:\n")
print(tokenPool)

# duplicated token
tokenPool.insertToken(token_l1hit)
print("*****Duplicated token test:\n")
print(tokenPool)

# remove a token
print("*****Find and remove token l2cache::cacheMiss test:\n")
tokenPool.findAndRemoveToken(l2cache, 'cacheMiss')
print(tokenPool)

# remove multiple-hit token
print("*****Find and remove all token l1cache::cacheHit test:\n")
tokenPool.findAndRemoveToken(l1cache, 'cacheHit')
print(tokenPool)