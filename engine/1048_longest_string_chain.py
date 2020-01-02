def longestStrChain(words):
        # dont want to start from every word
        # word can access another word if store them into a graph
        # graph = {
        #     a: ba
        #     b: ba
        #     ba: bca, bda
        #     bca: bdca
        #     bda: bdca
        # }
# traverse it 
# return longest dfs
        dic = dict()
        for word in words:
            dic[word] = 1
        best = 0

        words.sort(key = lambda a: len(a))
        for word in dic: #need to iter after sorting to make build on values properly
            for i in range(len(word)):
                reduced = word[:i] + word[i+1:]
                print(reduced)
                if reduced in dic:
                    dic[word] = dic[reduced] + 1 #dic[word] wont always be max but at some point it will and thats when itll be recorded in "best"
                    best = max(best, dic[word]) 
        return best
print(longestStrChain(["a","b","ba","bca","bda","bdca"]))