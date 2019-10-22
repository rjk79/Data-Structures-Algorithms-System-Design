# starts
[1, 2, 3, 3]
# ends
[3, 4, 5, 6]
# profit
[50, 10, 40, 70]

#   1     2
#   /    /
#  3   4
# / \
#5   6 

# brute - DFS
# any interval completely contained and with greater profit is better

# memoization
# tabulate -> [len of start times]
# go backwards
# best profit from idx onwards
# ex. best profit from idx = 3 onwards => 70
#                            2 => 70
#                            1 => 120

# better dp?
# store as a heap. sort by profit
# dont need ending times, just combine if end time < start time
# if you eclipse start times, itll be hard to add onto them so should make new instance of  
# [[3, 70], [3, 40]] => [[2, 10] [3, 70], [3, 40]] => [[2, 10] [1, 50], [1, 90]]
# 
