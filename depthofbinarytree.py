from idlelib.tree import TreeNode


class Solution:
    def maxDepth(self, root: TreeNode) -> int:
        p=[]
        depth=0
        p.append(root)
        if not root:
            return 0
        while p:
            temp=[]
            depth+=1
            for node in p:
                if node.left:
                    temp.append(node.left)
                if node.right:
                    temp.append(node.right)
            p=temp
        return depth