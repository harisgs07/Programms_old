from itertools import combinations
items = ['beef', 'chicken', 'milk', 'cheese', 'boots', 'clothes']
transactions = [['beef', 'chicken', 'milk'], ['beef', 'cheese'], ['cheese', 'boots'],
                ['beef', 'chicken', 'cheese'], ['beef', 'chicken', 'clothes', 'cheese', 'milk'],
                ['chicken', 'clothes', 'milk'], ['chicken', 'milk', 'clothes']]
print('ITEMS = ',items,'\n')
print("TRANSACTIONS\n")
print(*['t{} = {}\n'.format(i+1,transactions[i]) for i in range(len(transactions))])
c = dict()
for j in transactions:
    for i in range(len(j)):
        count = 0
        for k in transactions:
            if j[i] in k:
                count += 1
        if j[i] not in c.keys():
            c.update({j[i]:count})
            
print("SUPPORT\n")
for i in items:
    print('{} {} ACCEPTED'.format(i,c.get(i)/len(transactions)*100) if c.get(i)/len(transactions)*100 > 30 else '{} {} REJECTED'.format(i,c.get(i)/len(transactions)*100) )
    
print("\nCONFIDENTIALITY\n")    
for i in items:
    if c.get(i)/len(transactions)*100 > 30:
        for j in items:
            count = 0
            a=[]
            if i != j:
                a.extend([i,j])
                g = tuple(a)
                for k in transactions:
                    comb = combinations(k,2)
                    for cc in comb:
                        if cc == g:
                            count += 1
                confidence = count/c.get(i) * 100
                print('{} :{} {} Accepted'.format(g[0],g[1],confidence) if confidence > 79 else '{} :{} {} Rejected'.format(g[0],g[1],confidence))  
            
                
            
    
