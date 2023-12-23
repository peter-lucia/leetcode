func rotate(nums []int, k int) {
    // naive solution
    // []
    // [1,2,3,4,5,6,7]

    // [5], append nums[len(nums) - k + i] for 0 <= i < k
    // [5], append nums[i] for 0 <= i < n-k
    // [1,2,3,4,5,6,7]
    result := []int{}
    n := len(nums)
    if k > n {
        k = k % n
    }

    for i := 0; i < k; i++ {
        result = append(result, nums[n-k+i])
    }

    for i := 0; i < n-k; i++ {
        result = append(result, nums[i])
    }
    copy(nums, result)
    
}
