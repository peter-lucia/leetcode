func merge(nums1 []int, m int, nums2 []int, n int)  {
  i := 0
  j := 0
  res := []int{}
  for i < m && j < n { 
    if nums1[i] < nums2[j] {
      res = append(res, nums1[i])
      i++
    } else if nums1[i] == nums2[j] {
      res = append(res, nums1[i], nums2[j])
      i++
      j++
    }  else {
      res = append(res, nums2[j])
      j++
    }
  }
  
  for i < m {
    res = append(res, nums1[i])
    i++
  }
  for j < n {
    res = append(res, nums2[j])
    j++
  }
  copy(nums1, res)
}
