import math

def num_reverse_to_list(num_a):
    minus = 0


    digits = int(abs(math.log10(num_a)))+1

    sum = []
    for a in range(digits):
        # print (num_a%(10**(a+1)))
        sum.append(num_a%(10**(a+1))//(10**(a)))
    # print (sum)
    return sum

def reverse_list(l1,l2):
    n1=0
    n2=0
    l1_tot = 0
    l2_tot = 0
    for num1 in l1:
        l1_tot = l1_tot + num1*10**n1
        n1=n1+1
    for num2 in l2:
        l2_tot = l2_tot + num2*10**n2
        n2=n2+1
    # print ("l1_tot",l1_tot)    
    # print ("l2_tot",l2_tot)
    l3_tot = l1_tot + l2_tot
    return num_reverse_to_list(l3_tot)      

l1 = [1,2,3]
l2 = [9,9,8]
# print (reverse_list(l1,l2))
assert reverse_list(l1,l2) == [0,2,2,1], 'Fail'
# print (reverse(223))
