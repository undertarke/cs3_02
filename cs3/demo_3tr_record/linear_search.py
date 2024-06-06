import json
import time


# Hàm tìm kiếm tuyến tính
def linear_search(array, target):
    i = 0
    for product in array:
        i+=1
        if product['name'] == target:
            print(i)
            return product
    return None


with open('./demo_3tr_record/data.json', 'r', encoding='utf-8') as file:
    products = json.load(file)


stop = 0
while(int(stop) == 0):
    # Tìm kiếm sản phẩm theo tên
    product_name = input("Nhập tên sản phẩm cần tìm: ")


    start_time = time.time()
    result = linear_search(products, product_name)
    loading_time = time.time() - start_time


    if result:
        print(f"Đã tìm thấy sản phẩm: Name = {result['name']}, id = {result['id']}, time = {loading_time:.6f}")
    else:
        print("Không tìm thấy sản phẩm!")
    stop = input("continue = 0: ")

