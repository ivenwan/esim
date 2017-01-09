from test_util import Agent

class ActionItem(object):
    """ A class create/maintain/process action item
    """

    def __init__(self):
        self.owner = None
        self.action = None
        self.arg = None


    def set_owner(self, owner):
        self.owner = owner

    def set_action(self, action):
        """ action is a function name of the owner
        """
        self.action = action

    def pass_arg(self, arg):
        self.arg = arg

    def do(self):
        result = getattr(self.owner, self.action)(self.arg)

    def __repr__(self):
        return "ai:  %s::%s" % (self.owner, self.action)

# unit test


agent = Agent("dummy")
ai = ActionItem()
ai.set_owner(agent)
ai.set_action("open")
ai.do()

    