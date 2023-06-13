import a_bst as BST
from a_bst import Node, Tree

tree = BST.initialize()

tree.root = BST.insert(tree.root, 0)
tree.root = BST.insert(tree.root, 1)
tree.root = BST.insert(tree.root, -2)
tree.root = BST.insert(tree.root, 10)
tree.root = BST.insert(tree.root, -10)
tree.root = BST.insert(tree.root, 5)
tree.root = BST.insert(tree.root, -5)

node = tree.root

print(node.left.left.right.value)