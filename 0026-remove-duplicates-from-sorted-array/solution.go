func removeDuplicates(nums []int) int {
    // assuming values are sorted:
    // keep track of last unique value index and current index
    // as soon as the value at the new current index does not equal the value at the
    // last unique value index, increment the last unique value index and
    // assign the newest unique value to that index

    i := 0
    j := 1

    for i < j && j < len(nums) {
        if nums[i] != nums[j] {
            i++
            nums[i] = nums[j]
        }
        j++
    }
    return i+1

}
