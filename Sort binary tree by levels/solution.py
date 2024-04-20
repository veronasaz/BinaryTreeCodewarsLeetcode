class Node:
    '''Node class for binary tree'''
    def __init__(self, L, R, n) -> None:
        '''Constructor'''
        self.left = L
        self.right = R
        self.value = n

def tree_by_levels(node):
    '''Returns the list with elements from tree sorted by levels'''
    if not node:
        return []

    result = []
    queue = [node]
    while queue:
        current = queue.pop(0)
        result.append(current.value)
        if current.left:
            queue.append(current.left)
        if current.right:
            queue.append(current.right)
    return result
