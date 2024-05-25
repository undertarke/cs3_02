# ctrl + J

# crawler data

# MACBOOK => pip3
# Windows => pip install requests
# pip list

# requests => gọi API

import requests
import json

url = "https://tiki.vn/api/personalish/v1/blocks/listings"

headers = {
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36"
}

params = {
    "limit": 10,
    "include": "advertisement",
    "aggregations": 2,
    "version": "home-persionalized",
    "trackity_id": "3b6a70f5-8835-00a2-78dd-e147ec338fe3",
    "category": 2549,
    "page": 2,
    "urlKey": "do-choi-me-be"
}

lstProduct = []


# for page in range(1, 2):
#     params["page"] = page
#     response = requests.get(url, headers=headers, params=params)

#     # print(response.json().get("data")[0])
#     if response.status_code == 200:  # thành công
#         print("Request product ...")
#         for item in response.json().get("data"):
#             product = {
#                 "id": item["id"],
#                 "sku": item["sku"],
#                 "name": item["name"],
#                 "price": item["price"],
#                 "image": item["thumbnail_url"]
#             }
#             lstProduct.append(product)

# with open("data_product.json", 'w', encoding="utf-8") as file:
#     json.dump(lstProduct, file, ensure_ascii=False)


with open("data_product.json",'r', encoding="utf-8") as file:
    lstProduct = json.load(file)

print(lstProduct)