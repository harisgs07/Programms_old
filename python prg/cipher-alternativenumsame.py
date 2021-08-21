text=list(input('enter the palin text'))
cipher_text = []
cipher_text1=[]
cipher_text1.append(text[0::2])
cipher_text1.append(text[1::2])
cipher_text.extend(text[0::2])
cipher_text.extend(text[1::2])
print(cipher_text)
