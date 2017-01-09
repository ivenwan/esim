from argument import Argument
from actionitem import ActionItem

class ChainAction(object):
    """ This is a class for trigger:
        A trigger consists of:
        - a master
        - a slave
        - Master trigger condition
        - Slave action/function call
        - Argument passed from Master to Slave for the function call
    """

    def __init__(self, master, trigger, ai, arg):
        self.master = None
        self.slave = None
        self.trigger = None # master trigger condition
        self.ai = None # slave's function call
        self.arg = None # create an arg object
        self.set_master_trigger(master, trigger)
        self.set_slave_actionitem(ai, arg)


    def set_master_trigger(self,master, trigger):
        self.master = master
        self.trigger = trigger

    def set_slave_actionitem(self, ai, arg):
        self.ai = ai
        self.arg = arg
    
    def __repr__(self):
        str = ''
        str = str + "%s upon %s -> %s" % (self.master, self.slave, self.ai) 
        return str

# test
# unit test
class Agent(object):
    def open(self, arg):
        print ("open")
    
    def close(self, arg):
        print ("close")

dummy = Agent()


# create arg
arg = Argument()
arg.insert("sharability", "inner_sharable")
# create action item
ai = ActionItem()
ai.set_owner(dummy)
ai.set_action("open")
# create a chain-action
chain_action0 = ChainAction(dummy, "Monday", ai, arg)

print(chain_action0)