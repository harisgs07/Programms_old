import random

lottery_number = set(random.sample(range(22), 6))

lottery_name = [
    {'name': 'rolf', 'numbers': {1, 3, 5, 7, 9, 11}},
    {'name': 'charlie', 'numbers': {2, 7, 9, 22, 10, 5}},
    {'name': 'anna', 'numbers': {13, 14, 15, 16, 17, 18}},
    {'name': 'joe', 'numbers': {19, 20, 12, 7, 3, 5}}
]

numbers_matched = [len(i.get('numbers').intersection(lottery_number)) for i in lottery_name]

position_save = [ numbers_matched.index(i) for i in numbers_matched if i == max(numbers_matched)]

print(*["{} won {}".format(lottery_name[i]['name'],100 ** max(numbers_matched)) for i in position_save])
