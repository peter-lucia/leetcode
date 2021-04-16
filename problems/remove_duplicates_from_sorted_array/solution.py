class Solution:
    def removeDuplicates(self, arr: List[int]) -> int:
        ifirst= 0
        inext = 1
        while inext < len(arr):
            if arr[ifirst] == arr[inext]:
                arr.pop(ifirst)
            else:
                ifirst += 1
                inext += 1
        return len(arr)
