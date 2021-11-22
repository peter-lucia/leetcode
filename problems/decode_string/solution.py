class Solution:
    def is_digit(self, d: str) -> bool:
        try:
            _ = int(d)
            return True
        except ValueError:
            return False

    def decodeString(self, s: str) -> str:
        stack = []
        for c in s:
            stack.append(c)
            if c == ']':
                stack.pop()  # remove ']' from stack

                # extract string inside brackets
                new_string = ""  # ]
                elem = ''
                while elem != '[':
                    new_string = elem + new_string
                    elem = stack.pop()

                # get digit in front of left bracket
                digit = ""
                while True:
                    if stack:
                        if self.is_digit(stack[-1]):
                            elem = stack.pop()
                            digit = elem + digit
                        else:
                            break
                    else:
                        break

                # push the decoded string onto the stack
                digit = int(digit)
                for i in range(digit):
                    stack.append(new_string)
        # pop each element off the top of the stack and add it to the beginning of the result
        return "".join(stack)


        
        