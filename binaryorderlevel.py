from binarytree import tree
class TreeNode(object):
     def __init__(self, val=0, left=None, right=None):
         self.val = val
         self.left = left
         self.right = right

     def levelOrderBottom(root):
            arr=[]
            temp=[]
            def recursive(root,arr,temp):
                if not root.right:
                    temp.append(root.right)
                if not root.left:
                    temp.append(root.left)
                if not root.right and root.left:
                    arr.append(temp)
                root.left=recursive(root.left,arr,temp)
                root.right=recursive(root.right,arr,temp)
            recursive(root,arr,temp)
            print(temp,arr)
     print(levelOrderBottom([3,9,20,None,None,15,7]))