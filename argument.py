class Argument(object):
    """ This is a class for passing arguments
    """

    def __init__(self):
        self.arglist = {} # empty dict
    
    def insert(self, argname):
        """ insert an argname with no argval (True)
        """
        self.insert(argname, True)

    def insert(self, argname, argval):
        """ insert an arg dict entry {argname:argval}

        """
        self.arglist[argname] = argval

    def remove(self, argname):
        del self.arglist[argname]

    def get(self,argname):
        """ no argname -> None
            otherwise, return the argval
        """
        return self.arglist[argname]
    
    def has(self, argname):
        """check if contain an argname
        """
        if (sef.arglist[argname] == None):
            return False
        return True 

    def __repr__(self):
        str = ''
        for argname in self.arglist:
            str = str + "[%s: %s]\n" % (argname, self.arglist[argname])
        return str


# test
test_args = Argument()
test_args.insert('id', 5)
test_args.insert('parent', 'John')

print(test_args)