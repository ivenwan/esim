from heartbeat import Heartbeat
from timer import Timer

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