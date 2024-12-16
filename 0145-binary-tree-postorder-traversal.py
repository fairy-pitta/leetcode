# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []
        
        ans = []
        stack = []

        last_visited = None 
        cur = root 

        while stack or cur:
            if cur: 
                stack.append(cur)
                cur = cur.left
            else:
                peek_node = stack[-1]
                if peek_node.right and last_visited != peek_node.right:
                    cur = peek_node.right 
                else:
                    ans.append(peek_node.val)
                    last_visited = stack.pop()
        
        return ans