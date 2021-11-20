class HashMap:
    def __init__(self, key=None, value=None):
        self.key = key
        self.value = value
        self._size = 7
        self._capacity = 7
        self.arr = [None for index in range(0, self._size)]
        print(self.arr)
    def hash_function(self, key):
        #self.size = 7
        hashed_key = key[0] + key[1] % self._size
        return hashed_key
    def size(self):
        return 0
    def set(self, key, value):
        hash_key = self.hash_function(key)
        key_exists = False
        slot = self.arr[hash_key]
        slot_value = 0
        for i, kv in enumerate(slot):
            k, v = kv
            if key == k:
                key_exists = True
                slot_value = i
                break
        if key_exists:
            slot[slot_value] = ((key, value))
        else:
            slot.append((key,value))
    def get(self, key):
        hash_key = self.hash_function(key)
        slot = self.arr[hash_key]
        for kv in slot:
            k, v = kv
            if key == k:
                return v
        raise KeyError("key doesn't exist")
    def capacity(self):
        return self._capacity
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