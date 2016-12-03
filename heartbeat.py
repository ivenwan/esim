from sets import Set



class Heartbeat(object):
    """Heart beat class"""
    def __init__(self, name):
        self.name = name
        self.states = Set(['low','low-high','high','high-low'])
        self.curr_state = 'low'
        self.callee = []

    def add_callee(self, caller_state, callee, trigger_msg):
        self.callee.append( (caller_state, callee, trigger_msg) )

    def pre_run(self):
        if self.curr_state == 'low':
            self.next_state = 'low-high'
        elif self.curr_state == 'low-high':
            self.next_state = 'high'
        elif self.curr_state == 'high':
            self.next_state = 'high-low'
        elif self.curr_state == 'high-low':
            self.next_state = 'low'

    def run(self):
        self.pre_run()
        self.curr_state = self.next_state
        for (caller_state, callee, trigger_msg) in self.callee:
            if self.curr_state == caller_state:
                callee.trigger(trigger_msg)
    
    def __repr__(self):
        return 'name=%s, curr_state=%s' % (self.name, self.curr_state)
        

class HeartbeatTimer(object):
    """Heart beat counter"""
    def __init__(self, name):
        self.name = name


    def add_caller(self, caller, caller_state, trigger_msg):
        caller.add_callee( caller_state, self, trigger_msg )

    def trigger(self, msg):
        print msg



#
#class Clock(object):
#    """Clock class
#    """
#    def __init__(self, name, )

heartbeat = Heartbeat('basic heart beat')
heartbeatTimer = HeartbeatTimer('heartbeat timer')
heartbeatTimer.add_caller(heartbeat, 'low-high', 'posedge')
for i in range(100):
    heartbeat.run()
    print heartbeat