func shiftRight(nums []int) {
  prev := nums[len(nums)-1]
  i := 0
  for i < len(nums) {
      nums[i], prev = prev, nums[i]
      i++
  }
}

func rotate(nums []int, k int)  {
    for k > 0 {
        shiftRight(nums)
        k--
    }
}
