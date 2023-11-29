func twoSum(nums []int, target int) []int {
    lookup := map[int]int{}

    result := []int{-1, -1}
    for i, a := range nums {
        j, found := lookup[target - a]
        if found {
            result[0] = i
            result[1] = j
            return result
        }
        lookup[a] = i
    }
    return result

}
