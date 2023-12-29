'''
You are given an integer array nums and an integer target.

You want to build an expression out of nums by adding one of the symbols '+' and '-' before each integer in nums and then concatenate all the integers.

For example, if nums = [2, 1], you can add a '+' before 2 and a '-' before 1 and concatenate them to build the expression "+2-1".
Return the number of different expressions that you can build, which evaluates to target.

 

Example 1:

Input: nums = [1,1,1,1,1], target = 3
Output: 5
Explanation: There are 5 ways to assign symbols to make the sum of nums be target 3.
-1 + 1 + 1 + 1 + 1 = 3
+1 - 1 + 1 + 1 + 1 = 3
+1 + 1 - 1 + 1 + 1 = 3
+1 + 1 + 1 - 1 + 1 = 3
+1 + 1 + 1 + 1 - 1 = 3
Example 2:

Input: nums = [1], target = 1
Output: 1
'''


from typing import List


class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:

        def recursion(nums, target):
            if target == 0 and len(nums) == 0:
                return 1

            if len(nums) == 0:
                return 0

            size = 0
            size += recursion(nums[1:], target + nums[0])
            size += recursion(nums[1:], target - nums[0])
            return size

        return recursion(nums, target)


if __name__ == "__main__":
    sol = Solution()
    ans = sol.findTargetSumWays(
        [16, 40, 9, 17, 49, 32, 30, 10, 38, 36, 31, 22, 3, 36, 32, 2, 26, 17, 30, 47], 49)
    print(ans)
