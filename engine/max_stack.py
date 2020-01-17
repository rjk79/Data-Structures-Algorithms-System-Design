class MaxStack:

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.stack = []
        # [(val, currMax), 


    def push(self, x: int) -> None:
        maxi = max(x, self.stack[-1][1] if self.stack else float('-inf'))
        self.stack.append((x, maxi))

    def pop(self) -> int:
        return self.stack.pop()[0]

    def top(self) -> int:
        return self.stack[-1][0]

    def peekMax(self) -> int:
        return self.stack[-1][1]

    def popMax(self) -> int:
        temp = []
        curr = self.stack.pop()
        while curr[0] != curr[1]:
            temp.append(curr[0]) #to be put back in later
            curr = self.stack.pop()
        for el in reversed(temp): #need to add back in reverse
            self.push(el)
        return curr[0]

# Your MaxStack object will be instantiated and called as such:
# obj = MaxStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.peekMax()
# param_5 = obj.popMax()