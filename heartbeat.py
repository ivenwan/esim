from component import Component
from sets import Set




class Heartbeat(Component):
    """Heart beat class"""
    def __init__(self, name):
        self.name = name
        self.states = Set(['low','low-high','high','high-low'])
        self.curr_state = 'low'
        self.callee = []

    def pre_run(self):
        if self.curr_state == 'low':
            self.next_state = 'low-high'
        elif self.curr_state == 'low-high':
            self.next_state = 'high'
        elif self.curr_state == 'high':
            self.next_state = 'high-low'
        elif self.curr_state == 'high-low':
            self.next_state = 'low'

    def __repr__(self):
        return 'name=%s, curr_state=%s' % (self.name, self.curr_state)
        

class HeartbeatTimer(Component):
    """Heart beat counter"""
    def __init__(self, name):
        self.name = name


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
heartbeatTimer.add_caller(heartbeat, 'high-low', 'negedge')

for i in range(100):
    heartbeat.run()
    print heartbeat