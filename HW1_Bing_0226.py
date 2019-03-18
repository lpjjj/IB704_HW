import math

def reverse(num_a):
    minus = 0
    if (num_a < 1):
        num_a = num_a * -1
        minus = 1

    digits = int(abs(math.log10(num_a)))+1

    sum = 0
    for a in range(digits):
        # print (num_a%(10**(a+1)))
        sum = sum + num_a%(10**(a+1))//(10**(a))*(10**(digits-a-1))
    if (minus):
        sum = sum * -1
    return sum
# print (reverse(-2245))
# # n=22244
# # digits = int(math.log10(n))+1
# # print (digits)
assert reverse(123) == 321, 'Fail'
assert reverse(-123) == -321, 'Fail'
assert reverse(120) == 21, 'Fail'
assert reverse(1534236469) == 0, 'Fail'
