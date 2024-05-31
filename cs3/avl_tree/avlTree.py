

class AVLNode:
    def __init__(self, value):
        self.key = value
        self.left = None
        self.right = None
        self.height = 1


def getHeight(node):
    # lấy chiều cao của một node
    if not node:
        return 0
    return node.height


def updateHeight(node):
    # tính toán chiều cao của một node
    node.height = 1 + max(getHeight(node.left), getHeight(node.right))


def getBalance(node):
    # hàm tính toán chiều cao cây trái - cây phải của một node
    if not node:
        return 0
    return getHeight(node.left) - getHeight(node.right)


def insert(root, value):
    if not root:
        return AVLNode(value)

    if root.key < value:
        root.right = insert(root.right, value)
    elif root.key > value:
        root.left = insert(root.left, value)
    else:
        return root

    updateHeight(root)

    # [ -1 , 0 , 1]
    checkBalance = getBalance(root)

    # lệch trái
    if (checkBalance > 1 and value < root.left.key):
        print(f"Lệch trái khi thêm node: {value}")
        # xoay phải
        return rightRotate(root)

    # lệch trái - phải
    if (checkBalance > 1 and value > root.left.key):
        print(f"Lệch trái-phải khi thêm node: {value}")
        # xoay trái - phải
        root.left = leftRotate(root.left)
        return rightRotate(root)

    # lệch phải
    if (checkBalance < -1 and value > root.right.key):
        print(f"Lệch phải khi thêm node: {value}")
        # xoay trái
        return leftRotate(root)

    # lệch phải - trái
    if (checkBalance < -1 and value < root.right.key):
        print(f"Lệch phải-trái khi thêm node: {value}")

        # xoay phải - trái
        root.right = rightRotate(root.right)
        return leftRotate(root)

    return root


def rightRotate(treeNotBalance):
    leftChild = treeNotBalance.left
    subTree = leftChild.right

    treeNotBalance.left = subTree
    leftChild.right = treeNotBalance

    updateHeight(treeNotBalance)
    updateHeight(leftChild)

    return leftChild


def leftRotate(treeNotBalance):
    rightChild = treeNotBalance.right
    subTree = rightChild.left

    treeNotBalance.right = subTree
    rightChild.left = treeNotBalance

    updateHeight(treeNotBalance)
    updateHeight(rightChild)

    return rightChild


listNumber = ["A", "B", "C", "D", "E", "F", "W", "Z", "U", "T", "K"]
avlTree = None
# them phan tu vao AVL Tree
for item in listNumber:
    avlTree = insert(avlTree, item)


def duyet_tree(root):
    if root is None:
        return None
    return {
        'key': root.key,
        'left': duyet_tree(root.left),
        'right': duyet_tree(root.right)
    }


print(duyet_tree(avlTree))
