from itertools import permutations
transactions = [['beef', 'chicken', 'milk'], ['beef', 'cheese'], ['cheese', 'boots'],
                ['beef', 'chicken', 'cheese'], ['beef', 'chicken', 'clothes', 'cheese', 'milk'],
                ['chicken', 'clothes', 'milk'], ['chicken', 'milk', 'clothes']]

print("TRANSACTIONS\n")
print(*['t{} = {}\n'.format(i+1,transactions[i]) for i in range(len(transactions))])
c,m,items1,items = dict(),dict(), set(),[]
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
            print('%10s%10.2f ACCEPTED'%(items[-1],c.get(items[-1])/len(transactions)*100) if c.get(items[-1])/len(transactions)*100 > 30 else
          '%10s%10.2f REJECTED'%(items[-1],c.get(items[-1])/len(transactions)*100) )
print('ITEMS = ',items,'\n')        
    
print("\nCONFIDENTIALITY\n")    
for i in items:
    if c.get(i)/len(transactions)*100 > 30:
        for j in items:
            count = 0
            a=[]
            if i != j:
                a.extend([i,j])
                for k in transactions:
                    if i in k and j in k:
                        count += 1
                confidence = count/c.get(i) * 100
                if '{}:{}'.format(i,j) not in m.keys() and '{}:{}'.format(j,i) not in m.keys() and confidence > 79:
                    items1.add(i)
                    items1.add(j)
                    m.__setitem__('{}:{}'.format(i,j),confidence)
                    print('%10s%10s%10.2f ACCEPTED'%(i,j,confidence))
                else:
                    print('%10s%10s%10.2f '%(i,j,confidence) )

m.clear()
print("Further More Steps for finding Association")
for i in range(len(items1)-1):
    if i > 0:
        x = permutations(items1,i+1)
        for j in x:
            value, count = 0, 0
            for k in transactions:
                if set(j).issubset(set(k)):
                    count += 1
                if items1.issubset(set(k)):
                    value += 1       
            confidence = value/count *100
            if '{}---{}'.format(set(j),items1-set(j)) not in m.keys():
                m.update({'{}---{}'.format(set(j),items1-set(j)):confidence})         
    else:
        for j in items1:
            count = 0
            for k in transactions:
                if items1.issubset(set(k)):
                    count += 1
            confidence = count/c.get(j) * 100
            if '{}---{}'.format(set([j]),items1-set([j])) not in m.keys():
                m.update({'{}---{}'.format(set([j]),items1-set([j])):confidence})
for i in m.keys():
    print('{} {} ACCEPTED'.format(i,m.get(i)) if m.get(i) > 79 else '{} {}'.format(i,m.get(i)))
