# Data Structures and Algorithms
This is my personal Data Structures and Algorithms study guide for coding interviews.  It is based off of what many practice websites, articles, papers, and online courses consider fundamental.

## Table of Contents
- Dynamic Programming
- Sorts / Searches
- Graphs 
- Trees
- Strings / Arrays
- Intervals
- Pathing
- Bits
- Other
- Backtracking
- Linked Lists
- Stacks / Queues


### 1. Dynamic Programming
- Signs:
  - Overlapping Subproblems 
  - Optimal Substructure (buying travel tickets)
- steps: 
  - write recursive
    - reduce args
  - draw recurse tree
    - det state
    - det old vs new state relation
  - write DP
    - inputs becomes axes (e.g 3 inputs => 3D DP)
1. **Fibonacci** - 1D: since only need prev val and prev-prev val, beginning always directly affects answer
  - Decode Ways 
  - Climbing Stairs
2. **0/1 Knapsack** - 2D: since need 2 types of vals: avail items and target val
  - Equal Subset Sum Partition
```python
def knapsack(vals, wts, W):
    dp = [[0 for _ in range(W + 1)] for _ in range(len(vals) + 1)]
    for i in range(len(dp)):
        for w in range(len(dp[0])):
            if i == 0 or w == 0:            #if you're not considering any items or you have 0 allowed wt
                dp[i][w] = 0
                                            # if curr item's wt is too large, we cant consider it for this curr wt
                                            # so just refer to val above ()
            elif wts[i - 1] > w:
                dp[i][w] = dp[i - 1][w]
            else:
                                            # max of: best val while not considering the curr item and 
                                            # val of curr item + best while not considering the curr item at the remaining weight
                dp[i][w] = max(vals[i-1] + dp[i - 1][w - wts[i - 1]], dp[i - 1][w])
    return dp[-1][-1]
```

3. **Boundless Knapsack** (can repeat items) 1D: since only need to know best val at lower weight
  - Coin Change
```python
def coinChange(self, coins: List[int], amount: int) -> int:
     max = float('inf')
                        # [0, inf, inf, inf...]
        dp = [0] + amount * [max]
                        # dont need to cover amount == 0 since we already have it in "dp"
                        # add 1 to iter up to amount
        for amt in range(1, amount + 1):
                        # add 1 since we're spending/using a coin now
                        # amt - coin can be == 0 since we need to hit 0..
                        #           use max if you would go below 0 (invalid coin option)
            dp[amt] = min([dp[amt - coin] if amt - coin >= 0 else max for coin in coins]) + 1
                        # 2 elem arr and we idx either at 0 or 1
                        # if dp.last == inf, True is 1 so then return -1
                        # if dp has a val, False is 0 so return that val
        print(dp)
        return [dp[amount], -1][dp[amount] == max]
```

4. **Longest Palindromic Subsequence** - 2D: 2 Pointers on 1 arr/str to delin a Window (Palindrome-specific)
```python
bbbab
12345
                    # 1 2 3 3 4 <-- res
                    # 0 1 2 2 3
                    # 0 0 1 1 3
                    # 0 0 0 1 1
                    # 0 0 0 0 1
n = len(s)
dp = [[0 for _ in range(n)] for _ in range(n)] 
for i in range(n): #seed the cells where i == j
    dp[i][i] = 1
for cl in range(2,n+1):           # DIAGONAL traverse
    for i in range(n - cl + 1): # "nickel"
        j = i + cl - 1  # "icicle"
        if s[i] == s[j]:
            dp[i][j] = dp[i+1][j-1] + 2   #looks LD
        else:
            dp[i][j] = 
                                # logic for break in palindrome
                                # can resume by using other squares (if doing "subsequences", can use max(L, D, LD))
return dp[0][-1]                # return TopRight
```
5. **Longest Common Substring** - 2 Pointers (1 on each arr/str), beginning might not directly affect answer
  - Longest Common Subseq (LCS)
  - Shortest Common Superseq
