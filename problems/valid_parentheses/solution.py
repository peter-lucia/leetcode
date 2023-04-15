def closesBracket(left, right) -> bool:
    if left == "(" and right == ")":
        return True
    if left == "[" and right == "]":
        return True
    if left == "{" and right == "}":
        return True

    return False

class Solution:

        
    def isValid(self, s: str) -> bool:

        stack = []
        for c in s:
            if c in ["(", "{", "["]:
                stack.append(c)
            elif not stack:
                return False
            elif not closesBracket(stack[-1], c):
                return False
            else:
                stack.pop(-1)
        return not stack
            







