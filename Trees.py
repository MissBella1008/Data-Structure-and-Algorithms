class Node:
    def __init__(self, key):
        self.left = None
        self.right = None
        self.val = key

# Inorder traversal (Left, Root, Right)
def inorder(root):
    if root:
        inorder(root.left)
        print(root.val, end=" ")
        inorder(root.right)

# Preorder traversal (Root, Left, Right)
def preorder(root):
    if root:
        print(root.val, end=" ")
        preorder(root.left)
        preorder(root.right)

# Postorder traversal (Left, Right, Root)
def postorder(root):
    if root:
        postorder(root.left)
        postorder(root.right)
        print(root.val, end=" ")

# Insert a node into a Binary Search Tree (BST)
def insert(root, key):
    if root is None:
        return Node(key)
    if key < root.val:
        root.left = insert(root.left, key)
    else:
        root.right = insert(root.right, key)
    return root

# Search for a node in a BST
def search(root, key):
    if root is None or root.val == key:
        return root
    if key < root.val:
        return search(root.left, key)
    return search(root.right, key)

# Delete a node from a BST
def delete(root, key):
    if root is None:
        return root
    if key < root.val:
        root.left = delete(root.left, key)
    elif key > root.val:
        root.right = delete(root.right, key)
    else:
        if root.left is None:
            return root.right
        elif root.right is None:
            return root.left
        temp = minValueNode(root.right)
        root.val = temp.val
        root.right = delete(root.right, temp.val)
    return root

# Find the node with the minimum value in a BST
def minValueNode(node):
    current = node
    while current.left is not None:
        current = current.left
    return current

# Driver code
if __name__ == "__main__":
    root = None
    values = [50, 30, 70, 20, 40, 60, 80]
    for v in values:
        root = insert(root, v)
    
    print("Inorder traversal:")
    inorder(root)
    print("\nPreorder traversal:")
    preorder(root)
    print("\nPostorder traversal:")
    postorder(root)
