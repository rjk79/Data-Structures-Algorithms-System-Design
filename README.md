### Python methods
- [[for j in range] for i in range]
- [::][::-1]
- collections
  - Defaultdict		like Hash.new(0)
  - Deque
  - Counter.items()
- itertools
  - list(combinations(arr, #))
  - list(permutations(arr, #))
- sorted(    .sort(key=
- reversed(    .reverse
- Find 	rfind()  	like indexOf
- lstrip rstrip
- [*zip(*grid)]
- need star to unpack zip object
- Arrays: 
  - del arr[] 
  - remove(val) 
  - insert(idx, val)

- Sets: 
  - .add 
  - .discard/.remove to remove 
- range is a lazy iterable like iterators but range is not an iterator
  - iterators
- bisect.bisect(iterable, target) does BS but returns idx + 1 so do - 1 after
  - can also find where to insert a target

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
- X, y
- Dirs = 
- Xi, yj if in bounds
- Topo Sort

### Strings and Arrays
- Kadane’s - largest contig sum in arr
- Rabin Karp - hashing to find pattern in string
- Two pointers
- Slow and Fast pointer

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
    roots[root1] = root2
```
- Topological Sort
  - orders are not the only "right" answer
  - when you've explored all prereqs/predecessors, then add it to "order"
  - DFS method (recursive calls) or BFS (Queue)
```
    prereqs = {
        : []
    }

    order = []

    def dfs(node, visited):
        visited.add(node)
        for neigh in neighbor:
            if not in visited: dfs(neigh, visited)
        order.append(node)

    dfs(el with no prereqs)
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

### Backtracking
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