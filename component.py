class Component(object):
    """basic component class """
    def __init__(self):
        self.callee = None
        self.curr_state = None
        self.next_state = None
    
    def pre_run(self):
        return
    
    def run(self):
        self.pre_run()
        self.curr_state = self.next_state
        for (caller_state, callee, trigger_msg) in self.callee:
            if self.curr_state == caller_state:
                callee.trigger(trigger_msg)
        
    def add_callee(self, caller_state, callee, trigger_msg):
        self.callee.append( (caller_state, callee, trigger_msg) )

    
    def add_caller(self, caller, caller_state, trigger_msg):
        caller.add_callee( caller_state, self, trigger_msg )

    def trigger(self, msg):
        return