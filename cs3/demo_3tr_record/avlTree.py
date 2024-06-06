import json
import time


class Node:
    def __init__(self, key, data):
        self.key = key
        self.data = data
        self.height = 1
        self.left = None
        self.right = None

class AVLTree:
    def insert(self, root, key, data):
        if not root:
            return Node(key, data)
        elif key < root.key:
            root.left = self.insert(root.left, key, data)
        else:
            root.right = self.insert(root.right, key, data)

        root.height = 1 + max(self.getHeight(root.left), self.getHeight(root.right))
        balance = self.getBalance(root)

        # Left Left
        if balance > 1 and key < root.left.key:
            return self.rightRotate(root)

        # Right Right
        if balance < -1 and key > root.right.key:
            return self.leftRotate(root)

        # Left Right
        if balance > 1 and key > root.left.key:
            root.left = self.leftRotate(root.left)
            return self.rightRotate(root)

        # Right Left
        if balance < -1 and key < root.right.key:
            root.right = self.rightRotate(root.right)
            return self.leftRotate(root)

        return root

    def leftRotate(self, z):
        y = z.right
        T2 = y.left

        y.left = z
        z.right = T2

        z.height = 1 + max(self.getHeight(z.left), self.getHeight(z.right))
        y.height = 1 + max(self.getHeight(y.left), self.getHeight(y.right))

        return y

    def rightRotate(self, y):
        x = y.left
        T2 = x.right

        x.right = y
        y.left = T2

        y.height = 1 + max(self.getHeight(y.left), self.getHeight(y.right))
        x.height = 1 + max(self.getHeight(x.left), self.getHeight(x.right))

        return x

    def getHeight(self, root):
        if not root:
            return 0
        return root.height

    def getBalance(self, root):
        if not root:
            return 0
        return self.getHeight(root.left) - self.getHeight(root.right)


    def search(self, root, key):
        if not root or root.key == key:
            return root
        if root.key < key:
            return self.search(root.right, key)
        return self.search(root.left, key)

with open('./demo_3tr_record/data.json', 'r', encoding='utf-8') as file:
    products = json.load(file)

avl = AVLTree()
root = None

for product in products:
    try:
        root = avl.insert(root, product['name'], product)
        pass
    except Exception as e:
    # Xử lý mọi ngoại lệ
        print(f"Đã xảy ra lỗi: {product}, {e}")
   

stop = 0
while(int(stop) == 0):
    product_name = input("Nhập tên sản phẩm cần tìm: ")

    start_time = time.time()
    result = avl.search(root, product_name)
    loading_time = time.time() - start_time

    if result:
        print(f"Đã tìm thấy sản phẩm: Name = {result.data['name']}, id = {result.data['id']}, time = {loading_time:.6f}")
    else:
        print("Sản phẩm không tìm thấy")

    stop = input("continue = 0: ")
    
