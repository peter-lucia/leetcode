class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        """
        Approach:

        1. Finding a pivot point where all elements to the left are smaller and all
        elements to the right are greater, you can find the median

        x x [x]|[x] x x  long_l, long_r
          y [y]|[y] y    short_l, short_r

        x x [y] [x] | [y] y [x] x x

        2. Any pivot point in the smaller array has a corresponding point on the
        large array, that divides the total # of elements in two

        x x x x x x
          y y y y

        3. After picking a pivot point, it's possible to determine whether we need to
        go left or right

        1 2 3|4 5 6
          2 3|4 5

        Code Outline
        1. Binary search on small array
        2. Get indices of long_l, long_r, short_l, short_r
        3. Get direction we need to do binary search in (left (-1) or right (1) or 0 means we've found the right pivot)
        4. At the end, calculate the median

        """


        if len(nums1) > len(nums2):
            nums1, nums2 = nums2, nums1

        n = len(nums1)
        m = len(nums2)
        total = n + m

        half =  total // 2

        # binary search over best pivot in nums1
        # pivot in nums2 is determined from pivot in nums1
        low = 0
        high = len(nums1) - 1
        while True:
            mid_nums1 = low + (high - low) // 2
            mid_nums2 = half - mid_nums1 - 2

            short_l = nums1[mid_nums1] if mid_nums1 >= 0 else float("-inf")
            short_r = nums1[mid_nums1+1] if mid_nums1+1 < n else float("inf")
            long_l = nums2[mid_nums2] if mid_nums2 >= 0 else float("-inf")
            long_r = nums2[mid_nums2+1] if mid_nums2+1 < m else float("inf")

            # if partition is correct, determine result
            if short_l <= long_r and long_l <= short_r:
                if total % 2 == 0:
                    # determine two middle elements and then calculate their average
                    return (max(short_l, long_l) + min(short_r, long_r)) / 2
                # odd: it's the smaller element of the right hand partitions
                # 1|2 3
                # 1|2
                # 1 1 2 2 3
                return min(short_r, long_r)
            elif short_l > long_r:
                # x x [x]|[x] x x  long_l, long_r
                #   y [y]|[y] y    short_l, short_r
                high = mid_nums1 - 1
            elif long_l > short_r:
                # x x [x]|[x] x x  long_l, long_r
                #   y [y]|[y] y    short_l, short_r
                low = mid_nums1 + 1
