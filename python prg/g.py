convert_num1 = int(input())
list_print,sum_of = [],[]
num_alpha = [j for j in range(0, 10)] + [chr(i) for i in range(65, 65 + 26)]
print(num_alpha)
while (convert_num1 > 3999):
    print('Enter value less than 3999')
    convert_num1 = int(input())

dict_roman = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}

'''convertion of the numeric to the Roman character '''


def below_10(convert_num, a, b, low, mid, additional):
    if convert_num < a:
        list_print.insert(0, list(dict_roman.keys())[list(dict_roman.values()).index(low)] * int(convert_num / low))
    elif convert_num == a:
        list_print.insert(0, list(dict_roman.keys())[list(dict_roman.values()).index(low)] + list(dict_roman.keys())[
            list(dict_roman.values()).index(mid)])
    elif convert_num == b:
        list_print.insert(0, list(dict_roman.keys())[list(dict_roman.values()).index(low)] + list(dict_roman.keys())[
            list(dict_roman.values()).index(additional)])
    else:
        list_print.insert(0, list(dict_roman.keys())[list(dict_roman.values()).index(mid)] + list(dict_roman.keys())[
            list(dict_roman.values()).index(low)] * int((convert_num - mid) / low))


def finding_roman(convert_num1):
    mod_value, a, b = 10, 4, 9
    while convert_num1 > 0:
        convert_num = convert_num1 % mod_value
        convert_num1 = convert_num1 - convert_num
        if convert_num == 0:
            mod_value = mod_value * 10

        elif 0 < convert_num < 10:
            below_10(convert_num, a, b, 1, 5, 10)
            mod_value = mod_value * 10

        elif 10 <= convert_num < 100:
            below_10(convert_num, a, b, 1 * 10, 5 * 10, 100)
            mod_value = mod_value * 10

        elif 100 <= convert_num < 1000:
            below_10(convert_num, a, b, 1 * 100, 5 * 100, 1000)
            mod_value = mod_value * 10
        else:
            list_print.insert(0, list(dict_roman.keys())[list(dict_roman.values()).index(1000)] * int(convert_num / 1000))
        a = a * 10
        b = b * 10
    return list_print

return_value = finding_roman(convert_num1)
r = ''.join(return_value)
v = list(r)
print(''.join(v))
comb = set(''.join(v))
print(num_alpha.index(max(comb))+1)
loop = num_alpha.index(max(comb))
if 1 <= loop <= 3999:
    return_value.clear()
    return_value = list(finding_roman(num_alpha.index(max(comb))))
    r = ''.join(return_value)
    v = list(r)
    print(''.join(v))
    print(v)
    comb = set(''.join(v))
    loop = num_alpha.index(max(comb))
    print(loop+1)

    sum_of = [num_alpha.index(v[i]) * pow(loop+1, len(v)-1)for i in range(len(v))]
    print(sum_of)

