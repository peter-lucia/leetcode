class MinStack:

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.stack = deque()
        self.stack_position = 0
        

    def push(self, x: int) -> None:
        if not self.stack:
            self.stack.append((x, x))
            return
        current_min = self.stack[-1][1]
        self.stack.append((x, min(current_min, x)))
        
    def pop(self) -> None:
        self.stack.pop()
        

    def top(self) -> int:
        return self.stack[-1][0]


        
    def getMin(self) -> int:
        return self.stack[-1][1]
        
        


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(x)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()