class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        """
        numbers is sorted so we can use a
        two pointers approach
        i = 0, j = len(numbers) - 1
        if i + j > target, decrement j
        if i + j < target, increment i
        otherwise, return [-1, -1]
        """
        i = 0
        j = len(numbers) - 1

        while i < j:
            if numbers[i] + numbers[j] > target:
                j -= 1
            elif numbers[i] + numbers[j] < target:
                i += 1
            else:
                return [i+1,j+1]

        return [-1, -1]



        
