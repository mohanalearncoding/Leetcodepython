from binarytreestudy import TreeNode


class Solution:
     def __init__(self, val=0, left=None, right=None):
               self.val = val
               self.left = left
               self.right = right
     def increasingBST( root: TreeNode, tail=None) -> TreeNode:
         if not root:return tail
         result = self.increasingBST(root.left, root)
         root.left = None
         root.right = self.increasingBST(root.right, tail)
         return result