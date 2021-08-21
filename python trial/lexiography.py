'''
#prgm:lexiography using permutations

import itertools
test_case = int(input())
string1 = str(input())
string1 = string1.upper()
string2 = str(input())
string2 = string2.upper()
x=itertools.permutations(string1)
y=itertools.permutations(string2)
print(*sorted([''.join(i) for i in x]))
print(*sorted([''.join(i) for i in y]))


#prgram for rain_water harvesting:

def left(low,high,height,tank):
    if len(height[low:high]) == 1:
        if max(height[low:high]) < height[1]:
           return tank
    else:
        tank_cap = []
        height_min = []
        temp_height = height[low:high]
        temp_len = high
        high = temp_height.index(max(temp_height))
        if high == low:
            breadth_tank = abs(temp_len - high -1)
            tank_cap.append(temp_height[high] * breadth_tank)
            for i in height[high+1:temp_len]:
                if i > 0:
                    height_min.append(i)
            tank = tank + tank_cap[-1]-sum(height_min)
            return tank
        else:
            breadth_tank = abs(temp_len - high -1)
            tank_cap.append(temp_height[high]* breadth_tank)
            for i in height[high+1:temp_len]:
                if i > 0:
                    height_min.append(i)
            tank = tank + tank_cap[-1]-sum(height_min)
            return left(0,high,height,tank)
        return tank

def right(low,high,height,tank):
    if len(height[low+1:high]) == 1:
        if max(height[low+1:high]) < height[-2]:
           return tank
    else:
        tank_cap = []
        height_min = [] 
        temp_len = low
        low = height.index(max(height[low+1:high]))
        if low == high-1:
            breadth_tank = abs(low - temp_len -1)
            tank_cap.append(height[low] * breadth_tank)
            for i in height[temp_len+1:low]:
                if i > 0:
                    height_min.append(i)
            tank = tank + tank_cap[-1]-sum(height_min)
            return tank
        else:
            breadth_tank = abs(low - temp_len -1)
            tank_cap.append(height[low] * breadth_tank)
            for i in height[temp_len+1:low]:
                if i > 0:
                    height_min.append(i)
            tank = tank + tank_cap[-1]-sum(height_min)
            return right(low,len(height),height,tank)
        return tank
    
c, d = 0, 0
length = int(input())
height = list(map(int,input().split()))[:length]
if height.index(max(height)) == 0:
    d = right(height.index(max(height)),len(height),height,0)
elif height.index(max(height)) == len(height)-1:
    c = left(0,height.index(max(height)),height,0)
else:
    c = left(0,height.index(max(height)),height,0)
    d = right(height.index(max(height)),len(height),height,0)

print(c+d)

'''

#train platforms
import operator as o
no_trains = int(input())
timings = list(zip(list(map(int,input().split())),list(map(int,input().split()))))
timings.sort(key=o.itemgetter(0))
print(timings)
a = timings.index(min(timings,key=o.itemgetter(0)))
print(a)
    


