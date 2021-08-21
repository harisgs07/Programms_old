'''class decrypt(ans_vector,ans_div,len(inp)):
    ans_decrypt = []
    ans_decrypt.append([(ans_div[i] * 26 )+ans_vector[i] for i in range(len(inp))])
    print(*ans_decrypt,sep='\n')'''
import string
class decrypt():
    def __init__(self,ans_vector,key_vector_2d):
        decrypt_ans_vector = []
        decrypt_ans_vector1 = []
        inverse_key_vector = [[key_vector_2d[j][i] for j in range(len(ans_vector))]for i in range(len(ans_vector))]
        print(*inverse_key_vector,sep='\n')
        for i in range(len(ans_vector)):
            ans1 = 0
            for j in range(len(ans_vector)):
                print(inverse_key_vector[i][j])
                print(ans_vector[j])
                ans1 = ans1 + (inverse_key_vector[i][j] * ans_vector[j])
            decrypt_ans_vector.append(ans1%26)
            print(decrypt_ans_vector)
            decrypt_ans_vector1.append(ans1)
        print(*decrypt_ans_vector1,sep='\n')
        print(*decrypt_ans_vector,sep='\n')
        print(*[string.ascii_lowercase[i] for i in decrypt_ans_vector],sep='')
            
        
                
            
        
        
    
    
    
    
