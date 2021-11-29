class Solution:
    def isValid(self, s: str) -> bool:
        # approach 1: anytime we see {}, (), or [], remove it from the expression
        
        # Append each character in s to the stack
        # if the stack is not empty, and the last character added to the stack
        # is the closing bracket of the same time, don't append the new character 
        # to the stack and remove the left bracket from the stack to effectively
        # remove the {}, (), or [] from the string
        # repeat this process until we've gone through all characters in s.
        # if at the end the stack is not empty, return False
        # otherwise, return True
        
        stack = []
        
        for c in s:
            if stack:
                if c == '}' and stack[-1] == '{':
                    stack.pop(-1)
                elif c == ')' and stack[-1] == '(':
                    stack.pop(-1)
                elif c == ']' and stack[-1] == '[':
                    stack.pop(-1)
                else:
                    stack.append(c)
            else:
                stack.append(c)
        if stack:
            return False
        else:
            return True
                