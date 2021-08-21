'''
dic = {'A':[(1,2,4),(2,3),(5)],'B':[(1,2),(2,3,4)],
       'C':[(1,2),(2,3,4),(2,4,5)],'D':[(2),(3,4),(4,5)],
       'E':[(1,3),(2,4,5)]}
dic = {'A':[(30),(90)],'B':[(10,20),(30),(10,40,60,70)],
       'C':[(30,50,70,80)],'D':[(30),(30,40,70,80),(90)],
       'E':[(90)]}
minsup =int(input())

for getting items set
item = []
item1char = []
b =[]

for i in dic.values():
    r = []
    for j in i:
        if type(j) == int and :
            r.append(j)
        else:
            r.extend(j)
    b.append(list(set(r)))
print(b)
for i in b:
    for j in i:
        c = 0
        if j not in item:
            item.append(j)
            for k in b:
                if j in k :
                    c = c +1
            if len(dic.items())/ c > minsup/100:
                item1char.append(j)
print(item1char)
print(item)
'''
import operator
a = {'b':2,'a':1}
b=sorted(a.values(),reverse=True)
print(b)
