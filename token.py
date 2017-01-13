
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

    def insert(self, token):
        self.tokenPool.append(token)
    
    def has(self, component, infoString):
        for token in self.tokenPool:
            if (token.getComponent() == component) and (token.getInfoString() == infoString):
                return token
            
        return None
        
    def findAndRemove(self, component, infoString):
        """ find if token exist by component and infoString
        """
        token = self.has(component, infoString)
        if token: # not None
            self.tokenPool.remove(token)

    def findAndRemoveAll(self, component, infoString):
        """ find if token exist by component and infoString
        """
        token = self.has(component, infoString)
        while (token):
            self.tokenPool.remove(token)
            token = self.has(component, infoString)

    def removeAll(self):
        del self.tokenPool[:]

    def consolidate(self):
        self.tokenPool = list(set(self.tokenPool))

    def pop(self):
        if self.tokenPool:  # not empty
            return self.tokenPool.pop()
        else:
            return None # empty

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
tokenPool.insert(token_l1hit)
tokenPool.insert(token_l1miss)
tokenPool.insert(token_l2hit)
tokenPool.insert(token_l2miss)
print("*****Simple token test:\n")
print(tokenPool)

# duplicated token
tokenPool.insert(token_l1hit)
print("*****Duplicated token test:\n")
print(tokenPool)

# remove duplicated token
tokenPool.consolidate()
print("*****Consolidate token test:\n")
print(tokenPool)

# remove a token
tokenPool.insert(token_l1hit)
print("*****Find and remove token l2cache::cacheMiss test:\n")
tokenPool.findAndRemove(l2cache, 'cacheMiss')
print(tokenPool)

# remove multiple-hit token
print("*****Find and remove all token l1cache::cacheHit test:\n")
tokenPool.findAndRemove(l1cache, 'cacheHit')
print(tokenPool)

# remove all token
print("*****remove all token test:\n")
tokenPool.removeAll()
print(tokenPool)

tokenPool.insert(token_l1hit)
tokenPool.insert(token_l1miss)
tokenPool.insert(token_l2hit)
tokenPool.insert(token_l2miss)
print("*****pop one token test:\n")
print(tokenPool.pop())
print(tokenPool.pop())
print(tokenPool.pop())
print(tokenPool.pop())
print(tokenPool.pop())
print(tokenPool.pop())