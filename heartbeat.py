from component import Component
from sets import Set




class Heartbeat(Component):
    """Heart beat class"""
    def __init__(self, name):
        Component.__init__(self)
        self.name = name
        self.states = Set(['low','low-high','high','high-low'])
        self.curr_state = 'low'
        self.callee = []

    def pre_run(self, msg):
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
        

class Timer(Component):
    """Timer class"""
    def __init__(self, name, timer, debug):
        Component.__init__(self)
        self.name = name
        self.timer = timer
        self.repeat = True
        self.cnt = 1
        self.curr_state = 'stop'
        self.debug = debug

    def start(self):
        self.curr_state = 'run'

    def set_repeat(self,repeat):
        self.repeat = repeat

    def pre_run(self, msg):
        self.next_state = self.curr_state  #default
        if (self.curr_state == 'stop'):
            return

        if (self.curr_state == 'run'):
            if (msg == 'tick'):
                self.cnt = (self.cnt+1) % (self.timer+1)  
            self.next_state = 'triggered' if (self.cnt == self.timer) else self.curr_state
      
        if (self.curr_state == 'triggered'):
            if (self.repeat):
                self.next_state = 'run'
                self.cnt = 1
            else:
                self.next_state = 'stop'


    def __repr__(self):
        return 'name=%s, curr_state=%s timer=%s cnt=%s' % (self.name, self.curr_state, self.timer, self.cnt)

    def trigger(self,msg):
        if (self.debug):
            print self
        Component.trigger(self, msg)
#
#class Clock(object):
#    """Clock class
#    """
#    def __init__(self, name, )

timerDebug = True
heartbeat = Heartbeat('basic heart beat')
heartbeatTimer = Timer('heartbeat timer', 5, timerDebug)
heartbeatTimer.set_repeat(False)
heartbeatTimer.set_repeat(True)

heartbeatTimer.add_caller(heartbeat, 'low-high', 'tick')
heartbeatTimer.start()
for i in range(50):
    heartbeat.trigger('none')
    #print heartbeat