Python methods
[[for j in range] for i in range]
[::][::-1]
Defaultdict		like Hash.new(0)
Deque
Counter.items()
sorted(    .sort(key=
reversed(    .reverse
Find 	rfind()  	like indexOf
lstrip rstrip

Dynamic Programming
minChange

Sorts and Searches
	Iterative B-search
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
Backtracking

Trees and Graphs
	BFS, DFS
	Graph - BFS
	X, y
	Dirs = 
	Xi, yj if in bounds
	Topo Sort

Strings and Arrays
Kadane’s - largest contig sum in arr
Rabin Karp - hashing to find pattern in string
Two pointers
Slow and Fast pointer

Pathing
Bellman-Ford
Dijkstra’s
(source is “a”)
    distances = {a: 0, b: ∞, c: ∞, d: ∞
    unvisited (a, b, c, d,
    while unvisited.length:
        Find the closest, unvisited node 
        Remove from unvisited
        For all neighbors
            If best distance to neighbor is greater than best distance to current + dist from curr to neighbor, then change best to that

Bit manipulation
^ finds rightmost 1, finds the one duplicate el
+ -


Self-balancing Trees
Black Red Trees

Handy Boilerplate

Graphs
dirs = []
for x, y in dirs:
    xi, yj
    if 0 <= xi < len and 0 <= yj < len

visited = set()
q = []
while q:
    q.pop
    visited.add
    for neighbor in .neighbors:
        if not in visited:
            q.append


Trees

.left
.right

q = []
newQ = []
newQ << .left
newQ << .right


Backtracking

res = []
def recurse(curr, idx)
    res.append(curr[::]) if
    for i in range(idx, len)
    .append
    recurse
    .pop
recurse([], 0)

.isdigit
.isalpha