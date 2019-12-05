402328-864247
# 444444 - 789999
# real range 

# Question 1
# def passwordFinder():
#     res = []
#     def recurse(curr, idx):
#         if len(curr) == 6: #RULE 1
#             if len(set(curr)) != len(curr): #RULE 3
#                 res.append("".join([str(el) for el in curr]))
#             return
#         for i in range(idx, 10): #RULE 4: 4 - 9 on 1st round. if we use 5 on this round, we start on 5 next also
#             recurse(curr + [i], i)

#     recurse([], 4)
#     res = [el for el in res if el > "402328" and el < "864247"] #RULE 2
    
                



        
    # return len(res)
# print(passwordFinder())

# Question 2:
# change RULE 3: the password must have at least one pair of duplicates where: it must be alone
def valid(string):
    for i in range(-1, len(string)-2):
        if 0 <= i < len(string):
            first = string[i]
        else:
            first = "#"
        second = string[i + 1]
        third = string[i + 2]
        if 0 <= i + 3 < len(string):
            fourth = string[i + 3]
        else:
            fourth = "#"

        if second == third and first != second and third != fourth:
            return True
    
    return False
def passwordFinder():
    res = []
    def recurse(curr, idx):
        if len(curr) == 6: #RULE 1
            if len(set(curr)) != len(curr): #RULE 3
                res.append("".join([str(el) for el in curr]))
            return
        for i in range(idx, 10): #RULE 4: 4 - 9 on 1st round. if we use 5 on this round, we start on 5 next also
            recurse(curr + [i], i)

    recurse([], 4)
    res = [el for el in res if el > "402328" and el < "864247"] #RULE 2
    res = [el for el in res if valid(el)] #modified RULE 3
        
    return len(res)

# print(valid("888001"))
# print(valid("88800"))
# print(valid("8810"))

print(passwordFinder())
