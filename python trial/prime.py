import math
list_a = []
number = int(input())
for i in range(2,number):
    list_a.append(i)
for i in range(2,math.floor(math.sqrt(number))+1):
    for j in range(2,math.ceil(number/i)):
        if i*j in  list_a:
            list_a.remove(i * j)
print(list_a)

