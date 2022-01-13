class Solution:
    
    @staticmethod
    def find_pivot(arr: List[int]) -> int:
        """
        Finds index where dropoff occurs
        e.g. 3,4,5,1,2 would return 2 since that is the index of the pivot, 5
        """

        low = 0
        high = len(arr) - 1
        n = len(arr)

        while low <= high:
            mid = low + (high - low) // 2
            if mid + 1 < n and arr[mid] > arr[mid + 1]:
                # found pivot at mid
                return mid
            elif mid - 1 > 0 and arr[mid] < arr[mid - 1]:
                # found pivot at mid - 1
                return mid-1
            elif arr[low] >= arr[mid]:
                # element furthest left >= element at mid, set high one less than mid
                # drop-down is left so search left
                high = mid - 1
            else:
                # element further right < element at mid, set low to one above mid
                # drop down is right so search right
                low = mid + 1
        return -1

    
    def search(self, arr: List[int], key: int) -> int:
        
        if len(arr) < 1:
            return -1
        
        if len(arr) == 1:
            if arr[0] == key:
                return 0
            else:
                return -1

        pivot = Solution.find_pivot(arr)

        if arr[pivot] < key or arr[pivot+1] > key:
            return -1


        if pivot == -1:
            low = 0
            high = len(arr) - 1
        elif arr[0] <= key:
            low = 0
            high = pivot
        else:
            low = pivot+1
            high = len(arr) - 1

        if arr[low] == key:
            return low

        while low <= high:
            mid = low + (high - low) // 2
            if arr[mid] < key:
                low = mid + 1
            elif arr[mid] > key:
                high = mid - 1
            else:
                return mid
        return -1
        
