# Definition for a binary tree node.
class TreeNode(object):
     def __init__(self, val=0, left=None, right=None):
         self.val = val
         self.left = left
         self.right = right
class Solution(object):
    def sumRootToLeaf( root):
        """
        :type root: TreeNode
        :rtype: int
        """
            arr=[]
            def depthfind(node,arr,data):
                if not node:
                    arr.append(str(node.val))
                if node.right:
                    depthfind(node.right,arr,data+str(node.right.val))
                if node.left:
                    depthfind(node.left,arr,data+str(node.left.val))
            depthfind(root,arr,str(root.val))
            print(arr)

print(Solution.sumRootToLeaf([1,0,1,0,1,0,1]))