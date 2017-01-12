#from sets import Set

class Component(object):
    """basic component class """
    def __init__(self):
        self.slave = None
        self.curr_state = None
        self.next_state = None
        self.states = Set()

    def pre_run(self, cmd):
        """
        Use cmd as a communication mechanism to prepare what to do next in run 
        """
        return
    
    def run(self):
        self.curr_state = self.next_state
        if self.slave != None:
            for (master_state, slave, cmd) in self.slave:
                if self.curr_state == master_state:
                    slave.execute(cmd)
        
    def add_slave(self, master_state, slave, cmd):
        self.slave.append( (master_state, slave, cmd) )

    
    def add_master(self, master, master_state, cmd):
        master.add_slave( master_state, self, cmd )
        
    def execute(self, cmd):
        self.pre_run(cmd)
        self.run()
        return

    def set_next_state(self, n_state):
        self.next_state = n_state

    def update_state(self):
        self.curr_state = self.next_state   


    