```python
def LCS(text1, text2):
    m = len(text1)
    n = len(text2)  

    dp = [[0 for _ in range(n + 1)] for _ in range(m + 1)]   #0 buffer
    for i in range(1, len(dp)):                 
        for j in range(1, len(dp[0])):  
            if text1[i - 1] == text2[j - 1]:                # DP is 1-indexed
                dp[i][j] = dp[i - 1][j - 1] + 1             # LeftUp + 1
            else:
                dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])  #carry through max(Left, Up)
    return dp[-1][-1]        #BottomRight
```
  - Longest Increasing Subseq (LIS)
```python
def LIS(nums):
    if not nums: return 0
    n = len(nums)
    dp = [1 for _ in range(n)]
    for i in range(n):
        for j in range(i):
            if nums[j] < nums[i]:           #   if curr val > earlier val then set dp[j] to dp[i] as long as it sets a new best
                dp[i] = max(dp[i], 1 + dp[j])
    return max(dp) 
```

- 2D array for X vs. Y "graph"
- Probability
- Memoizing: @functools.lru_cache(None)     (not dp, only similar)

### 2. Sorts and Searches
- Quick sort - worst case O(n^2)
- Merge sort - stable
- Insertion sort
- Radix sort
- Iterative B-search
```python
    lo, hi = 0, len() 
    while(lo < hi) {
    int mid = lo + (hi - lo) / 2;
    if( #Special condition passed)(optional):
        return mid; 
    if( #condition passed)
    hi = mid;
    else 
    lo = mid + 1;
    }
    return lo;
```
- bisect.bisect(iterable, target) does BS but returns idx + 1 so do - 1 after
  - can also find where to insert a target
- Reservoir Sampling
- random.random()*3#1  (0, 1, 2)

### 3. Graphs
- visited
  - separate 2D array 
  - visited = set() .add(str([xi, yj]))
- Tradeoffs
  - Adjacency matrix
  - graph
  - Class
- BFS, DFS
- Graph - BFS
  - don't use [-1] for ranges (will mess up when combined with dirs)
```python
visited = set()
dirs = []
for x, y in dirs:
    xi, yj
    if 0 <= xi < len and 0 <= yj < len
        if (xi, yj) not in visited:
```
```python
visited = set()
q = []
while q:
    q.pop
    visited.add
    for neighbor in .neighbors:
        if not in visited:
            q.append
```


### 4. Trees
- acyclic graphs
- Traversals
  - inorder gives sorted
- DFS
```
.left
.right
```
- BFS
```python
q = []
newQ = []
newQ << .left
newQ << .right
```
- Level Order
- Tries
```python
class TrieNode:
    def __init__(self):
        self.children = collections.defaultdict(TrieNode)   # makes itself {ref: TreeNode}
        self.isWord = False

class Trie:
    def __init__(self):
        self.root = TrieNode()  #abstracts away TrieNode
    def insert(self, word):
        root = self.root
        for c in word:
            root = root.children[c]  #creates the child if not there
        root.isWord = True
    def search(self, word):
        root = self.root
        for c in word:
            root = root.children.get(c)
            if not root: return False
        return root.isWord
```

- Heaps
  - heapq
    - .heapify(<arr>)
    - .heappush(<heap>, el)
    - .heappop(<heap>)
  - sorts ASC by [0] so [0][0] is the smallest val it sees
  - insert and delete are O(logn)
  - creating a heap is NOT O(nlogn) even though it's n els * logn insert time...
    - time is amortized to O(n)
  - insert => sift up
  - remove min/max => swap then sift down

### 5. Strings and Arrays
- ord() and chr()
- Kadane’s - largest contig sum in subarr
- Two pointers
- Slow and Fast pointer
- satisfying additional subarrays: 
    res += count
    count += 1
- Moving Window
```python
counts = { } #usually a hash of element frequencies in window (collections.Counter)
currCount #some constraint on window
bestLength = 0
start = 0
for end in range(len(string)):
    currCount += function(input[end])               #el at end contributes to currCount

    if :                                #if window does not satisfy (e.g end - start - 1 > constraint or currCount > constraint):
        currCount -= function(input[start])                 #el at start is no longer being considered
        start += 1

    bestLength = max(bestLength, end - start + 1)           #update bestLength
      
return bestLength
```
- in-place:
  - make els - 

