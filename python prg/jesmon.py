import sys
marks = sum(list(map(int,input().split())))/5
dict = {90:'S',80:'A',70:'B',60:'C',50:'Fails'}
result = [[round(marks,2),dict.get(i)] for i in dict if marks > i and marks < i+9]
print(result[0][0],' ',result[0][1])

    
