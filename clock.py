from component import Component

class Clock(Component):
    """This is a basic clock class
    """

    def __init__(self, name, low_cnt, high_cnt):
        # call base class
        Component.__init__(self)
        self.name = name
        self.states = {"stop", "low", "low-high", "high", "high-low"}
        self.actions = {"reset","start", "stop", "tick"}
        self.reset_cnt()
        self.curr_state = "stop"
        self.low_max = low_cnt
        self.high_max = high_cnt
        self.scheduled_message = []
        self.outbound_mailbox = []

    def reset_low_cnt(self):
        self.low_cnt = 0
    
    def reset_high_cnt(self):
        self.high_cnt = 0

    def incr_low_cnt(self):
        self.low_cnt = self.low_cnt + 1

    def incr_high_cnt(self):
        self.high_cnt = self.high_cnt + 1

    def reset_cnt(self):
        self.reset_low_cnt()
        self.reset_high_cnt()


    def start(self):
        # start freshly only if now is in stop
        if self.curr_state == "stop":
            self.reset_cnt()
            self.curr_state = "low_high"
        #take no effect is already !stop

    def tick(self):
        # do nothing if stop
        if (self.curr_state == "stop"):
            return
        
        # determine next state
        if (self.curr_state == "low"):
            self.incr_low_cnt()
            if not self.low_cnt < self.low_max:
                self.set_next_state("low_high")  

        if (self.curr_state == "high"):
            self.incr_high_cnt()
            if not self.high_cnt < self.high_max:
                self.set_next_state("high_low")  

        if (self.curr_state == "low_high"):
            self.reset_cnt()
            self.set_next_state("high")

        if (self.curr_state == "high_low"):
            self.reset_cnt()
            self.set_next_state("low")
            
        # next state becomes current
        self.update_state()

    def schedule_mail_for_slave(self, master_trigger_state, mail, slave):
        scheduled_mail = (master_trigger_state, mail, slave)
        self.postoffice.append(scheduled_mail)

    def prepare_current_mail(self):
        for (master_trigger_state,mail,slave) in self.scheduled_message:
            if self.curr_state == master_trigger_state:
                self.delivery_bin.append((mail,slave))

    def send_mail_to_slave(self):
        for (mail,slave) in self.curr_message:
            slave.mailbox.append((self,mail))
        
            
        


    def stop(self):
        self.curr_state = "stop"

    def __repr__(self):
        return 'name=%s curr_state=%s low_cnt=%d high_cnt=%d' % (self.name, self.curr_state, self.low_cnt, self.high_cnt)

myclock = Clock("testclock",5,5)
myclock.start()
for i in range(50):
    myclock.tick()
    print myclock
#    def set_next_state(self, n_state):
#        self.next_state = n_state

#    def update_state(self):
#        self.curr_state = self.next_state
