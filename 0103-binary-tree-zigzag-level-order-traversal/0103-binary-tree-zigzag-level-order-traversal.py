# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
        level = 1
        cur = [root]
        ans = []
        while cur:
            next_level = []
            cur_val = []
            for node in cur:
                cur_val.append(node.val)
                if node.left:
                    next_level.append(node.left)
                if node.right:
                    next_level.append(node.right)
            if level%2==0:
                ans.append(cur_val[::-1])
            else:
                ans.append(cur_val)
            cur = next_level
            level+=1
        return ans
            