#write a programm to find the fibinochii series of a agaiven set of numbers
fib = []
def number(n):
    count = 0
    c = 0
    if count == 0:
        a = 1
        b = 1
        yield a
        yield b
    while c < n:
        temp = a
        a = b
        b += temp
        yield b
        c += 1
for i in number(int(input())):
    print(i)

