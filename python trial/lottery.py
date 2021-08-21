import random
lottery_number = set(random.sample(range(22),6))
numbers_matched, position_save = [], []
lottery_name = [
    {'name':'rolf','numbers':{1,3,5,7,9,11}},
    {'name':'charlie','numbers':{2,7,9,22,10,5}},
    {'name':'anna','numbers':{13,14,15,16,17,18}},
    {'name':'joe','numbers':{19,20,12,7,3,5}}
               ]

'''for loop to get lottery_numbers of each players and compare
    it with the drawn lottery-number to know how many common
    number are for each person and they are stored in numbers_matched'''
'''for i in lottery_name:
    check_numbers = i.get('numbers')
    numbers_matched.append(len(check_numbers.intersection(lottery_number)))'''

   
'''to find the maximum number matched and also check whether
   multiple players got same number of matched element and save their positions
for i in numbers_matched:
    if i == max(numbers_matched):
        position_save.append(numbers_matched.index(i))


''By using the position name of the player is selected from lottery_name''
for i in position_save:
    print(*"[{} won {}".format(lottery_name[i].get('name'),100 ** max(numbers_matched)) for i in position_save])   
'''          

            
    
    
