class Solution:
    def findMedianSortednums1rrays(self, nums1: [int], nums2: [int]) -> float:
        return self.function1(nums1, nums2)
        # return self.function2(nums1, nums2)

    def function1(self, nums1: [int], nums2: [int]) -> float:
        nums1_length = len(nums1)
        nums2_length = len(nums2)
        nums_mid = int((nums1_length + nums2_length) / 2) + 1
        def findKthNum(k:int, left1:int, left2:int) -> float:
            if k == 1:
                if left1 + 1 >= nums1_length:
                    return nums2[left2 + 1]
                elif left2 + 1 >= nums2_length:
                    return nums1[left1 + 1]
                else:
                    return min(nums1[left1 + 1], nums2[left2 + 1])
            cut_count = int(k / 2)
            left1_next = left1 + cut_count if left1 + cut_count < nums1_length else nums1_length - 1
            left2_next = left2 + cut_count if left2 + cut_count < nums2_length else nums2_length - 1
            if left1_next == left1:
                cut_count = left2_next - left2
                left2 = left2_next
            elif left2_next == left2:
                cut_count = left1_next - left1
                left1 = left1_next
            else:
                if nums1[left1_next] < nums2[left2_next]:
                    cut_count = left1_next - left1
                    left1 = left1_next
                else:
                    cut_count = left2_next - left2
                    left2 = left2_next
            k = k - cut_count
            return findKthNum(k, left1, left2)
        if (nums1_length + nums2_length) % 2 != 0:
            return findKthNum(nums_mid, -1, -1)
        else:
            return (findKthNum(nums_mid - 1, -1, -1) + findKthNum(nums_mid, -1, -1)) / 2

    def function2(self, nums1: [int], nums2: [int]) -> float:
        m, n = len(nums1), len(nums2)
        if m > n:
            nums1, nums2, m, n = nums2, nums1, n, m
        if n == 0:
            raise ValueError
        imin, imax, half_len = 0, m, int((m + n + 1) / 2)
        while imin <= imax:
            i = int((imin + imax) / 2)
            j = half_len - i
            if i < m and nums2[j-1] > nums1[i]:
                # i is too small, must increase it
                imin = i + 1
            elif i > 0 and nums1[i-1] > nums2[j]:
                # i is too big, must decrease it
                imax = i - 1
            else:
                # i is perfect
                if i == 0: max_of_left = nums2[j-1]
                elif j == 0: max_of_left = nums1[i-1]
                else: max_of_left = max(nums1[i-1], nums2[j-1])

                if (m + n) % 2 == 1:
                    return max_of_left

                if i == m: min_of_right = nums2[j]
                elif j == n: min_of_right = nums1[i]
                else: min_of_right = min(nums1[i], nums2[j])

                return (max_of_left + min_of_right) / 2.0
# print(Solution().findMedianSortednums1rrays([1,3,4,9],[1,2,3,4,5,6,7,8,9]))
print(Solution().findMedianSortednums1rrays([1,3],[2,3]))
1,1,2,3,3,4,4,5,6,7,8,9,9