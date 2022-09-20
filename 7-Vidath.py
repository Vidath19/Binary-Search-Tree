class Node:
    def _init_(self, key):
        self.key = key
        self.left = None
        self.right = None


# A utility function to do inorder traversal of BST
def inorder(root):
    if root is not None:
        inorder(root.left)
        print(root.key, end=" ")
        inorder(root.right)


def insert(node, key):
    # If the tree is empty, return a new node
    if node is None:
        return Node(key)

    if key < node.key:
        node.left = insert(node.left, key)
    else:
        node.right = insert(node.right, key)

    return node


def minValueNode(node):
    current = node

    # loop down to find the leftmost leaf
    while (current.left is not None):
        current = current.left

    return current


def deleteNode(root, key):
    if root is None:
        return root
    # if key is smaller than left subtree
    if key < root.key:
        root.left = deleteNode(root.left, key)

    # If the kye is greater than root key
    elif (key > root.key):
        root.right = deleteNode(root.right, key)

    # If key is same as root key
    else:
        # Node with only one child or no child
        if root.left is None:
            temp = root.right
            root = None
            return temp

        elif root.right is None:
            temp = root.left
            root = None
            return temp

        # Node with two children:
        # Inorder successor
        temp = minValueNode(root.right)

        root.key = temp.key

        # Delete the inorder successor
        root.right = deleteNode(root.right, temp.key)

    return root

    # Suppose the Tree is
    50

/ \
    30
70
/   \ / \
    20
40
60
80

root = None
root = insert(root, 50)
root = insert(root, 30)
root = insert(root, 20)
root = insert(root, 40)
root = insert(root, 70)
root = insert(root, 60)
root = insert(root, 80)

print("Inorder Traversal of Tree")
inorder(root)

print("\nDelete 20")
root = deleteNode(root, 20)
print("Inorder traversal of the modified tree")
inorder(root)

print("\nDelete 30")
root = deleteNode(root, 30)
print("Inorder traversal of the modified tree")
inorder(root)

print("\nDelete 50")
root = deleteNode(root, 50)
print("Inorder traversal of the modified tree")
inorder(root)