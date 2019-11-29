# Data Structures and Algorithms

### Dynamic Programming
- 2D array for X vs. Y "graph"
- Probability
- minChange

### Sorts and Searches
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
### Trees and Graphs
- BFS, DFS
- Graph - BFS
  - don't use [-1] for ranges (will mess up when combined with dirs)
```
i, j
                    //mark as visited
dirs = 
for x, y in dirs:
    xi, yj =       // if in bounds
```
- Topo Sort

### Strings and Arrays
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

### Pathing
- Bellman-Ford
- Dijkstra’s
(source is “a”)
```
    distances = {a: 0, b: ∞, c: ∞, d: ∞
    unvisited (a, b, c, d,
    while unvisited.length:
        Find the closest, unvisited node 
        Remove from unvisited
        For all neighbors
            If best distance to neighbor is greater than best distance to current + dist from curr to neighbor, then change best to that
```
### Bit manipulation
- ^ finds rightmost 1, finds the one duplicate el
- << multiply by 2


### Self-balancing Trees
- AVL
- Black Red Trees

### Other Data Structures / Algorithms
- Union Find
  - keep finding a deeper root until the root matches the node
```
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
- Topological Sort
  - for Directed Acyclic graphs
  - orders are not the only "right" answer
  - when you've explored all prereqs/predecessors, then add it to "order"
  - DFS method (recursive calls) or BFS (Queue)
  - need to sometimes check for cycles too
```
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
- Reservoir Sampling

## Handy Boilerplate

### Graphs
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

### Trees
```
.left
.right

q = []
newQ = []
newQ << .left
newQ << .right
```
```
class TrieNode:
    def __init__(self):
        self.children = collections.defaultdict(TrieNode)
        self.isWord = False
def Trie:
    def __init__(self):
        self.root = TrieNode()
    def insert(self, word):
        root = self.root
        for c in word:
            root = root.children[c]
        root.isWord = True
    def search(self, word):
        root = self.root
        for c in word:
            root = root.children.get(c)
            if not root: return False
        return root.isWord
```

### Backtracking
- can mutate outer res using 
  - [] assignment
  - .append
- can change curr using:
  - curr + [ ]
  - curr.append  curr.pop
- copy.deepcopy(arr) 

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
- [[for j in range] for i in range]
- array iterating backwards
  - [::][::-1]
  - [-1:0:-1]  (starts at [-1], doesnt touch [0]) (awkward...)
- collections
  - Defaultdict		like Hash.new(0)
  - Deque
  - Counter.items()
- Combinations / Permutations
  - list(itertools.combinations(arr, #)) [(), ()]
  - list(itertools.permutations(arr, #)) [(), ()]
- sorted(    .sort(key=
- reversed(    .reverse
- Find 	rfind()  	like indexOf
- Strings
  - lstrip rstrip
  - startswith() endswith()
- [*zip(*grid)]
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
- 

- Sets: 
  - .add 
  - .discard/.remove to remove 
- range is a lazy iterable like iterators but range is not an iterator
  - iterators
- bisect.bisect(iterable, target) does BS but returns idx + 1 so do - 1 after
  - can also find where to insert a target
- random.random()*3//1  (0, 1, 2)


### C++ Notes
- cout << "Hi"
- true false
- if () {} else if () {}
- while () { }
- for (int i; i < 10; i ++) {}
- int arr[5]
- int arr[5][4]
- use arrays for frequent access and vectors for freq push/pop
- vector <int> a (5) 
  - vector <int> a [5] = creates array of 5 vectors 
  - .resize() then .push_back() adds to back
  - 2D vector ==>> vector < vector <int> > (need the space so that it doesnt do the ">>" operator )
  - pass vectors by reference into funcs int func(vector<int>& vect)
  - .push_back()
  - .pop_back()
- (&) can retrieve memory address
- (*) can store memory address
- void myFunc(string a) { }