class Node:
    def __init__(self, data) -> None:
        '''Constructor'''
        self.data = data
        self.left = None
        self.right = None

def pre_order(node):
    '''
    1. Visit the root
    2. Traverse the left subtree (left node)
    3. Traverse the right subtree (right node)
    '''
    def pre(node, result):
        if node:
            result.append(node.data)
            pre(node.left, result)
            pre(node.right, result)

    result = []
    if node:
        pre(node, result)

    return result

def in_order(node):
    '''
    1. Traverse the left subtree (left node)
    2. Visit the root
    3. Traverse the right subtree (right node)
    '''
    def in_or(node, result):
        if node:
            in_or(node.left, result)
            result.append(node.data)
            in_or(node.right, result)

    result = []
    if node:
        in_or(node, result)

    return result

def post_order(node):
    '''
    1. Traverse the left subtree (left node)
    2. Traverse the right subtree (right node)
    3. Visit the root
    '''
    def post(node, result):
        if node:
            post(node.left, result)
            post(node.right, result)
            result.append(node.data)

    result = []
    if node:
        post(node, result)

    return result

# a = Node("A")
# b = Node("B")
# c = Node(1)

# a.left = b
# a.right = c

# print(pre_order(a)) # ['A', 'B', 1]
# print(in_order(a)) # ['B', 'A', 1]
# print(post_order(a)) # ['B', 1, 'A]

# d = Node("D")
# c.left = d

# print(pre_order(a)) # ['A', 'B', 'D', 1]
# print(in_order(a)) # ['B', 'D', 'A', 1]
# print(post_order(a)) # ['B', 'D', 'C', 'A']
