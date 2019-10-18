# def banana():
#     arr = [1, 2, 3]
#     res = [0 for i in range(len(arr))]
#     print (res)

# (banana())
# TEST TEST TEST TEST TEST TEST TEST
# import pdb; pdb.set_trace()















import itertools
import collections
import re
# print (collections.Counter("abcdaeabc").most_common(1)[0][0])
print (dict(collections.Counter("abcdaeabc")).items())
# Counter({'a': 2, 'c': 2, 'b': 2, 'e': 1, 'd': 1})
print ([list(g) for k, g in itertools.groupby('aaabbbcdefghiabc')])

# [['a', 'a', 'a'], ['b', 'b', 'b'], ['c'], ['d'], ['e'], ['f'], ['g'], ['h'], ['i'], ['a'], ['b'], ['c']]

print (re.match(".+", "a"))

# print(0b10001 ^ 0b10000)

print(bin(~10010))

# b = [1, 2, 3]
# print(map(lambda a: a + 1, b))
print bin(38)

# print int("0110101", 2)
# print int("1011010", 2)

c = "app le"
print (c.split(" "))

arr = [ [1, 2], [2, 3], [3, 4], [1, 3], [6, 3] ]
# ties are sorted in order of appearance
arr.sort(key = lambda a: a[1])
print (arr)

for i in reversed(range(5)):
    print(i)