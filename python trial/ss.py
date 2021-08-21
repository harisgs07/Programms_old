import operator as op
a = {'s':2,'f':1}
b = {'p':4,'o':3}
d = dict()
a.update(b)
print(a)
print(sorted(a.items(),key = op.itemgetter(0),reverse = True))
d= a.copy()
print(d)
'''if itr < len(key):
            if key[itr] == 'i' or key[itr] == 'j':
                a=['i','j']
                alphbts.remove('i')
                alphbts.remove('j')
                if 'j' in key:
                    key.remove('j')
                itr += 1
            else:
                a.append(key[itr])
                alphbts.remove(key[itr])
                itr += 1
                
        else:
            if alphbts[itralphbts] == 'i' or alphbts[itralphbts] == 'j' :
                a=['i','j']
                alphbts.remove('i')
                alphbts.remove('j')
            else:
                a=alphbts[itralphbts]
                itralphbts += 1''''
