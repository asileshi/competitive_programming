# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def countNodes(self, root: Optional[TreeNode]) -> int:
        ans = 0
        def dfs(node):
            nonlocal ans
            if not node:
                return 
            ans+=1
            dfs(node.left)
            dfs(node.right)
            return ans
        if not root:
            return 0
        return dfs(root)