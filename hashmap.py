class HashMap:
    def __init__(self, key=None, value=None):
        self.key = key
        self.value = value
        self._size = 7
        self._capacity = 7
        self.arr = [None for index in range(0, self._size)]
    def hash_function(self, key):
        #self.size = 7
        hashed_key = key[0] + key[1] % self._size
        return hashed_key
    def set(self, key, val):
        h = self.hash_function(key)
        self.arr[h] = val
    def get(self, key):
        h = self.hash_function(key)
        return self.arr[h]
    def remove(self, key):
        h = self.hash_function(key)
        self.arr[h] = None
    def size(self):
        return 0
key = (0, 0)
value = 27

key2 = (3, 2)
value2 = 44

key3 = (3, 2)
value3 = 55
hm = HashMap(key, value)

hm.set(key2, value2)
# print(hm.get(key2))
print(hm.arr)
hm.remove(key2)
print(hm.arr)