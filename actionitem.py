from test_util import Agent

class ActionItem(object):
    """ A class create/maintain/process action item
    """

    def __init__(self):
        self.owner = None
        self.action = None
        self.arg = None


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

    def __repr__(self):
        return "ai:  %s::%s" % (self.owner, self.action)

# unit test


agent = Agent("dummy")
ai = ActionItem()
ai.setOwner(agent)
ai.setAction("open")
ai.do()



    