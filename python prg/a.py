def a(b,c):
    return [True if len(set(b) & set(c)) != 0 else False]
print(*a([1,2,3],[4,3,6]))
