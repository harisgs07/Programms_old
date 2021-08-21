from itertools import permutations
'''transactions = [['l1', 'l2', 'l5'], ['l2', 'l4'], ['l2', 'l3'],
                ['l1', 'l2', 'l4'], ['l1', 'l3'], ['l2', 'l3'], ['l1', 'l3'],
                ['l1', 'l2', 'l3', 'l5'], ['l1', 'l2', 'l3']]

transactions = [['beef', 'chicken', 'milk'], ['beef', 'cheese'], ['cheese', 'boots'],
                ['beef', 'chicken', 'cheese'], ['beef', 'chicken', 'clothes', 'cheese', 'milk'],
                ['chicken', 'clothes', 'milk'], ['chicken', 'milk', 'clothes']]'''


'''transactions = [['milk','egg','bread','butter'],['milk','butter','egg','ketchup'],['bread','butter','ketchup']
                    ,['milk','bread','butter'],['bread','butter','cookies'],
                ['milk','bread','butter','cookies'],['milk','cookies'],['milk','bread','butter'],
                ['milk','butter','egg','cookies'],['milk','butter','bread']
                ,['milk','bread','butter'],['milk','bread','cookies','ketchup']]'''

'''transactions = [[1,3,4],[2,3,5],[1,2,3,5],[2,5]]'''

'''--for dynamic input of transaction---
num_transaction = int(input('Enter the number of transactions '))
transactions = [list(map(int,input().split(' '))) for n in range(num_transaction)]'''

mins = int(input('Enter the minimum support'))
minc = int(input('Enter the minimum confidentiality'))

print("\nTRANSACTIONS\n")
print(*['t{} = {}\n'.format(i+1,transactions[i]) for i in range(len(transactions))])
c, m, items1, items = dict(),dict(), set(), []

for j in transactions:
    for i in j:
        count = 0
        if i not in items:
            items.append(i)
        for k in transactions:
            if items[-1] in k:
                count += 1
        if items[-1] not in c.keys():
            c.update({items[-1]:count})
            print('%10s%10.2f ACCEPTED'%(items[-1],c.get(items[-1])/len(transactions)*100) if c.get(items[-1])/len(transactions)*100 >= mins else
          '%10s%10.2f '%(items[-1],c.get(items[-1])/len(transactions)*100) )
print('ITEMS = ',items,'\n')        

print("CONFIDENTIALITY\n")
for i in items:
    if c.get(i)/len(transactions)*100 >= mins:
        for j in items:
            count = 0
            if i != j:
                for k in transactions:
                    if i in k and j in k:
                        count += 1
                confidence = count/c.get(i) * 100
                if '{}:{}'.format(i,j) not in m.keys() and '{}:{}'.format(j,i) not in m.keys() and confidence >= minc:
                    items1.add(i)
                    items1.add(j)
                    m.__setitem__('{}:{}'.format(i,j),confidence)
                    print('%10s%10s%10.2f ACCEPTED'%(i,j,confidence))
                else:
                  print('%10s%10s%10.2f '%(i,j,confidence) )

m.clear()
print("Further More Steps for finding Support and Confidintiality check")
for i in range(len(items1)-1):
    if i > 0:
        x = permutations(items1,i+1)
        for j in x:
            for u in range(1,len(items1-set(j))+1):
                y = permutations(items1-set(j),u)    
                for yh in y:
                    value= 0
                    count = 0
                    coo = set(yh).union(set(j))
                    for k in transactions:
                        if coo.issubset(set(k)):
                            value += 1
                        if set(j).issubset(set(k)):
                            count += 1
                    if count != 0:
                        if value/len(transactions) * 100 >= mins:
                            confidence = value/count *100
                            if '{}---{}'.format(set(j),set(yh)) not in m.keys():
                                m.update({'{}---{}'.format(set(j),set(yh)):confidence})     
    else:
        for j in items1:
            for u in range(2,len(items1-set([j]))+1):
                y = permutations(items1-set([j]),u)    
                for yh in y:
                    count = 0
                    coo = set(yh).union(set([j]))
                    for k in transactions:
                        if coo.issubset(set(k)):
                            count += 1
                    if count/len(transactions) * 100 >= mins:
                        confidence = count/c.get(j) * 100
                        if '{}---{}'.format(set([j]),set(yh)) not in m.keys():
                            m.update({'{}---{}'.format(set([j]),set(yh)):confidence})
for i in m.keys():
    print('{} {} ACCEPTED'.format(i,m.get(i)) if m.get(i) > minc else '{} {}'.format(i,m.get(i)))

'''\nFinal_assosiation'''
print('final assosiation')
for i in m.keys():
    if m.get(i) > minc-1:
        print('%10s%10s ACCEPTED'%(i,m.get(i)))
