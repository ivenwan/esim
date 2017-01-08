#from trigger import Trigger

class Scheduler(object):
    """ This is a Scheduler
        Scheduled event will be bookkept here
        When time comes, the scheduler will issue the command to execute
    """

    def __init__(self, name):
        self.name = name
        # default schedule actions for 3 cycles
        self.schedule = {}  # a dict
        self.schedule[0] = []
        self.schedule[1] = []
        self.schedule[2] = []
        
    
    def schedule_ai(self, cycle, action_item):
        if not cycle in self.schedule:
            self.schedule[cycle] = []

        self.schedule[cycle].append(action_item)

    def issue(self):
        # execute current action items
        if not self.schedule:
            print "empty schedule"
        if 0 in self.schedule:
            for action_item in self.schedule[0]:
                self.do(action_item)  # execute ai
        
    def do(self,action_item):
        print action_item

    # process for next cycle
    
    def step(self):
        # step forward one unit (cycle)
        self.schedule_nxt = {}
        self.issued_ai = []
        for key in self.schedule:
            if (key == 0):
                self.issued_ai = self.schedule[key]
            else:
                self.schedule_nxt[key-1] = self.schedule[key]
                # remove from exist schedule
                self.schedule[key] = None
        
        # swap the schedule and schedule_nxt
        self.schedule = self.schedule_nxt
        
# unit test
test_schedule = Scheduler("my scheduler")
test_schedule.schedule_ai(1,"Monday: go school")
test_schedule.schedule_ai(2,"Tuesday: field trip")
test_schedule.schedule_ai(3,"Wednesday: no class")

for i in range(0,10):
    test_schedule.issue()
    test_schedule.step()

