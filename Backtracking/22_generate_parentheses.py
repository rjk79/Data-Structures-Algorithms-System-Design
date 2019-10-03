def generateParenthesis(self, n: int) -> List[str]:
        targetLen = n
        res = []
        def recurse(curr, numOpen, numClose):
            if (numOpen == 0) and (numClose == 0):
                res.append(curr)
                return
            if numOpen != 0:
                recurse(curr + "(", numOpen - 1, numClose)
            if numClose != 0 and (numOpen < numClose):
                recurse(curr + ")", numOpen, numClose - 1)
        recurse("", n, n)
        return res
    
#     check if num opening == num closing