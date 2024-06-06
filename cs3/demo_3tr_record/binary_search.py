import json
import time

def binary_search_by_name(products, target_name):

    low, high = 0, len(products) - 1

    while low <= high:
        mid = (low + high) // 2
        mid_name = products[mid]["name"]

        if mid_name < target_name:
            low = mid + 1
        elif mid_name > target_name:
            high = mid - 1
        else:
            return mid  # Trả về chỉ số của sản phẩm

    return -1  # Không tìm thấy sản phẩm


with open('./demo_3tr_record/data.json', 'r', encoding='utf-8') as file:
    products = json.load(file)


start_time = time.time()
# Sắp xếp danh sách theo tên
products.sort(key=lambda x: x["name"])
order_time = time.time() - start_time

# Tìm kiếm sản phẩm theo tên

stop = 0
while(int(stop) == 0):
    target_name = input("Nhập tên sản phẩm: ")
    start_time = time.time()
    result = binary_search_by_name(products, target_name)
    loading_time = time.time() - start_time 

    if result != -1:
        print(f"Đã tìm thấy sản phẩm: Name = {products[result]['name']}, id = {products[result]['id']}, time = {loading_time:.6f}")
    else:
        print("Sản phẩm không tìm thấy.")

    stop = input("continue = 0: ")
