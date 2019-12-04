import collections
def ladderLength(beginWord, endWord, wordList):
    all_words = collections.defaultdict(list)
    # break up every word at all possible partitions
    for word in wordList:
        for i in range(len(word)):
            all_words[ word[:i] + "*" + word[i+1:] ].append(word)  
    # print (all_words)
    visited = {beginWord: True}
    q = collections.deque([(beginWord, 1)])
    while q:
        currWord, level = q.popleft()
    # break up curr word at all possible partitions
        for i in range(len(currWord)):
            interWord = currWord[:i] + "*" + currWord[i+1:]
    # add in all words that could match
            for word in all_words[interWord]:
                if word == endWord:
                    return level + 1
                if word not in visited:
                    q.append((word, level + 1))
                    visited[word] = True
            all_words[interWord] = []
    return 0

print(ladderLength("hit", "cog", ["hot","dot","dog","lot","log","cog"]))

# create an all_words dict
# add all words from wordList
# { do* [ ]
# h*t [ ]
# ...
# *ot: [ hot, dot, lot ]
# h*t: [ ]
# ho*: [ ]
# }

# created visited Hash
# {hit: True}