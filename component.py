class Component(object):
    """basic component class """
    def __init__(self):
        self.slave = None
        self.curr_state = None
        self.next_state = None
    
    def pre_run(self, msg):
        """
        Use msg as a communication mechanism to prepare what to do next in run 
        """
        return
    
    def run(self):
        self.curr_state = self.next_state
        if self.slave != None:
            for (master_state, slave, trigger_msg) in self.slave:
                if self.curr_state == master_state:
                    slave.trigger(trigger_msg)
        
    def add_slave(self, master_state, slave, trigger_msg):
        self.slave.append( (master_state, slave, trigger_msg) )

    
    def add_master(self, master, master_state, trigger_msg):
        master.add_slave( master_state, self, trigger_msg )
        
    def trigger(self, msg):
        self.pre_run(msg)
        self.run()
        return