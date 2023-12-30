func merge(nums1 []int, m int, nums2 []int, n int)  {
    // copy nums1 into a new array size m
    // then using the mergesort merge operation, merge the two separate arrays into nums1

    // deep copy the first m elements of nums1 into a new array nums3
    nums3 := make([]int, m)
    copy(nums3, nums1)

    i := 0
    j := 0
    k := 0
    // fmt.Printf("src slice: %v, memory address of the backing array: %p\n", nums1, nums1)
	// fmt.Printf("dst slice: %v, memory address of the backing array: %p\n", nums3, nums3)
    for (i < m && j < n) {
        fmt.Println(nums1, nums3, i, nums2, j)
        if nums3[i] <= nums2[j] {
            nums1[k] = nums3[i]
            i++
            k++
        } else {
            nums1[k] = nums2[j]
            j++
            k++
        }
    }
    // fmt.Println("-----------------")
    // fmt.Println(nums1, nums3, i, nums2, j)
    for (i < m) {
        nums1[k] = nums3[i]
        i++
        k++
    }
    // fmt.Println(nums1, nums3, i, nums2, j)
    for (j < n) {
        nums1[k] = nums2[j]
        j++
        k++
    }
}
