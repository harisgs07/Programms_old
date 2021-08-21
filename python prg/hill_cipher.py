
import random, string,hill_cipher_decrypt
#inp = input('enter the text')
inp = 'act'
#key = random.sample(string.ascii_lowercase,pow(len(inp),2))
key = 'gybnqkurp'
key_vector = [string.ascii_lowercase.index(i) for i in key]
key_vector_2d = [key_vector[i*len(inp):(i+1)*len(inp)]for i in range(len(inp))]
print(*key_vector_2d,sep='\n')
msg_vector = [string.ascii_lowercase.index(i) for i in inp]
print(*msg_vector,sep='\n')
ans_vector = []
ans_div = []
for i in range(len(inp)):
    ans = 0
    for j in range(len(inp)):
        ans = ans + (key_vector_2d[i][j] * msg_vector[j])
    ans_div.append(ans/26)
    ans_vector.append(ans%26)
print(*ans_vector,sep='\n')
print(*[string.ascii_lowercase[i] for i in ans_vector],sep='')

hill_cipher_decrypt.decrypt(ans_vector,key_vector_2d)
