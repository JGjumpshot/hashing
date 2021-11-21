class HashMap:
    def __init__(self, key=None, value=None):
        self.key = key
        self.value = value
        self._size = 0
        self._capacity = 7
        self._input = 0
        self.arr = [[] for index in range(0, self._size)]
    def hash_function(self, key):
        #self.size = 7
        hashed_key = key[0] + key[1] % self._size
        return hashed_key
    def set(self, key, val):
        self._size += 1
        # print(type(self.arr))
        print(f"{len(self.arr)}\n")
        for i in range(len(self.arr)):
            print(self.arr[i])
        # if self._size
        if self._input > len(self.arr) // 2:
            self._capacity = (2 * len(self.arr) - 1)
        h = self.hash_function(key)
        self.arr[h] = val
        self._input += 1
    def get(self, key):
        h = self.hash_function(key)
        return self.arr[h]
    def remove(self, key):
        h = self.hash_function(key)
        self.arr[h] = None
    def size(self):
        return self._size
        return self.arr
    def capacity(self):
        return self._capacity
    def clear(self):
        return self.__init__
# key = (0, 0)
# value = 27

key2 = (3, 2)
value2 = 44

# key3 = (3, 2)
# value3 = 55
# hm = HashMap(key, value)

# hm.set(key2, value2)
# # print(hm.get(key2))
# print(hm.arr)
# hm.remove(key2)
# print(hm.arr)
hm = HashMap()
hm.set(key2, value2)
hm.size()
# keys = [(r,r) for r in (range(10))]
# print(keys)
# values = list(range(1, 11))
# for k,v in zip(keys,values):
#     hm.set(k,v)