# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:

        if not root:
            return 0

        depth = 0
        max_depth = 0

        cur = root 
        stack = []
        stack.append((root, 1))

        while stack or cur:
            while cur:
                depth += 1
                stack.append((cur, depth))
                max_depth = max(max_depth, depth)
                cur = cur.left
            
            cur, depth = stack.pop()
        

            cur = cur.right
        
        return max_depth
        