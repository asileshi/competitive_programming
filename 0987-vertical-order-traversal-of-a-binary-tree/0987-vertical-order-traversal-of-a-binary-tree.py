# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def verticalTraversal(self, root: Optional[TreeNode]) -> List[List[int]]:
        mat = defaultdict(list)
        def dfs(node,row, col):
            if not node:
                return
            dfs(node.left, row + 1, col - 1)
            dfs(node.right, row + 1, col + 1)
            mat[col].append((row, node.val))
        dfs(root, 0, 0)
        result = sorted(mat.items())
        answer = []
        for _, res in result:
            res.sort()
            answer.append(list(map(lambda x:x[1], res)))
        return answer
    
    
    
    