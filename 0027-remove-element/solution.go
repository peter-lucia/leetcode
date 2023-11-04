import "fmt"
func removeElement(nums []int, val int) int {
	// if nums[i] == val, swap nums[i] with nums[n-occ-1], where occ is occurrences of val
	// [1, 2, 3, 4, 3, 5, 3]
	//              |, swap 3 for 3, occ +=1
	// [1, 2, 3, 4, 3, 5, 3]
	//              |, swap 3 for 5, occ += 1,
	// [1, 2, 3, 4, 3, 5, 3]
	//                 |     5 is not 3, so increment i. since i >= len(nums) - occ - 1, we're done.
	// [1, 2, 3, 4, 5, 3, 3]

	occ := 0
	n := len(nums)
	for i := 0; i < n - occ; {
		if nums[i] == val {
            // swap nums
			t := nums[i]
			nums[i] = nums[n-occ-1]
			nums[n-occ-1] = t
            occ++
		} else {
            i++
        }
	}
    // fmt.Println(nums, occ)
	return n - occ
}

