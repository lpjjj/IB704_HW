from collections import Counter




def Bing_duplicate(list1,k):
    #most_common(1) 代表取前一個最多重複元素的item , (2) 取前兩個.  [0][1]  一開始list, 後來轉tuple
    list2 = list1[0:k]
    # print (list2)
    if (Counter(list2).most_common(1)[0][1] >1):
        return True
    else:
        return False


assert Bing_duplicate([1,2,2,3,2,1],3) is True, 'Fail'
assert Bing_duplicate([1,3,5,6,7,8],3) is False, 'Fail'
