"""from binarytree import Node
from binarytree import build
root=Node(3)
root.right=Node(6)
root.left=Node(0)
arr=[3, 6, 8, 2, 11, None, 13]
binary_t=build(arr)


print(binary_t)"""
from idlelib.tree import TreeNode


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val=val
        self.left=left
        self.right=right
    def merge(t1: TreeNode, t2: TreeNode) -> TreeNode:
        if t1 is None: return t2
        if t2 is None: return t1
        t1+=t2
        t1.right=self.merge(t1.right,t2.right)
        t1.left=self.merge(t1.left,t2.left)
        return t1
    print(merge([1,3,2,5],[2,1,3,None,4,None,7]))