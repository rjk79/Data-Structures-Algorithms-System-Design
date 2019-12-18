def convert(s, numRows):
        stacks = [list() for _ in range(numRows)]
        stackIds = [idx for idx in range(numRows)]
#       0 1 2 3 4
#         1 2 3 
        stackIds = stackIds + stackIds[1:-1][::-1]
        print(stackIds)
        stackId = 0
        for char in s:
            stacks[stackIds[stackId]].append(char)
            stackId += 1
            if stackId >= len(stackIds): stackId = 0


        
        res = ""
        words = ["".join(stack) for stack in stacks]
        return "".join(words)
print(convert("PAYPALISHIRING", 3))
# "PAHNAPLSIIGYIR"