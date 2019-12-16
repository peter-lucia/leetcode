class Solution(object):
    def dailyTemperatures(self, T):
        # initialize the answer to all zeros
        ans = [0] * len(T)
        # since we iterate from the end to the beginning, the last elements (top) of the stack are 
        # closest to i as we iterate through it backwards.
        # elements in the stack that are less than the element at i are removed at each iteration.
        stack = []
        
        for i in range(len(T) - 1, -1, -1):           
            # remove all elements in the stack that are less than the current element
            while stack and T[i] >= T[stack[-1]]:
                stack.pop()
            # if there are elements left over that are greater than the current element
            # append the difference between the last element (which is the element closest to i)
            if stack:
                ans[i] = stack[-1] - i
            # append the current element's position to the stack
            stack.append(i)
        return ans
        
        