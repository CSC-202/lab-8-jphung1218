# bst.py
## author - nick s.
## .... this was supposed to be your lab 8, but now you need to write less code :)


# given to students
class Node:
    left: any
    right: any
    value: any

    def __init__(self, val, left=None, right=None):
        self.left = left
        self.right = right
        self.value = val


# given to students
class Tree:
    root: Node
    def __init__(self, root=None):
        self.root = root


# NOT given to students
def initialize() -> Tree:
    return Tree() # TODO


# NOT given to students
def isEmpty(tree: Tree) -> bool:
    return tree.root is None # TODO


# given to the students
def height(root: Node) -> int:
    if root is None:
        return 0
    else:
        h_left: int = height(root.left)
        h_right: int = height(root.right)
        return max(h_left, h_right) + 1


# given to the students
def preorder_traversal(tree: Node, level:int=0):
    if level == 0:
        print('pre order traversal')
    if tree != None:
        print(f' level = {level:^3d} : value = {tree.value}')
        preorder_traversal(tree.left, level+1)
        preorder_traversal(tree.right, level+1)


# NOT given to the students
def inorder_traversal(tree: Node, level:int=0):
    if level == 0:
        print('in order traversal')
    if tree != None:
        inorder_traversal(tree.left, level+1)
        print(f' level = {level:^3d} : value = {tree.value}')
        inorder_traversal(tree.right, level+1)


# NOT given to the students
def postorder_traversal(tree: Node, level:int=0):
    if level == 0:
        print('post order traversal')
    if tree != None:
        postorder_traversal(tree.left, level+1)
        postorder_traversal(tree.right, level+1)
        print(f' level = {level:^3d} : value = {tree.value}')


# NOT given to the students
def search(root: Node, value: int) -> Node:
    # base cases
    if root is None:
        return None
    elif root.left is None and root.right is None: # TODO
        if root.value == value:
            return root
        else:
            return None # TODO
    # recursive step
    else:
        if root.value == value: # TODO
            return root # TODO
        else:
            if root.left is not None:
                root = root.left # TODO
            if root.right is not None:
                root = root.right


# NOT given to students
def insert(root: Node, value: int) -> Node:
    if root is None: # TODO
        root = Node(value)
        return root # TODO
    else:
        if value < root.value and root.left is None:
            root.left = Node(value)
        elif value > root.value and root.right is None:
            root.right = Node(value)
        else:
            if value < root.value and root.left is not None:
                insert(root.left, value)
            elif value > root.value and root.right is not None:
                insert(root.right, value)
    return root #switch the ifelif & else statemenst??


# given to students
def remove(root: Node, value: int) -> Node:
    def getMin(v: Node):
        current = v
        while current.left is not None:
            current = current.left
        return current
    if root is None:
        return None
    if value < root.value:
        root.left = remove(root.left, value)
    elif value > root.value:
        root.right = remove(root.right, value)
    else:
        if root.left is None:
            temp = root.right
            root = None
            return temp
        elif root.right is None:
            temp = root.left
            root = None
            return temp
        temp = getMin(root.right)
        root.value = temp.value
        root.right = remove(root.right, temp.value)
    return root


# given to students
# uses in order traversal
def storeNodes(v: Node, nodes:list):
    if v is None:
        return
    else:
        storeNodes(v.left, nodes)
        nodes.append(v)
        storeNodes(v.right, nodes)


num_iter: int = 0

# given to students
def balance_tree(tree: Tree) -> Tree:
    global num_iter
    def helper(nodes: list, start: int, end: int) -> Node:
        global num_iter
        num_iter += 1
        if start > end:
            return None
        else:
            mid: int = (start + end) // 2 # you divide by two
            w: Node = nodes[mid]
            w.left = helper(nodes, start, mid - 1) # you do half work (first time)
            w.right = helper(nodes, mid + 1, end) # you do half work (second time)
            return w
    # end helper
    nodes: list = list()
    storeNodes(tree.root, nodes)
    n: int = len(nodes)
    tree.root = helper(nodes, 0, n - 1)
    print(f'num iters to balance {num_iter}')
    return tree
