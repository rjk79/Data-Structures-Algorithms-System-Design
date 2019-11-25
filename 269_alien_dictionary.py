def alienOrder(words):


# Given the following words in dictionary,
# [
#   "wrt",
#   "wrf",
#   "er",
#   "ett",
#   "rftt"
# ]
# The correct order is: "wertf".
# Example 2:
# Given the following words in dictionary,
# [
#   "z",
#   "x"
# ]
# The correct order is: "zx".
# Example 3:
# Given the following words in dictionary,
# [
#   "z",
#   "x",
#   "z"
# ]
# The order is invalid, so return "".
# Note:
# You may assume all letters are in lowercase.
# You may assume that if a is a prefix of b, then a must appear before b in the given dictionary.
# If the order is invalid, return an empty string.
# There may be multiple valid order of letters, return any one of them is fine.




# if we didn't remove all prereqs then dont add it into queue, charsToProcess
# (we dont have enough info to place it. there are more chars that come before it)
# if we dont add something to Q on this iter, then either the next succ for the current letter will add something OR
# the next letter's successors will be added 