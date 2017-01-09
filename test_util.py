

# unit test
class Agent(object):
    def __init__(self,name):
        self.name = name

    def open(self, arg):
        print ("I am openning")
    
    def close(self, arg):
        print ("I am closing")

    def __repr__(self):
        return self.name