### 6. Intervals
- Inserting
  - map based on start, [0], sort, bisect.bisect(arr, newInterval[0]), then .insert
```python
    starts = [interval[0] for interval in intervals] 
    starts.sort()
    idx = bisect.bisect(starts, newInterval[0])
    intervals.insert(idx, newInterval)
```
- Merging
  - if [i][1] > [i + 1][0] then set [i][1] to max([i][1], [i + 1][1])
  if current's end is GREATER than next's start, then set currs end to the GREATER end
```python
    merged = [intervals[0]]        #seed it with the 1st interval
    for i in range(1, len(intervals)):
        if merged[-1][1] >= intervals[i][0]:
            merged[-1][1] = max(merged[-1][1], intervals[i][1]) # absorb it
        else:
            merged.append(intervals[i])
    return merged
```
- isOverlap?
  - start1 < end2 and start2 > end1
- Overlap area
  - max(start1, start2) - min(end1, end2)
### 7. Pathing

- Dijkstra’s (2 dicts and 1 set)
  - finds shortest distance to every node
  - visit all nodes once
    - for each node, check dist for all neighbors
(source is “a”)
```python

        def findClosest(self, best, visited): #Find the closest (to orig src), unvisited node 
            res = None
            for node in best:
                if node not in visited and (not res or best[node] < best[res]):
                    res = node
            return res
                                                    # K = starting node, N = # of nodes
                                                    # all nodes receive signal
        graph = collections.defaultdict(dict)
        for edge in edges:
            graph[edge[0]][edge[1]] = edge[2]       #graph[src][dest] = edge
  
        best = dict()           # {a: 2, b: 3}
        for i in range(1, N + 1):
            best[i] = float('inf')
        best[K] = 0
        
        visited = set()
        
        for _ in range(N): 
            closest = self.findClosest(best, visited)
            visited.add(closest)
            for neighbor in graph[closest]:
                best[neighbor] = min(best[closest] + graph[closest][neighbor], best[neighbor])    # src to curr + curr to neigh

        for val in best.values():       #check if we can reach every other node
            if val == float('inf'): return -1
         
        return          #some value in best                      
```

### 8. Bit manipulation
- & | ~
- ^ 
  - finds rightmost 1
  - finds the one duplicate el
- << >>   multiply by 2
- change / check / clear a specific bit
  - shift a "1" over X times using <<
  - maybe ~ (not) it
  - & or | it with your number
- bin() to convert to bin OR
 - format(<num>, '#010b') to keep padding
- int(<binary string>, 2) to convert back to int

### 9. Other Data Structures / Algorithms
- Union Find (num of connected components)
  - keep finding a deeper root until the root matches the node
```python
# input: 
# edges = [[0, 1], [1, 2], [2, 3], [3, 4]]               # list of undirected edges
# n  = 5

# n = 5 and edges = [[0, 1], [1, 2], [3, 4]]

roots = [i for i in range(n)]

def find(key):
    while key != roots[key]:
        key = roots[key]

for edge in edges:
    root1 = find(edge[0])
    root2 = find(edge[1])
    if root1 != root2:
        roots[root1] = root2
        #logic for being in same group ex: count -= 1
    else:
       #logic for being in diff group
```
- Topological Sort (alien dic)
  - for Directed Acyclic graphs
  - orders are not the only "right" answer
  - when you've explored all prereqs/predecessors, then add it to "order"
  - DFS method (recursive calls) or BFS (Queue)
  - need to sometimes check for cycles too
```python
    input:
    words = {"baa", "abcd", "abca", "cab", "cad"} #(given sorted)

    prereqs = {
        : []
    }

    order = []

    visited = {}

    def dfs(node):
        visited.add(node)
        for neigh in neighbor:
            if not in visited: dfs(neigh)
        order.append(node)

    for node in numNodes:
        if node not in visited:
            dfs(node)

    return order[::-1]

```

