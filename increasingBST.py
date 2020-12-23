def increasingBST(self, root):
    def recurse(stack,node):
        if node is None:
            return
        recurse(stack,node.left)
        stack.append(stack.node)
        recurse(stack,node.right)
        stack=[]
        recurse(stack,root)
        for i in range(len(stack[:-1])):
            stack[i].right=stack[i+1]
            stack[i].left=None
        return stack[0]

        def recurse(node, stack):
            if node is None:
                return

            recurse(node.left, stack)
            stack.append(node)
            recurse(node.right, stack)

        stack = []
        recurse(root, stack)
        for i in range(len(stack[:-1])):
            stack[i].right = stack[i + 1]
            stack[i].left = None
        return stack[0]