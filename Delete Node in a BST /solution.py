'''Delete TreeNode in a BST'''

class TreeNode:
    '''TreeNode class'''
    def __init__(self, val=0, left=None, right=None):
        '''Constructor'''
        self.val = val
        self.left = left
        self.right = right

class Solution:
    '''Class for solution'''
    def deleteNode(self, root: TreeNode, key: int):
        '''Delete the node fron the binary search tree'''
        if not root:
            return None

        if key < root.val:
            root.left = self.deleteNode(root.left, key)
        elif key > root.val:
            root.right = self.deleteNode(root.right, key)
        else:
            if not root.left:
                return root.right
            if not root.right:
                return root.left

            root.val = self.min_value(root.right)
            root.right = self.deleteNode(root.right, root.val)

        return root

    def min_value(self, root):
        minvalue = root.val
        while root.left:
            minvalue = root.left.val
            root = root.left
        return minvalue
