"""
Given a binary array nums, return the maximum number of consecutive 1's in the array.

Example 1:
Input: nums = [1,1,0,1,1,1]
Output: 3

Explanation: The first two digits or the last three digits are consecutive 1s. The maximum number of consecutive 1s is 3.

Example 2:
Input: nums = [1,0,1,1,0,1]
Output: 2
"""


from typing import List


class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        count = 0
        maxCount = 0

        for num in nums:
            if num == 1:
                count += 1
            else:
                count = 0

            maxCount = max(count, maxCount)

        return maxCount


if __name__ == "__main__":
    sol = Solution()
    input = [1, 1, 0, 1, 1, 1]
    ans = sol.findMaxConsecutiveOnes(input)
    print(ans)

# Time Complexity: O(N), where N is the number of elements in the array.
# Space Complexity: O(1). We do not use any extra space.
