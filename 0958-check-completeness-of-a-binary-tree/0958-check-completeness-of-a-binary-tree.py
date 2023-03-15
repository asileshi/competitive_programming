# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isCompleteTree(self, root: Optional[TreeNode]) -> bool:
        cur = [root]
        bfs = []
        while cur:
            bfs.append([nd.val for nd in cur])
            non = False
            nxt = []
            for nd in cur:
                if nd.left:
                    if non:
                        return False
                    nxt.append(nd.left)
                else:
                    non = True
                if nd.right:
                    if non:
                        return False
                    nxt.append(nd.right)
                else:
                    non = True
            cur = nxt
        for i in range(1,len(bfs)-1):
            if len(bfs[i])!=len(bfs[i-1])*2:
                return False
        return True