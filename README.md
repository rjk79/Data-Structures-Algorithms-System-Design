# Data Structures and Algorithms

### Dynamic Programming
- Overlapping Subproblems 
- Optimal Substructure (buying travel tickets)
- 2D array for X vs. Y "graph"
- Probability
- minChange
- Memoizing: @functools.lru_cache(None)     (not dp, only similar)

### Sorts and Searches
- Quicksort - worst case O(n^2)
- Iterative B-search
```
    lo, hi = 0, len() 
    while(lo < hi) {
    int mid = lo + (hi - lo) / 2;
    if(Special condition passed)(optional):
        return mid; 
    if(condition passed)
    hi = mid;
    else 
    lo = mid + 1;
    }
    return lo;
```
- bisect.bisect(iterable, target) does BS but returns idx + 1 so do - 1 after
  - can also find where to insert a target
- Reservoir Sampling
- random.random()*3//1  (0, 1, 2)

### Graphs
- Tradeoffs
  - Adjacency matrix
  - graph
  - Class
- BFS, DFS
- Graph - BFS
  - don't use [-1] for ranges (will mess up when combined with dirs)
```
dirs = []
for x, y in dirs:
    xi, yj
    if 0 <= xi < len and 0 <= yj < len
```
```
visited = set()
q = []
while q:
    q.pop
    visited.add
    for neighbor in .neighbors:
        if not in visited:
            q.append
```

- Topo Sort

### Trees
- Traversals
- DFS
```
.left
.right
```
- BFS
```
q = []
newQ = []
newQ << .left
newQ << .right
```
- Level Order
- Tries
```
class TrieNode:
    def __init__(self):
        self.children = collections.defaultdict(TrieNode)   # makes itself
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
  - heapq.heappush(arr, el)
  - heapq.heappop(arr)
  - sorts ASC by [0] so [0][0] is the smallest val it sees
  - insert and delete are O(logn)
  - creating a heap is NOT O(nlogn) even though it's n els * logn insert time...
    - time is amortized to O(n)
### Strings and Arrays
- ord() and chr()
- Kadane’s - largest contig sum in arr
- Rabin Karp - hashing to find pattern in string
- Two pointers
- Slow and Fast pointer
- Moving Window
```
counts = { } //usually a hash of element frequencies in window
currCount //some constraint on window
bestLength = 0
start = 0
for end in range(len(string)):
    currCount += function(input[end])               //el at end contributes to currCount

    if :                                //if window does not satisfy (e.g end - start - 1 > constraint or currCount > constraint):
    currCount -= function(input[start])                 //el at start is no longer being considered
    start += 1

    bestLength = max(bestLength, end - start + 1)           //update bestLength
      
return bestLength
```
### Intervals
- Inserting
  - map based on start, [0], sort, bisect.bisect(arr, newInterval[0]), then .insert
```
    starts = [interval[0] for interval in intervals] 
    starts.sort()
    idx = bisect.bisect(starts, newInterval[0])
    intervals.insert(idx, newInterval)
```
- Merging
  - if [i][1] > [i + 1][0] then set [i][1] to max([i][1], [i + 1][1])
  if current's end is GREATER than next's start, then set currs end to the GREATER end
```
    merged = [intervals[0]]        //seed it with the 1st interval
    for i in range(1, len(intervals)):
        if merged[-1][1] >= intervals[i][0]:
            merged[-1][1] = max(merged[-1][1], intervals[i][1])
        else:
            merged.append(intervals[i])
    return merged
```
- isOverlap?
  - start1 < end2 and start2 > end1
- Overlap area
  - max(start1, start2) - min(end1, end2)
### Pathing

- Dijkstra’s 
  - finds shortest distance to every node
  - visit all nodes once
    - for each node, check dist for all neighbors
(source is “a”)
```

        def findClosest(self, best, visited): //Find the closest (to orig src), unvisited node 
            res = None
            for node in best:
                if node not in visited and (not res or best[node] < best[res]):
                    res = node
            return res
                                                    // K = starting node, N = # of nodes
                                                    // all nodes receive signal
        graph = collections.defaultdict(dict)
        for edge in edges:
            graph[edge[0]][edge[1]] = edge[2]       //graph[src][dest] = edge
  
        best = dict()           // {a: 2, b: 3}
        for i in range(1, N + 1):
            best[i] = float('inf')
        best[K] = 0
        
        visited = set()
        
        for _ in range(N): 
            closest = self.findClosest(best, visited)
            visited.add(closest)
            for neighbor in graph[closest]:
                best[neighbor] = min(best[closest] + graph[closest][neighbor], best[neighbor])    // src to curr + curr to neigh

        for val in best.values():       //check if we can reach every other node
            if val == float('inf'): return -1
         
        return          //some value in best                      
```
- Bellman-Ford - one node to others
- Floyd-Warshall - short dist poss between all pairs of nodes
- Minimum Spanning Trees 
  - Kruskal - sort edges, keep adding smallest edge (not nec contiguous) that would connect trees
  - Prim - choose random node, keep choosing smallest avail edge that would add an unvisited node
### Bit manipulation
- & | ~
- ^ 
  - finds rightmost 1
  - finds the one duplicate el
- << >>   multiply by 2
- change / check / clear a specific bit
  - shift a "1" over X times
  - maybe ~ it
  - & or | it with your number
- bin() to convert to bin
- int(<binary string>, 2) to convert back to int


### Self-balancing Trees
- AVL
- Black Red Trees

### Other Data Structures / Algorithms
- Union Find (num of connected components)
  - keep finding a deeper root until the root matches the node
```
input: 
edges = [[0, 1], [1, 2], [2, 3], [3, 4]]               // list of undirected edges
n  = 5

n = 5 and edges = [[0, 1], [1, 2], [3, 4]]

roots = [i for i in range(len(edges))]

def find(key):
    while key != roots[key]
        key = roots[key]

for edge in edges:
    root1 = find(edge[0])
    root2 = find(edge[1])
    if root1 != root2:
        roots[root1] = root2
        //logic for being in same group
    else:
       //logic for being in diff group
```
- Topological Sort (alien dic)
  - for Directed Acyclic graphs
  - orders are not the only "right" answer
  - when you've explored all prereqs/predecessors, then add it to "order"
  - DFS method (recursive calls) or BFS (Queue)
  - need to sometimes check for cycles too
```
    input:
    words(sorted) = {"baa", "abcd", "abca", "cab", "cad"}

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


### Backtracking
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
- .isdigit()
- .isalpha()

### Python methods
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
- reversed(    .reverse
- Find 	rfind()  	like indexOf
- Strings
  - lstrip rstrip
  - startswith() endswith()
- [*zip(*grid)]   starboard!
  - need star to unpack zip object
- Arrays: 
  - del arr[] 
  - remove(val) 
  - insert(idx, val)
- Sets:
  - declared with { }
  - set1.union(set2) set1.intersection(set2)
- range(start, end, step)
- sum(2darray, []) will flatten it

- Sets: 
  - .add 
  - .discard/.remove to remove 
- range is a lazy iterable like iterators but range is not an iterator
  - iterators


