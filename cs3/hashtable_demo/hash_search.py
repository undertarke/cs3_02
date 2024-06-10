
import json
import time


class HashTable:
    def __init__(self, size):
        self.size = size
        self.table = [[] for _ in range(self.size)]

    def hash_function(self, key):
        return sum(ord(char) for char in key) % self.size

    def insert(self, product):
        index = self.hash_function(product['name'])
        self.table[index].append(product)

    def search(self, name):
        index = self.hash_function(name)

        return self.table[index]

    def recommend_products(self, product_name):

        target_product = self.search(product_name)

        if len(target_product) == 0:
            return []

       

        return target_product


with open('data.json', 'r', encoding='utf-8') as file:
    products = json.load(file)

hash_table = HashTable(len(products))
for product in products:
    hash_table.insert(product)


stop = 0
while int(stop) == 0:
    product_name = input("Enter product name: ")

    start_time = time.time()
    recommendations = hash_table.recommend_products(product_name)

    loading_time = time.time() - start_time

    result = []

    for product_hash in recommendations:
        if product_name == product_hash['name']:
            result = product_hash


    print(f"Đã tìm thấy sản phẩm: Name = {result['name']}, id = {result['id']}, time = {loading_time:.6f}")

    stop = input("Press 0 continue!: ")
