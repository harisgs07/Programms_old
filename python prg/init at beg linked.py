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
    def beg(self,newnodea):
        ppp = self.headnode
        self.headnode = hari(newnodea)
        self.headnode.nextnode = ppp
obj = head()
obj.headnode = hari('h')
obj.headnode.nextnode = hari('a')
obj.headnode.nextnode.nextnode = hari('r')
ep=hari('k')
obj.beg(ep)
obj.printi()
    
