import random
from string import ascii_lowercase as alc
num = random.randint(4,6)
alphbts = [i for i in alc]
alphbts_temp = alphbts
random.shuffle(alphbts_temp)
key = alphbts_temp[0:num]

index_values = []                                              # index values stored for space
index_repeat ={}
max_val = 0
text_main = input()
text = list(text_main)
print(key)
cipher_text = []                                               # encrpted_text is stored
i_j = []                                                       # storing i and j format

'''index of space are found and append to a list_variable'''
for i in range(len(text)):
    if ' ' in text:
        index_values.append(text.index(' '))
        text.remove(' ')
    else:
        break
    
a, b, text_divide = [], [], []
fun = [key,alphbts]

'''placing the key elements and other letters in a 5*5 matrix'''
def h(itr):
    for i in itr:
        if i not in a:
            if i=='i' or i =='j':
                if ['i','j'] not in a:
                    a.append(['i','j'])
                else:
                    continue
            else:
                a.append(i)
                
'''for forming the matrix'''
for i in fun:
    h(i)
for i in range(1,6):
    b.append(a[(i-1)*5:i*5])                                    # 5*5 matix
print(*['{}\n'.format(i) for i in b])

'''dividing the palin_txt'''
for i in range(1,(len(text)//2)+1):
    text_divide.append(text[(i-1)*2:i*2])
    if text_divide[-1][0] == text_divide[-1][1]:               # checking whether the repeatition in the pair
        if text_divide[-1][1] == 'x':
            index_repeat.update({text_divide.index(text_divide[-1]):text_divide[-1][1]})
            text_divide[-1][1] = 'y'
        else:
            index_repeat.update({text_divide.index(text_divide[-1]):text_divide[-1][1]})
            text_divide[-1][1] = 'x'  
print(text_divide)

print(index_repeat) ##repeated pairs index

i0_val = []
i1_val = []

'''start encryption'''
for i in text_divide:
    if i[0] in ['i','j'] or i[1] in ['i','j']:                  #for apperance of i or j in the given plain_text        
        if i[0] in ['i','j'] and i[1] not in ['i','j']:
            i_j.append(i[0])
            if a.index(['i','j'])//5 == a.index(i[1])//5:   #row encryption for [i,j]
                max_val = (a.index(['i','j'])//5)*5
                if a.index(i[1]) == max_val -1:
                    cipher_text.append([a[a.index(['i','j'])+1],a[a.index(i[1])-4]]) #a[(a.index(['i','j'])//5-1)*5]
                elif a.index(['i','j']) == max_val -1:
                    cipher_text.append([a[a.index(['i','j'])-4],a[a.index(i[1])+1]])
                else:
                    cipher_text.append([a[a.index(['i','j'])+1],a[a.index(i[1])+1]])
                    
            elif a.index(['i','j'])%5 == a.index(i[1])%5:   #column encryption for [i,j]
                max_val = (a.index(['i','j'])%5)+20
                if a.index(i[1]) == max_val:
                    cipher_text.append([a[a.index(['i','j'])+5],a[a.index(i[1])%5]])
                elif a.index(['i','j']) == max_val:
                    cipher_text.append([a[a.index(['i','j'])%5],a[a.index(i[1])+5]])
                else:
                    cipher_text.append([a[a.index(['i','j'])+5],a[a.index(i[1])+5]])
            else:
                i0_val.extend([a.index(['i','j'])//5,a.index(['i','j'])%5])
                i1_val.extend([a.index(i[1])//5,a.index(i[1])%5])
                if i0_val[1] > i1_val[1] :
                    cipher_text.append([a[a.index(['i','j'])-(i0_val[1]-i1_val[1])],a[a.index(i[1])+(i0_val[1]-i1_val[1])]])
                else:
                    cipher_text.append([a[a.index(['i','j'])+(i1_val[1]-i0_val[1])],a[a.index(i[1])-(i1_val[1]-i0_val[1])]])
                i0_val.clear()
                i1_val.clear()
        elif i[0] in ['i','j'] and i[1] in ['i','j']:
                i_j.extend([i[0],i[1]])
                cipher_text.append([i[1],i[0]])
        else:
            i_j.append(i[1])
            if a.index(i[0])//5 == a.index(['i','j'])//5:
                max_val = (a.index(['i','j'])//5)*5
                if a.index(['i','j']) == max_val -1:
                    cipher_text.append([a[a.index(i[0])+1],a[(a.index(['i','j'])-4)]])
                elif a.index(i[0]) == max_val -1:
                    cipher_text.append([a[(a.index(i[0])-4)],a[a.index(['i','j'])+1]])
                else:
                    cipher_text.append([a[a.index(i[0])+1],a[a.index(['i','j'])+1]])
            elif a.index(i[0])%5 == a.index(['i','j'])%5:
                max_val = (a.index(['i','j'])%5)+20
                if a.index(i[0]) == max_val:
                    cipher_text.append([a[a.index(i[0])%5],a[a.index(['i','j'])+5]])
                elif a.index(['i','j']) == max_val:
                    cipher_text.append([a[a.index(i[0])+5],a[a.index(['i','j'])%5]])
                else:
                    cipher_text.append([a[a.index(i[0])+5],a[a.index(['i','j'])+5]])
            else:
                i0_val.extend([a.index(i[0])//5,a.index(i[0])%5])
                i1_val.extend([a.index(['i','j'])//5,a.index(['i','j'])%5])
                if i0_val[1] > i1_val[1] :
                    cipher_text.append([a[a.index(i[0])-(i0_val[1]-i1_val[1])],a[a.index(['i','j'])+(i0_val[1]-i1_val[1])]])
                else:
                    cipher_text.append([a[a.index(i[0])+(i1_val[1]-i0_val[1])],a[a.index(['i','j'])-(i1_val[1]-i0_val[1])]])
                i0_val.clear()
                i1_val.clear()    
                    
    elif a.index(i[0])//5 == a.index(i[1])//5:                  #row encryption
        max_val = (a.index(i[0])//5)*5
        if a.index(i[1]) == max_val -1:
            cipher_text.append([a[a.index(i[0])+1],a[(a.index(i[0])//5-1)*5]])
        elif a.index(i[0]) == max_val -1:
            cipher_text.append([a[(a.index(i[0])//5-1)*5],a[a.index(i[1])+1]])
        else:
            cipher_text.append([a[a.index(i[0])+1],a[a.index(i[1])+1]])
            
    elif a.index(i[0])%5 == a.index(i[1])%5:                    #column encryption
        max_val = (a.index(i[0])%5)+20
        if a.index(i[1]) == max_val:
            cipher_text.append([a[a.index(i[0])+5],a[a.index(i[0])%5]])
        elif a.index(i[0]) == max_val:
            cipher_text.append([a[a.index(i[0])%5],a[a.index(i[1])+5]])
        else:
            cipher_text.append([a[a.index(i[0])+5],a[a.index(i[1])+5]])
    else:
        i0_val.extend([a.index(i[0])//5,a.index(i[0])%5])
        i1_val.extend([a.index(i[1])//5,a.index(i[1])%5])
        if i0_val[1] > i1_val[1] :
            cipher_text.append([a[a.index(i[0])-(i0_val[1]-i1_val[1])],a[a.index(i[1])+(i0_val[1]-i1_val[1])]])
        else:
            cipher_text.append([a[a.index(i[0])+(i1_val[1]-i0_val[1])],a[a.index(i[1])-(i1_val[1]-i0_val[1])]])
        i0_val.clear()
        i1_val.clear()
               
print(cipher_text)

print(i_j)

cipher_text_file = []
for i in cipher_text:
    cipher_text_file.extend(i)
print(*(cipher_text_file),sep = '')
