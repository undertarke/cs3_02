
class HashTable:
    def __init__(self, size):
        self.size = size
        # [ [] ,  [] , [] , [] , [] , [] , [] ]
        self.table = [[] for i in range(size)]

    def hashFunction(self, value):
        return value % self.size

    def insert(self, value):
        index = self.hashFunction(value)
        self.table[index].append(value)

    def search(self, value):
        index = self.hashFunction(value)
        for number in self.table[index]:
            if number == value:
                print("Tìm thấy tại index", index)
                return

        print("Không tìm thấy")

    def delete(self, value):
        index = self.hashFunction(value)
        # self.table[index].remove(value)

        temp = [item for item in self.table[index] if item != value]
        self.table[index] = temp

    def update(self, value):
        index = self.hashFunction(value)
        self.table[index]

        # size = 7
lstNumber = [25, 14, 33, 11, 10, 20, 30]

hashTable = HashTable(len(lstNumber))

for number in lstNumber:
    hashTable.insert(number)

print(hashTable.table)

hashTable.delete(11)

print(hashTable.table)
