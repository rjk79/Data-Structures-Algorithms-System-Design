(0, 0, 1)
(0, 2, 2)
(2, 2, 1)
(1, 1, 2)
(2, 0, 1)
(1, 0, 2)
(2, 1, 1)

def __init__(self, n):
        count = collections.Counter()
        def move(row, col, player):
            #             line vals:  across, down, diag1(sum) diag2(sum)
            for i, x in enumerate((row, col, row+col, row-col)):
                 # type of line, line val, player#     
                count[i, x, player] += 1
                if count[i, x, player] == n:
                    print(count)
                    return player
            return 0
        self.move = move

count = {

}
i = 0 1 2 3
x = 0 0 0 0
