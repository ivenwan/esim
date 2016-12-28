from component import Component
        

class Timer(Component):
    """
    Timer class
    
    """
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
