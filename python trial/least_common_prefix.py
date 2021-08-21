def looks(index):
    count = 0
    for i in list_words:
        if i[:index] == min(list_words)[:index]:
            count += 1
        else:
            if index-1 > 0:
                return looks(index-1)
            else:
                return -1
    if count == len(list_words):
        return min(list_words)[:index]
test_case = int(input())
list_result = []  
for i in range(test_case):
    words = int(input())
    list_words = input().split()
    list_result.append(looks(len(min(list_words,key=len))))
print("{}\n".format(*[str(i) for i in list_result]))
    
    
    
