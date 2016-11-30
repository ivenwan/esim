class Tick(object):
	"""Global reference tick"""
	def __init__(self, name, period):
		self.name = name
		self.tick = 0
		self.period = period
		self.triggees = {}
		for i in range(0,period-1):
			self.triggees[i] = [] # dict
	
	def add_triggee(self, triggee, tick, msg):
		self.triggees[tick].append(tuple([triggee, msg]))
	
	def run(self):
		self.tick += 1
		if self.tick in self.triggees.keys():
			for (triggee, msg) in self.triggees[self.tick]:
				triggee.run(msg)
			
		if self.tick == self.period:
			self.tick = 0
		
	def __repr__(self):
		# return 'name=%s tick=%s' % (self.name, self.tick)
		return '.(%s)' % self.tick
		
tick = Tick('reference_tick',10)

class Clock(object):
	"""Clock class
	"""
	def __init__(self, name, trigger, high_ticks, low_ticks, offset):
		self.name = name
		self.trigger = trigger
		trigger.add_triggee(self, high_ticks, "go_high")
		trigger.add_triggee(self, low_ticks, "go_low")
		
		self.high_ticks = high_ticks
		self.low_ticks = low_ticks
		
		self.triggees = {}
		self.phases = ['posedge', 'negedge', 'setup', 'hold']
		for x in self.phases:
			self.triggees[x] = []
		
		self.phase = None
	
	def add_triggee(self, triggee, phase, msg):
		self.triggees[phase].append(tuple([triggee,msg]))
		
	def run(self, msg):
			
		if msg == 'go_high':
			self.phase = 'posedge'
			print "^"
			
		if msg == 'go_low':
			self.phase = 'negedge'
			print "v"
			
		# trigger all triggee for that phase
		for (triggee,msg) in self.triggees[self.phase]:
			triggee.run(msg)
				
	
	def __repr__(self):
		return 'name=%s high=%s low=%s' % (self.name, self.high_ticks, self.low_ticks)

clock0 = Clock('clock0', tick, 4, 8, 2)
for i in range(100):
	tick.run()
	print(tick)	
		


		
class Action(object):
	def __init__(self, name):
		self.name = name
	
	def run(self):
		print "%s" % (self.name)

	def __repr__(self):
		return 'Action[%s]' % self.name

class Todo(object):
	def __init__(self, name, trigger, action, ):
		"""todo: condition -> action"""
		self.name = name
		self.trigger = trigger
		trigger.add_triggee(self)
		self.action = action
		
	def triggered(self):
		self.run()
	
	def run(self):
		self.action.run()
	
	def __repr__(self):
		return 'Todo[%s]: Trigger[%s] -> %s' % (self.name, self.trigger, self.action)
		

todo_shopping = Todo('shopping', timer3, Action('buy something'))
print todo_shopping

#reset
for i in range(100):
	tick.run()
	print(tick)




# Schedule( Next cyle, True, [Assert Signal])
# Schedule( In 2 cycles, [Send Req], if cond)
# Schedule( In 2 cycles, [Accept Req], True)

# Single: Assert Signal
#       | Deassert Signal
#       | Read
#       | Write

# Action: 
#         |Single
#         |Single [Action]
#         |ConditionalAction [Action]
#         |Timer=>Action [Action]

# An action is a list of tasks

# Accept Req: 
# if Req==True && has_room => (next cycle, [Assert Ack];
# if Req==False => (next cycle, [Deassert Ack]);


		
class Adder(object):
	"""Adder class
	"""
	
	def __init__(self, name):
		self.name = name
		self.inputs = {}
		self.inputs['a'] = None
		self.inputs['b'] = None
		self.eval = None

	def hook(self, pin_in, input):
		self.inputs[pin_in] = input

	def execute(self):
		if self.inputs['a'] == None:
			a = 0
		else:
			a = self.inputs['a'].eval
		if self.inputs['b'] == None:
			b = 0
		else: 
			b = self.inputs['b'].eval
		self.eval = a+b
		
	def __repr__(self):
		return 'name=%s(%s) input[a=%s b=%s]' % (self.name,  self.eval, self.inputs['a'], self.inputs['b']) 


	
from random import randint
class RandVal(object):
	"""Random event
	"""
	
	def __init__(self, name, min, max):
		self.name = name
		self.min = min
		self.max = max
		self.eval = None
		
	
	def execute(self):
		self.eval = randint(self.min,self.max)
		
	
	def __repr__(self):
		return '%s(%s)' % (self.name, self.eval)
	

		


rand_a = RandVal("rand_a",0,5)
rand_b = RandVal("rand_b",0,10) 
adder0 = Adder("Adder")




adder0.hook('a',rand_a)
adder0.hook('b',rand_b)

for i in range(10):
	rand_a.execute()
	rand_b.execute()
	adder0.execute()
	print(adder0)

