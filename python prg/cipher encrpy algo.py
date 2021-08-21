'''play cipher encryption algorithm

1.get the key and text from the user
2.split the text give into pair and store to a list
  while spliting
  a. store the position of the space
3.insert each element of key to the matrix if any repatition is there then
  we need to replace the letter with another value.
  during insertion check whether the input text is havinng  i or the j
  if i then i if j then j if both i dont know
4.check whether the given pair is in
 a.same row:
 shift right side and store the values

 b.same column:
 shift downwards and store the values
 
 c.else: different
 cretae a imaginary rectangle with the pairs as there vertex at opposite side
 then ineterchange them with opposite diagonal verices
5.print them

'''
pp = {'d':565}
l = [1,23,3]
def h(*j,**p):
    print(str(p.values))
h(l,i = 899)
