from typing import List


class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        k = 0

        for i in range(len(nums)):
            if nums[i] != val:
                nums[k] = nums[i]
                k += 1

        return k


# Test the solution
nums = [0, 1, 2, 2, 3, 0, 4, 2]
val = 2

result = Solution().removeElement(nums, val)
print(f"Number of elements not equal to {val}: {result}")
print(f"Modified array: {nums[:result]}")
