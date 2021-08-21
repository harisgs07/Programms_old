from itertools import combinations as c
def MaximumProduct(N):
    prdt = {}
    a = [i for i in range(N+1)]
    for i in range(2,N):
        x= c(a,i)
        for j in x:
            if sum(j) ==N:
                prdtn = 1
                for k in j:
                    prdtn = prdtn * k
                    if len(prdt) == 0:
                        prdt.update({j:prdt})
                    elif prdt[1]< prdtn:
                        prdt.__delitem__(prdt.popitem())
                        prdt.update({j:prdt})
    for i in prdt.keys():
        return len(i)
print(MaximumProduct(5))
