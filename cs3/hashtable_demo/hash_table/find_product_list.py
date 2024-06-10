# product: name, category, price
# input => name product
# output => product: category
import json

class Product:
    def __init__(self, name, price, category):
        self.name = name
        self.price = price
        self.category = category


products = [
    Product("Novel", 20, "Books"),
    Product("History_Book", 25, "Books"),
    Product("Science_Book", 30, "Books"),
    Product("Children_Book", 15, "Books"),

    Product("Apple", 1, "Fruits"),
    Product("Bread", 2, "Fruits"),
    Product("Milk", 1.5, "Fruits"),
    Product("Eggs", 3, "Fruits"),

    Product("Refrigerator", 500, "Home Appliances"),
    Product("Oven", 360, "Home Appliances"),
    Product("Microwave", 100, "Home Appliances"),
    Product("Washing_Machine", 400, "Home Appliances"),

    Product("Sofa", 700, "Furniture"),
    Product("Dining_Table", 600, "Furniture"),
    Product("Chair", 50, "Furniture"),
    Product("Bed", 800, "Furniture"),

    Product("Teddy_Bear", 20, "Toys"),
    Product("Puzzle", 15, "Toys"),
    Product("Remote_Car", 30, "Toys"),
    Product("Doll", 25, "Toys"),
    
    Product("Shampoo", 10, "Beauty, Personal Care"),
    Product("Body_Lotion", 15, "Beauty, Personal Care"),
    Product("Perfume", 50, "Beauty, Personal Care"),
    Product("Lipstick", 20, "Beauty, Personal Care")
]


class HashTable:
    def __init__(self,size):
        self.size = size
        self.table = [ [] for _ in range(self.size) ] # [ [Apple, Bread, Milk, Eggs] , [Teddy_Bear,Puzzle,Remote_Car ] ,[]  ] 
    
    def hashFunction(self, key):
        return sum(ord(char) for char in key)  % self.size #   T o y s =>
    
    def insert(self,product):
        index = self.hashFunction(product.category) # chuỗi string
        self.table[index].append(product)

    def search (self, name):
        index = self.hashFunction(name)
        return self.table[index]
    
    def recommendProduct(self, product):
        productTarget = self.search(product.category)
    
        if len(productTarget) == 0:
            return []
        
        lstNameProduct= []

        for item in productTarget:
            if item.name != product.name:
                lstNameProduct.append(item.name)
        
        return lstNameProduct


hashTable = HashTable(len(products))
for product in products:
    hashTable.insert(product)

print(hashTable.table)

productName = input("Nhập tên sản phẩm: ")

productTemp = None
for item in products:
    if item.name == productName:
        productTemp = item

# tìm kiếm sản phẩm tương tự
print(hashTable.recommendProduct(productTemp))


# thuật toán tìm kiếm tuần tự (linear search, binary search) theo tên sản phẩm
[
    {
        "id": 301079736,
        "name": "Perfume 3219601",
        "price": 1238228,
        "category": "Shoe"
    },
    {
        "id": 836105161,
        "name": "Nokia 4041354",
        "price": 30875125,
        "category": "Phone"
    }
]