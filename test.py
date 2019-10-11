# def banana():
#     arr = [1, 2, 3]
#     res = [0 for i in range(len(arr))]
#     print (res)

# (banana())

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