from argument import Argument

class Trigger(object):
    """ This is a class for trigger:
        A trigger consists of:
        - a master
        - a slave
        - Master trigger condition
        - Slave action/function call
        - Argument passed from Master to Slave for the function call
    """

    def __init__(self):
        self.master = None
        self.slave = None
        self.trigger = None # master trigger condition
        self.action = None # slave's function call
        self.arguments = Argument() # create an arg object

    def set_master(self,master):
        self.master = master

    def set_slave(self,slave):
        self.slave = slave

    def set_trigger(self,trigger):
        self.trigger = trigger

    def add_argument(self, argname, argval):
        self.arguments.insert(argname, argval)

    def new_trigger(self, master, slave, trigger):
        self.set_master(master)
        self.set_slave(slave)
        self.set_trigger(trigger)
    
    def __repr__(self):
        str = ''
        str = str + "%s triggers %s upon %s with arg %s" % (self.master, self.slave, self.trigger, self.arguments) 
        return str

# test
test_trigger = Trigger()
test_trigger.new_trigger("CacheControl", "L1DCache", "data_arrival")
test_trigger.add_argument("sharability", "inner_sharable")

print test_trigger