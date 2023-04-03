# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def widthOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        q = [[root,0]]
        width = 0
        while q:
            width = max(width,q[-1][-1]-q[0][1]+1)
            next_level = []
            for node,idx in q:
                if node.left:
                    next_level.append([node.left,2*idx])
                if node.right:
                    next_level.append([node.right,2*idx+1])
            q = next_level
        return width
            
        