/**
 * You are given two integer arrays nums1 and nums2, sorted in non-decreasing order, and two integers m and n, representing the number of elements in nums1 and nums2 respectively.

 * Merge nums1 and nums2 into a single array sorted in non-decreasing order.

 * The final sorted array should not be returned by the function, but instead be stored inside the array nums1. To accommodate this, nums1 has a length of m + n, where the first m elements denote the elements that should be merged, and the last n elements are set to 0 and should be ignored. nums2 has a length of n.

Constraints:

nums1.length == m + n
nums2.length == n
0 <= m, n <= 200
1 <= m + n <= 200
-109 <= nums1[i], nums2[j] <= 109


 * @param {number[]} nums1
 * @param {number} m
 * @param {number[]} nums2
 * @param {number} n
 * @return {void} Do not return anything, modify nums1 in-place instead.
 */

// The two-pointer approach implemented is the most efficient way to merge two sorted arrays in-place. The code below solves with an optimal solution with O(m + n) time complexity

// Explanation of Time Complexity:
// * Each element in nums1 and nums2 is visited at most once.
// * The comparisons and assignments within the loop take constant time.
// * Therefore, the overall time complexity is directly proportional to the total number of elements in both arrays, resulting in O(m + n).

var merge = function (nums1, m, nums2, n) {
  // Initialize pointers
  let p1 = m - 1; // Last element in nums1
  let p2 = n - 1; // Last element in nums2
  let p = m + n - 1; // Last position in merged array

  // Comparing and merging elements
  while (p2 >= 0) {
    if (p1 >= 0 && nums1[p1] > nums2[p2]) {
      nums1[p] = nums1[p1];
      p1--;
    } else {
      nums1[p] = nums2[p2];
      p2--;
    }
    p--;
  }
};
