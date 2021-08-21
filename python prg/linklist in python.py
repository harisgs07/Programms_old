class hari:
    def __init__(self,data=None):
        self.data = data
        self.nextnode = None
class head:
    def __init__(self):
        self.headnode = None
    def printi(self):
        pp = self.headnode
        while pp is not None:
            print(pp.data)
            pp = pp.nextnode

obj = head()
obj.headnode = hari('h')
e1 = hari('r')
e2 = hari('a')
obj.headnode.nextnode = e1
e1.nextnode = e2

obj.printi()
    
    
