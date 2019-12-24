class Solution:
    def arraysIntersection(self, arr1: List[int], arr2: List[int], arr3: List[int]) -> List[int]:
        a1 = set(arr1)
        a2 = set(arr2)
        a3 = set(arr3)
        
        result = []
        for each in a1:
            if each in a2 and each in a3:
                result.append(each)
        result = sorted(result)
        return result