# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
import random
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        prev = [-inf]
        answer = [True]
        def dfs(node):
            if not node:
                return
            dfs(node.left)
            if node.val>prev[0]:
                prev[0] = node.val
            else:
                answer[0] = False
                return
            dfs(node.right)
        dfs(root)
            
        return answer[0]