class Solution:
    
    def is_palindrome(self, s: str) -> bool:
        
        i = 0
        j = len(s) - 1
        
        while i < j:
            if s[i] != s[j]:
                return False
            i += 1
            j -= 1
        return True
    
    def partition(self, s: str) -> List[List[str]]:
        # Incrementally build candidates for the solution and discard candidates (backtrack) if
        # they don't satisfy the condition
        # DFS on the following tree:
        # s = abc
#i=1    #    check [a]bc                                                     # call stack 1
        #    [a] is a palindrome. check bc, path = ['a']
        # s = bc
        #    check [b]c                                                      # call stack 2
#i=1    #    [b] is a palindrome. check c, path = ['a', 'b']
        # s = c
        #    check [c]
        #    [c] is a palindrome. check '', path = ['a', 'b', 'c']
        # s = ''
        #    append ['a', 'b', 'c'] to result
        # s = bc
        #    check [bc]                                                      # call stack 2
#i=1    #    [bc] is not a palindrome
        # s = abc
#i=2    #    check [ab]c
        #    [ab] is not a palindrome
        #    check [abc]
        #    [abc] is not a palindrome
        
        def dfs(s, path, result):
            if not s:
                # finished recursing through tree of possible substrings
                result.append(path)
                return
            
            # generate substrings of all sizes in s
            for i in range(1, len(s)+1):
                print(s[:i])
                # if we find a palindrome
                # add it to the current dfs tree path
                # pass through the result
                if self.is_palindrome(s[:i]):
                    dfs(s[i:], path + [s[:i]], result)
        
        result = []
        dfs(s, [], result)
        return result
