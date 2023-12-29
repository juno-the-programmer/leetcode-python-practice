'''
Given the root of a binary tree and an integer targetSum, return all root-to-leaf paths where the sum of the node values in the path equals targetSum. Each path should be returned as a list of the node values, not node references.

A root-to-leaf path is a path starting from the root and ending at any leaf node. A leaf is a node with no children.

Example 1:
Input: root = [5,4,8,11,null,13,4,7,2,null,null,5,1], targetSum = 22
Output: [[5,4,11,2],[5,8,4,5]]
Explanation: There are two paths whose sum equals targetSum:
5 + 4 + 11 + 2 = 22
5 + 8 + 4 + 5 = 22

Example 2:
Input: root = [1,2,3], targetSum = 5
Output: []

Example 3:
Input: root = [1,2], targetSum = 0
Output: []
'''

from typing import List, Optional


class TreeNode:
    def __init__(self, val=None, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:

        def dfs(root, targetSum):
            if not root:
                return []

            if not root.left and not root.right and targetSum == root.val:
                return [[root.val]]

            targetSum -= root.val

            leftPath = dfs(root.left, targetSum)
            rightPath = dfs(root.right, targetSum)

            left = [[root.val] + l for l in leftPath]
            right = [[root.val] + r for r in rightPath]
            return left + right

        return dfs(root, targetSum)


root = TreeNode(5)
node1 = TreeNode(4)
node2 = TreeNode(8)
node3 = TreeNode(11)
node4 = TreeNode(7)
node5 = TreeNode(2)
node6 = TreeNode(13)
node7 = TreeNode(4)
node8 = TreeNode(5)
node9 = TreeNode(1)


root.left = node1
root.right = node2
node1.left = node3
node3.left = node4
node3.right = node5
node2.left = node6
node2.right = node7
node7.left = node8
node7.right = node9


if __name__ == "__main__":
    sol = Solution()
    ans = sol.pathSum(root, 22)
    print(ans)
