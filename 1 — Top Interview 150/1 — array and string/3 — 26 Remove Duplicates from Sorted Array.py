from typing import List

# Solve with two pointers


class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        k = 1

        # Iterate through the array but start at index 1 to skip the first element (since it's never a duplicate)
        for i in range(1, len(nums)):
            # Determine if the element is a duplicate by comparing it to the previous element
            if nums[i] != nums[i - 1]:
                nums[k] = nums[i]
                k += 1

        return k


# Test the solution
nums = [0, 0, 1, 1, 1, 2, 2, 3, 3, 4]
result = Solution().removeDuplicates(nums)
print(f"Number of unique elements: {result}")
