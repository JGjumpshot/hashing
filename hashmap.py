"""hashmap adt"""
class HashMap:
    def __init__(self, key=None, value=None):
        """init function"""
        self.key = key
        self.value = value
        self._size = 0
        self._capacity = 7
        self.arr = [[] for index in range(0, self._capacity)]
    DEFAULT_LOAD_FACTOR = 0.80

    def hash_function(self, key):
        """hash function"""
        hashed_key = key[0] % self._capacity
        return hashed_key

    def set(self, key, val):
        """set key value pair"""
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

        load_factor = (1 * self._size) / self._capacity
        # print(f"Current Load factor = {str(load_factor)}")
        if load_factor > self.DEFAULT_LOAD_FACTOR:
            self.rehash(h, self._capacity)

    def rehash(self, oldhash, size):
        """rehash function"""
        new_size = (size * 2) - 1
        self._capacity = new_size
        for i in range(size, self._capacity):
            self.arr.append([])
        return (oldhash * 2) - 1 % self._capacity

    def get(self, key):
        """get function"""
        h = self.hash_function(key)
        for element in self.arr[h]:
            if element[0] == key:
                return element[1]
        raise KeyError('key not found')

    def remove(self, key):
        """remove function"""
        h = self.hash_function(key)
        for index, element in enumerate(self.arr[h]):
            if element[0] == key:
                del self.arr[h][index]

    def size(self):
        """size function"""
        return self._size

    def capacity(self):
        """capacity function"""
        return self._capacity

    def clear(self):
        """clear function"""
        self._size = 0
        self._capacity = 7
        return self.__init__()

    def keys(self):
        """key function"""
        keys = []
        for i in self.arr:
            if i != []:
                print(i[0][0])
                keys.append(i[0][0])
        return keys
