from typing import List


class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """

        # Two Pointers: p1 for nums1, p2 for nums2, and last for merged array
        p1 = m - 1
        p2 = n - 1
        last = m + n - 1

        # Merge elements in reverse order

        while p1 >= 0 and p2 >= 0:
            if nums1[p1] > nums2[p2]:
                nums1[last] = nums1[p1]
                p1 -= 1
            else:
                nums1[last] = nums2[p2]
                p2 -= 1
            last -= 1

        # Copy remaining elements from nums2, if any
        while p2 >= 0:
            nums1[last] = nums2[p2]
            p2 -= 1
            last -= 1


nums1 = [1, 2, 3, 0, 0, 0]
m = 3
nums2 = [2, 5, 6]
n = 3

Solution().merge(nums1, m, nums2, n)
print(nums1)
