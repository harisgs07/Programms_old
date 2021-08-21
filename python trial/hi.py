def ishappy(i):
        sum = 0
        while i >0:
                sum = sum + pow(i%10,2)
                i = i//10
        if sum == 1:
                return 1
        elif sum == 4:
                return 0
        else:
                ishappy(sum)
def isprime(get1,get2,get3):
        check_get3 = 0
        a = []
        for i in range(get1,get2):
                count = 0
                for j in range(2,i):
                        if j == i:
                                continue
                        else:
                                if i%j == 0:
                                        count += 1
                                        break
                if count == 0:
                        ans = ishappy(i)
                        if  ans == 0:
                                continue
                        else:
                                a.append(i)
                                check_get3 += 1
                                if check_get3 == get3:
                                        return a
        if check_get3 < get3:
                return "invalid input"
                                        
                        
                
get1 =int(input())
get2 =int(input())
get3 =int(input())
print("{}" .format(isprime(get1,get2,get3)))
        
