text= list(input(''))
matrix = [[text[(j*4)+i] for i in range(4)] for j in range(4)]
print([f'*{i}\n' for i in matrix])
key={}
import random
c = 0 
while len(key)<4:
    a = random.randint(1,4)
    if a not in key.values():
        c += 1
        key.update({c:a})
print(key)
