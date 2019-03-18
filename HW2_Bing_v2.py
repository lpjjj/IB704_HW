def judge(parentheses):
    begin = 1
    count = 0
    find_c= ""
    pass_c= ""
    pass_num =0
    
    total_list=len(parentheses)
    global result_a
    result_a=1
    for element in parentheses:
        # if (element = "(" or element = "[" or element = "{")
        # print (str(begin) + element)
        if (begin):
            # print (element)
            if (element == ")" or element == "}" or element == "]"):
                # print ("shshshsh")
                result_a = 0
            if (element == "("):
                # parentheses.remove("(")
                find_c = ")"
                pass_c = "("
                pass_num = 1
                begin = 0
                index_i = count
            elif (element == "["):
                # parentheses.remove("[")
                find_c = "]"
                pass_c = "["
                pass_num = 1
                begin = 0
                index_i = count
            elif (element == "{"):
                # parentheses.remove("{")
                find_c = "}"
                pass_c = "{"
                begin = 0
                pass_num = 1
                index_i = count
        else:
            # print ("final:count",count+1,"final:total_list",total_list)
            # print ("element",element,"find_c",find_c,"pass_c",pass_c)
            if (element == find_c):
                # print (element+str(count))
                pass_num = pass_num -1
                if (pass_num == 0):

                    if (index_i+1 == count ):
                        # print ("aa")
                        # print ("i:"+str(count+1)+",f:"+str(total_list))
                        # print (parentheses[count+1:total_list])
                        judge(parentheses[count+1:total_list])
                        break
                    else:
                        # print ("bb")
                        # print ("i:"+str(index_i+1)+",f:"+str(count))
                        # print (parentheses[index_i+1:count])
                        # print ("i:"+str(count+1)+",f:"+str(total_list))
                        # print (parentheses[count+1:total_list])
                        judge(parentheses[index_i+1:count])
                        judge(parentheses[count+1:total_list])
                        break

                    # return "finnd_c@:"+str(count)
            elif (element == pass_c):
                pass_num = pass_num +1
        
        if (count+1 == total_list and pass_num != 0):
            # print ("final:count",count,"final:total_list",total_list)
            result_a = 0
        # print ("final:count",count+1,"final:total_list",total_list)
        # print (pass_num)
        count = count +1
        # if (element = ")" or element = "]" or element = "}")
    # print (pass_num)
    if (result_a):
        return True
    else:
        return False
# words1 = "{"

# words1 = "{{{{"

# words1 = "[(()aaaa)()(){([])[]}[]{}]"

# result_a = 1
# words1 = "((){}})"
# print (words1[1:2])
# print (judge(words1))
# print ([i for i,v in enumerate(words1) if v=="("])
assert judge('[') is False, 'Fail'
assert judge(')') is False, 'Fail'
assert judge('()') is True, 'Fail'
assert judge('()[]{}') is True, 'Fail'
assert judge('())(') is False, 'Fail'
assert judge('(]') is False, 'Fail'
assert judge('([)]') is False, 'Fail'
assert judge('{[]}') is True, 'Fail'