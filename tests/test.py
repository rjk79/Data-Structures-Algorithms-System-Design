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

# c = "app le"
# print (c.split(" "))

# arr = [ [1, 2], [2, 3], [3, 4], [1, 3], [6, 3] ]
# # ties are sorted in order of appearance
# arr.sort(key = lambda a: a[1])
# print (arr)

# for i in reversed(range(5)):
#     print(i)


class ListNode:
    def __init__(self, val):
        self.val = val 
        self.next = None

a = ListNode(1)
b = ListNode(2)
c = ListNode(3)
a.next = b
b.next = c

a.next, b.next, c.next = b.next, None, a.next

# head = a
# while head:
#     print (head.val)
#     head = head.next

# alphabet = [chr(i) for i in range(ord('a'), ord('a')+26)]
# for i,a in enumerate(alphabet):
#     print(a)
#     print(i)

a = [(2, 2), (2, 1)]

# heapq.heapify(a)


# trips = [[2,1,5],[3,3,7]]
# for i, v in sorted(x for n, i, j in trips for x in [[i, n], [j, - n]]):
#     print (i, v)
#     # i is time point
#     # v is change
# print("holupwayt")
#     # 1, 2  5 -2      3, 3   7 -3
# for n, i, j in trips:
#     for x in [[i, n], [j, - n]]:
#         print(x)


# print sorted(x*y for x in [y, 2, 3] for y in [1, 2])
# second for loop can reference the first loop (makes sense...)

def removeSubfolders(folder):
#       not removing subfolders in general
#       we are removing subfolders of folders that we've seen
        seen = set()
        res = []
        for f in folder:
#           i == 2: /a
            include = True
            for i in range(2, len(f)):
                if f[i] == "/" and f[:i] in seen: 
                    include = False
                if f[i] == "/": 
                    print(seen)
                    print(f[:i])
            if include: seen.add(f)
        return list(seen)
print(removeSubfolders(["/ah/al/am","/ah/al"]))

# for i in range(1, 2):
#     print (i)

class ListNode():
    def __init__(self, val):
        self.val = val
        self.next = None

a = ListNode(1)
b = ListNode(2)
c = ListNode(3)
d = ListNode(4)
a.next = b
b.next = c
c.next = d

a.next, b.next, c.next = c, d, b

# curr = a
# while curr:
#     print(curr.val)
#     curr = curr.next



a = ListNode(1)
b = ListNode(2)
c = ListNode(3)
d = ListNode(4)
e = ListNode(5)

a.next = b
b.next = c
c.next = d
# d.next = e

head = a
slow = a
fast = a
# defaults to making the 1ST half LONGER
while fast.next and fast.next.next:
    slow = slow.next
    fast = fast.next.next

newHead = slow.next 
slow.next = None

# better to make None instead of ghost node
prev = None
curr = newHead
# DONT MAKE PREV'S .next the head!!! otherwise inf loop
while curr:
    third = curr.next
    curr.next = prev
    prev = curr
    curr = third

# 0<-1-2-3
# p c t

curr = head
while curr:
    print(curr.val)
    curr = curr.next
print("working")
curr = prev
while curr:
    print(curr.val)
    curr = curr.next
# print(slow.val) 
# print(fast.val)


a = [[None for _ in range(5)] for _ in range(3)]
print(a)


print ("leetcode"[-5:3])

a = {1, 2, 3}
a.add(7)

print(a)

# doesnt touch 0
# range has step of -1
for i in range(4, 0, -1):
    print(i)

# flatten map each thing to itself or the rec if its an array
a = [[1, 2, 3], [4, 5, 6]]




def binarySearch(arr, target):
    l = 0
    r = len(arr) 
    while l < r:
        mid = (r + l) //2
        if arr[mid] == target: return mid
        elif arr[mid] < target:
            l = mid + 1
        elif arr[mid] > target:
            r = mid
    return -1

