# using a visited doesnt work bc theres nowhere to go once u complete the word with ["a", "a"] and "aa" as word
# so temporarily make the visited squares a SYMBOL "$"
def wordSearch(board, word):
    if board[0][0] == word: return True

    def dfs(word, point):
        if word == "": return True 
        dirs = [[0, 1], [1, 0], [-1, 0], [0, -1]]
        i, j = point
        # import pdb; pdb.set_trace()
        
        if board[i][j] == word[0]:
            temp = board[i][j]
            board[i][j] = "$"
            possible = False
            for x, y in dirs:
                xi, yj = x + i, y + j
                if 0 <= xi < len(board) and 0 <= yj < len(board[0]):
                    if dfs(word[1:], [xi, yj]): possible = True
            # switch it back once yr done making recurs calls
            board[i][j] = temp
            return possible
        else:
            return False      

    for i in range(len(board)):
        for j in range(len(board[0])):
                if dfs(word, [i, j]): return True
    return False

print (wordSearch([['A', 'B', 'C', 'E'], ['S', 'F', 'C', 'S'], ['A', 'D', 'E', 'E']], 'ABCCED')) #TRUE
print (wordSearch([['A', 'B', 'C', 'E'], ['S', 'F', 'C', 'S'], ['A', 'D', 'E', 'E']], 'SEE')) #TRUE
print (wordSearch([['A', 'B', 'C', 'E'], ['S', 'F', 'C', 'S'], ['A', 'D', 'E', 'E']], 'ABCB')) #FALSE (path should not overlap itself)
print (wordSearch([['a']], 'a')) #TRUE 
print (wordSearch([['a', 'a']], 'aa')) #TRUE 

# A B C E
# S F C S 
# A D E E



# iter thru array until we find the 1st letter of the word
#   then perform a DFS starting from there, passing in the rest of the word
#   each "neighbor" will be a "dir" away (stay in bounds)
#   each call passes a diminished str
#   if str reaches "" return True
#   use "or" to compile results
#   outer func returns True if inner DFS rets True
#   otherwise ret false once youre done iterating thru the grid