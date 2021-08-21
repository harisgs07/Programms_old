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
    def lst(self,newnodea):
        ppp = hari(newnodea)
        ppr = self.headnode
        while  ppr.headnode:
            ppr = ppr.nextnode
        ppr.nextnode=ppp
obj = head()
obj.headnode = hari('h')
obj.headnode.nextnode = hari('a')
obj.headnode.nextnode.nextnode = hari('r')
obj.lst('k')
obj.printi()