print("BSing")
print(binarySearch([1, 4, 5, 6, 8, 10], 1))
print(binarySearch([1, 4, 5, 6, 8, 10], 4))
print(binarySearch([1, 4, 5, 6, 8, 10], 5))
print(binarySearch([1, 4, 5, 6, 8, 10], 6))
print(binarySearch([1, 4, 5, 6, 8, 10], 8))
print(binarySearch([1, 4, 5, 6, 8, 10], 10))
print(binarySearch([1, 4, 5, 6, 8, 10], 0))
print(binarySearch([1, 4, 5, 6, 8, 10], 11))


def serialize(root):
        res = []
        def recurse(root):
            if not root: 
                res.append("#")
                return 
            res.append(str(root.val))
            recurse(root.left)
            recurse(root.right)
        # print(res)
        recurse(root)
        return " ".join(res)

# BT
def deserialize(data):
    data = iter(data.split(" "))

    def recurse():
#           consumes the iterable
        currVal = next(data)
        if currVal == "#":
            return None
        curr = TreeNode(int(currVal))
        curr.left = recurse()
        curr.right = recurse()
        return curr
    return recurse()



def serializeZ(root):
        """Encodes a tree to a single string.
        
        :type root: TreeNode
        :rtype: str
        """
        res = []
        def recurse(root):
            if not root: return 
            res.append(str(root.val))
                
            recurse(root.left)

            recurse(root.right)
            
        recurse(root)
        res = ",".join(res)
        return res 
            

def deserializeZ(data):
    """Decodes your encoded data to tree.
    
    :type data: str
    :rtype: TreeNode
    """
#       "213" parses data
    if data == "": return
    data = data.split(",")
    data = [int(el) for el in data]
#       i to j is searchable area
    def recurse(i, j):
        if i > j: return
        if i == j: return TreeNode(data[i])
        
        root = TreeNode(data[i])
        for k in range(i + 1, j+1):
#   if we encounter a higher val in searchable area
#   then create left and right subtree
#   if there are no lower vals then [0:0] will res in no left subtree
#   "k" is the partition
            if data[k] > data[i]:
                root.left = recurse(i + 1, k-1)
                root.right = recurse(k, j)
                return root
#   if we dont, then just create left subtree
        root.left = recurse(i+1, j)
        return root
    return recurse(0, len(data)-1)


class TreeNode:
    def __init__(self,x):
        self.val = x
        self.left = None
        self.right = None

a = TreeNode(3)
b = TreeNode(1)
c = TreeNode(2)
a.left = b
a.right = c
#       a
#      / \
#     b   c
# 
#       3
#      / \
#     1   2
# 

serial = serialize(a)
print(serial)

serial = serializeZ(a)
print(serial)

def subseqGenerator(arr): 
    res = []
    def recurse(arr, curr):
        if not arr:
            if curr: res.append(curr)
            return
        recurse(arr[1:], curr + [arr[0]]) #include
        recurse(arr[1:], curr) #dont include
    recurse(arr, [])
    return res
print("subseqs:")
print(subseqGenerator([1, 2, 4]))
# [1] [2] [4]
# [1, 2]
# [1, 4]
# [2, 4]
# [1, 2, 4]

import threading
# with threading.Semaphore(0):
# with print("helloooo"):
#     print("unlocked")

class Node:
    def __init__(self, val):
        self.val = val
dic = dict()
a = Node(1)
dic[a] = 5
b = a
print("its here", b in dic)

# path printer
def pathPrinter(edges):
    graph = collections.defaultdict(list)
    for edge in edges:
        graph[edge[0]].append(edge[1])
        if edge[1] not in graph:
            graph[edge[1]]
    memo = {}
    def dfs(node):
        # if node in memo: return memo[node]
        if not graph[node]:
            return [[node]]
        paths = []
        for neigh in graph[node]:
            for path in dfs(neigh):
                paths.append([node] + path)
        memo[node] = paths
        return paths
    res = []
    for node in graph:
        res.extend(dfs(node)) #concat
    return res
import time
start = time.time()
print(pathPrinter([[1, 2], [2, 3], [3, 4], [4, 5], [4, 6], [6, 7]]))
print("It took:", time.time() - start)
# 1 - 2 - 3 - 4 - 5
#              \ 
#               6 - 7

a = 'atactgactagctatcgatcgatctgact'

def counter(string):
    count = 0
    for char in string:
        if char == 'a':
            count += 1
    return count

print(counter(a))