### 10. Backtracking
- can mutate outer res using 
  - [] assignment
  - .append
- can change curr using:
  - curr + [ ]
  - curr.append  curr.pop
- copy.deepcopy(arr) 
- Combinations / Permutations
  - list(itertools.combinations(arr, #)) [(), ()]
  - list(itertools.permutations(arr, #)) [(), ()]
```
res = []
def recurse(curr, idx)
    res.append(curr[::]) if
    for i in range(idx, len)
    .append
    recurse
    .pop
recurse([], 0)
```
- .isdigit  
- .isalpha
 
### 11. Linked Lists
- Strategies:
  - fast and slow - finds middle, start of cycle
    - Deleting -
    - Dummy node
- Reversing - 3 pointers
    - Null node
- Merging - 3 pointers
    - swap between lists
- triple swaps

```python
tail, head = l1, l1
l1 = l1.next            #l1 head already accounted for by tail
while l2:
    tail.next = l2
    l2 = l2.next
    tail = tail.next
    if l1:
        l1, l2 = l2, l1
return head
```

### 12. Stacks / Queues
- .deque 
- validParens
```python
count = 0
for char in s:
    if char == "(":
        count += 1
    elif char == ")":
        count -= 1
        if count < 0: return False
return count == 0

```

### 13. Extra Knowledge
- Rabin Karp - hashing to find pattern in string
  - turn curr window into hash (integer. e.g 234)
  - convert when window slides (e.g. 345)
  - if currWindow hash == target hash, then compare actual chars
- Self-balancing Trees
  - AVL
  - Black Red Trees
- Sieve of Eratosthenes (finding every prime up to n)
  - check every number up to n 
  - eliminate every num starting at n^2 and incrementing by n
  - go to next unelimiminated 
- Bellman-Ford - one node to others
- Floyd-Warshall - short dist poss between all pairs of nodes
  - n^3
- Minimum Spanning Trees 
  - Kruskal - sort edges, keep adding smallest edge (not nec contiguous) that would connect trees
  - Prim - choose random node, keep choosing smallest accessible edge that would add an unvisited node


### Key Python methods
- list(string)      #how to split a word
- ternary
  - x = 1 if True else 2  #no colon
- .insert(index, el)
- [[for j in range] for i in range]
- array iterating backwards
  - [::][::-1]
  - [-1:0:-1]  (starts at [-1], doesnt touch [0]) (awkward...)
- collections
  - Defaultdict		like Hash.new(0)
  - Deque
  - Counter.items()
- sorted(    .sort(key=
  - sorts by [0] by default for 2D arrs
  - ([0], [1]) *tuple* to sort by multiple fields
- reversed(    .reverse
- Find 	rfind()  	like indexOf
- Strings
  - lstrip rstrip
  - startswith() endswith()
- [list(row) for row in list(zip(*reversed(board)))]  starboard! (Python3 syntax)
  - need to convert zip object
- Arrays: 
  - any(el > 5 for el in arr)
  - all(el > 5 for el in arr)
    - len(set(a) == 1)  #checks if all the same val
  - del arr[] 
  - remove(val) 
  - insert(idx, val)
  - extend(arr2)
  - "map" == [x**2 for x in arr] 
    - map(lambda a: , <iter>)
  - "filter" == [x for x in arr if x > 2] 
    - filter(lambda a: <iter>)
  - "flatten" == [y for x in graph[x] for y in x]
- Sets:
  - can't hash lists / dicts (CAN hash objects)
  - declared with { }
  - set1.union(set2) |= 
  - set1.intersection(set2) &=
  - .add 
  - .discard/.remove to remove 
- range(start, end, step)
- sum(<2darray>, []) will flatten it
- isinstance(<item>, <type>)
 
- range is a lazy iterable like iterators but range is not an iterator
  - iterators

Suggestions:
LL => pointers
rotated / sorted => bSearch
logn time => bSearch / bTree
k branches at each level of recurs tree, n levels => k^n time
top k => heap 
items in arr/str interacting => stack
rectangle/meeting time/free time => interval
anagram => hash
subsequence => dp
prereqs => topo sort