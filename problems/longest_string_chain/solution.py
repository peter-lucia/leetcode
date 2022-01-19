from pprint import pprint
       
class Solution:
    
    def longestStrChain(self, words: List[str]) -> int:
        # approach #1
        # build a Trie from the words list
        # keep track of the max depth when reaching the end of a word
        # return the max depth
        
        # approach #2 (working)
        # Source: https://leetcode.com/problems/longest-string-chain/discuss/294890/JavaC%2B%2BPython-DP-Solution
        # 1. sort the words by length
        # 2. Use a hashmap to map a word to the number of predecessor words
        # 3. For each word, iterate over all substrings with each character removed in that word
        #    If the substring is found in the table, increment the predecessors for the word by 
        #    the greater quantity between one plus what was found in the lookup for the substr 
        #    or what exist in the lookup for the current word
        # 4. Return the max number of predecessors found for all words, keep track of these each
        #    time the lookup for a word is adjusted
        # Time complexity: O(nlogn + nL^2) where L is the average (or longest) word length
        
        # Assumptions
        # Can assume 1 <= len(words) <= 1000
        # 1 <= words[i].length <= 16
        # words[i] only consists of English letters
        
        words = sorted(words, key=len)
        lookup = defaultdict(int)
        
        # a single word is a word chain
        result = 1
        
        for word in words:
            lookup[word] = 1
            
            for i in range(len(word)):
                # since a predecessor must have only 1 character difference,
                # we find all possible substrings of the word where 1 character is excluded.
                substr = word[:i] + word[i+1:]
                
                # because we care about letter order for predecessors, we don't need all permutations of the substring
                if substr in lookup:
                    lookup[word] = max(lookup[word], lookup[substr] + 1)
                    result = max(result, lookup[word])
                    
        return result
            
        
        
        
        