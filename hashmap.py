# import pytest
class HashMap:
    def __init__(self, key=None, value=None):
        self.key = key
        self.value = value
        self._size = 0
        self._capacity = 7
        self.arr = [[] for index in range(0, self._capacity)]
    DEFAULT_LOAD_FACTOR = 0.80
    def hash_function(self, key):
        hashed_key = key[0] % self._capacity
        return hashed_key
    def set(self, key, val):
        # print(f"{len(self.arr)}\n")
        h = self.hash_function(key)

        found = False
        for idx, element in enumerate(self.arr[h]):
            if len(element) == 2 and element[0] == key:
                self.arr[h][idx] = (key, val)
                found = True
                break
        if not found:
            self.arr[h].append((key, val))
        self._size += 1

        loadFactor = (1 * self._size) / self._capacity
        print(f"Current Load factor = {str(loadFactor)}")
        if (loadFactor > self.DEFAULT_LOAD_FACTOR):
            print(str(loadFactor) + " is greater than " + str(self.DEFAULT_LOAD_FACTOR))
            print("Therefore Rehashing will be done.")
 
            # Rehash
            self.rehash(h, self._capacity)
 
            print("New Size of Map: " + str(self._capacity))
 
        print("Number of pairs in the Map: " + str(self._size))
        print("Size of Map: " + str(self._size))
        # self.arr[h] = val
    def rehash(self, oldhash, size):
        new_size = (size * 2) - 1
        self._capacity = new_size
        for i in range(size, self._capacity):
            self.arr.append([])
        return (oldhash * 2) - 1 % self._capacity
    def get(self, key):
        h = self.hash_function(key)
        for element in self.arr[h]:
            if element[0] == key:
                return element[1]
        raise KeyError('key not found')
    def remove(self, key):
        h = self.hash_function(key)
        for index, element in enumerate(self.arr[h]):
            if element[0] == key:
                del self.arr[h][index]
    def size(self):
        return self._size
    def capacity(self):
        return self._capacity
    def clear(self):
        self._size = 0
        self._capacity = 7
        return self.__init__()
    def keys(self):
        print(self._size)
# key = (0, 0)
# value = 27

# key2 = (3, 2)
# value2 = 44

key3 = (4, 3)
value3 = 77

hm = HashMap()
hm.set(key3, value3)
# print(hm.get(key3))
print(hm.arr)
hm.clear()
print(hm.arr)
# hm.remove(key3)
# hm.get(key3)
# print(hm.arr)


