num = int(input("input n:"))
inputs =input("Input numbers from 1 to n:")
print('missing number is:',*[i for i in range(1,num+1) if str(i) not in inputs])
