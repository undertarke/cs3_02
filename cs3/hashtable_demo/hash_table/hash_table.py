

class HashTable:
    def __init__(self,size):
        self.size = size
        self.table = [ [] for _ in range(self.size) ]  # [ [40,70,50,110,10,20,30] , [] , [] ,[] , [] , [] , [] , [] , [] , []  ] 
    
    # value luôn luôn là number
    def hashFuntion(self,value):
        return value % self.size # 20 % 10 = 0
    
    def insert(self,value):
        index = self.hashFuntion(value)
        return self.table[index].append(value)
    
    def search(self,value):
        index = self.hashFuntion(value)
        return self.table[index]

listNumber = [40,70,50,110,10,20,30]

hashTable = HashTable(11) # số lượng phần tử càng nhiều, càng tiêu tốn tài nguyên lưu trữ
for item in listNumber:
    hashTable.insert(item)


# print(hashTable.search(30))

for item in hashTable.search(30): 
    if item == 30:
        print(item)

# size = 10
# [ [] , [] , [] ,[] , []  ] 