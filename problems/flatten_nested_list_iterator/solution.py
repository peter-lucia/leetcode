# """
# This is the interface that allows for creating nested lists.
# You should not implement it, or speculate about its implementation
# """
#class NestedInteger:
#    def isInteger(self) -> bool:
#        """
#        @return True if this NestedInteger holds a single integer, rather than a nested list.
#        """
#
#    def getInteger(self) -> int:
#        """
#        @return the single integer that this NestedInteger holds, if it holds a single integer
#        Return None if this NestedInteger holds a nested list
#        """
#
#    def getList(self) -> [NestedInteger]:
#        """
#        @return the nested list that this NestedInteger holds, if it holds a nested list
#        Return None if this NestedInteger holds a single integer
#        """

class NestedIterator:
    def __init__(self, nestedList: [NestedInteger]):
        self.nested_list = []
        
        def dfs(val):
            for each in val:
                if each.isInteger():
                    self.nested_list.append(each.getInteger())
                dfs(each.getList())
        
        dfs(nestedList)
        self.i = -1
        
    def next(self) -> int:
        self.i += 1
        return self.nested_list[self.i]
        
    def hasNext(self) -> bool:
        return self.i+1 < len(self.nested_list)
            

# Your NestedIterator object will be instantiated and called as such:
# i, v = NestedIterator(nestedList), []
# while i.hasNext(): v.append(i.next())