class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        return merge_sort(nums)

def merge_sort(arr):
    # Divide the array into subarrays of size 1
    subarrays = [[x] for x in arr]
    
    # Merge pairs of subarrays until the entire array is sorted
    while len(subarrays) > 1:
        # Merge the first two subarrays into a new subarray
        left = subarrays.pop(0)
        right = subarrays.pop(0)
        merged = merge(left, right)
        
        # Add the merged subarray back to the list of subarrays
        subarrays.append(merged)
    
    # Return the sorted array
    return subarrays[0]

def merge(left, right):
    result = []
    i = 0
    j = 0
    
    # Compare the first elements of each subarray and add the smaller one to the result array
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
    
    # Add any remaining elements from the left or right subarray to the result array
    result += left[i:]
    result += right[j:]
    
    return result
