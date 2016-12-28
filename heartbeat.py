from component import Component
from sets import Set




class Heartbeat(Component):
    """Heart beat class"""
    def __init__(self, name):
        Component.__init__(self)
        self.name = name
        self.states = Set(['low','low-high','high','high-low'])
        self.curr_state = 'low'
        self.slave = []

    def pre_run(self, cmd):
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
        
