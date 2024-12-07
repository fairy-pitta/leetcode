# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:

        def recursive(left, right):

            if not left and not right:
                return True 
            elif not left or not right:
                return False
            elif left.val != right.val:
                return False
            
            check1 = recursive(left.left, right.right)
            check2 = recursive(left.right, right.left)

            return check1 and check2

        if not root:
            return True 
        
        return recursive(root.left, root.right)