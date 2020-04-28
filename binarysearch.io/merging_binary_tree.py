# class Tree:
#     def __init__(self, val, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


class Solution:
    def solve(self, node0, node1):
        # Write your code here
        def helper(node1, node2, newNode):
            if node1 is None and node2 is None:
                return None

            if node1 and node2:
                newNode = Tree(node1.val + node2.val)
                newNode.left = helper(node1.left, node2.left, newNode.left)
                newNode.right = helper(node1.right, node2.right, newNode.right)
            elif node1:
                newNode = Tree(node1.val)
                newNode.left = helper(node1.left, None, newNode.left)
                newNode.right = helper(node1.right, None, newNode.right)
            elif node2:
                newNode = Tree(node2.val)
                newNode.left = helper(node2.left, None, newNode.left)
                newNode.right = helper(node2.right, None, newNode.right)

            return newNode
        return helper(node0, node1, None)


class Tree:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def solve(self, node0, node1):
        # Write your code here
        def helper(node1, node2):
            node1.val += node2.val

            if node2.left:
                if node1.left is None:
                    node1.left = Tree(0)
                helper(node1.left, node2.left)

            if node2.right:
                if node1.right is None:
                    node1.right = Tree(0)
                helper(node1.right, node2.right)
        helper(node0, node1)
        return node0
