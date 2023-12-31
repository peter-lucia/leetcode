func removeDuplicates(nums []int) int {
    // track last unique index
    // track current index
    // if current does not equal last unique,
    // increment last unique index and set current value to the new position
    // otherwise  increment current
    // O(n) time complexity
    // O(1) space complexity
    if len(nums) <= 1 {
        return len(nums)
    }
    idxLastUnique := 0
    idxCurr := 1

    for ;idxCurr < len(nums); {
        if nums[idxLastUnique] == nums[idxCurr] {
            idxCurr++
        } else {
            idxLastUnique++;
            nums[idxLastUnique] = nums[idxCurr] 
            idxCurr++
        }
    }

    return idxLastUnique+1
}
