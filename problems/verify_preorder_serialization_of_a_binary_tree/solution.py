class Solution:
    def isValidSerialization(self, preorder: str) -> bool:
        slots = 1  # root of tree
        
        for c in preorder.split(","):
            slots -= 1
            
            if slots < 0:
                return False
            
            if c != '#':
                slots += 2  # a valid node has potentially two chilcren
                
        return slots == 0  # check that all slots are used up at the end
            
            