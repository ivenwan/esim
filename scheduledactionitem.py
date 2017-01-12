#!/usr/bin/env python3
from actionitem import ActionItem

class ScheduledActionItem(ActionItem):
    
    def __init__(self):
        super().__init__()
        self.delay = 0
    
    def set_delay(self, delay):
        self.delay = delay
    
    def step(self):
        self.delay = self.delay - 1
    
    def do(self):
        if self.delay == 0:
            super().do()
            self.delay = -1
        else:
            self.step()
    
    def __repr__(self):
        str = ""
        if (self.delay >= 0):
            str = str + "delay[%d] " % self.delay + super().__repr__()
        
        return str



# unit test

from test_util import Agent

agent = Agent("dummy")
ai = ScheduledActionItem()
ai.set_owner(agent)
ai.set_action("open")
ai.set_delay(4)




for i in range(0,5):
    print ("clock %d:" % i)
    ai.do()
    
    
    
    # print(ai)
