root = {
    "key": 13,
    "left": {
        "key": 4,
        "left": {
            "key": 2,
            "left": {},
            "right": {}
        },
        "right": {
            "key": 5,
            "left": {},
            "right": {}
        }
    },
    "right": {
        "key": 20,
        "left": {
            "key": 14,
            "left": {},
            "right": {}
        },
        "right": {
            "key": 22,
            "left": {},
            "right": {}
        }
    }
}


class Node:
    def __init__(self, phone):
        self.key = phone["price"]
        self.info = phone
        self.left = None
        self.right = None


class BSTree:
    def __init__(self):
        self.root = None

    def insert_node(self, phone):
        self.root = self.insert(self.root, phone)

    def insert(self, root, phone):

        # thêm nút gốc
        if root is None:
            return Node(phone)

        # root , left , right
        if phone["price"] < root.key:
            root.left = self.insert(root.left, phone)
        elif phone["price"] > root.key:
            root.right = self.insert(root.right, phone)

        return root

    def get_tree(self):
        return self.in_order(self.root)

    def in_order(self, root):
        if root is None:
            return ''

        return f" {self.in_order(root.left)} - {root.key} - {self.in_order(root.right)} "

    def find_price(self, min, max):
        result = []
        result = self._find_price(self.root, min, max, result)
        return result

    def _find_price(self, root, min, max, result):
        
        if root is None:
            return
        if min <= root.key <= max:
            result.append(root.info["name"])

        self._find_price(root.left, min, max, result)

        self._find_price(root.right, min, max, result)

        return result


lstPhone = [
    {
        "name": "phone A",
        "price": 5
    },
    {
        "name": "phone B",
        "price": 1
    },
    {
        "name": "phone C",
        "price": 2
    },
    {
        "name": "phone D",
        "price": 10
    },
    {
        "name": "phone E",
        "price": 6
    },
    {
        "name": "phone F",
        "price": 3
    }
]

bsTree = BSTree()

for phone in lstPhone:
    bsTree.insert_node(phone)

# print(bsTree.get_tree())

# tìm kiếm giá tiền sản phẩm theo min và max
# Input : 2 - 7

min = 2
max = 7

result = bsTree.find_price(min, max)

print(result)
