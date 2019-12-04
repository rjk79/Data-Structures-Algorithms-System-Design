def alienOrder(words):



# if we didn't remove all prereqs then dont add it into queue, charsToProcess
# (we dont have enough info to place it. there are more chars that come before it)
# if we dont add something to Q on this iter, then either the next succ for the current letter will add something OR
# the next letter's successors will be added 