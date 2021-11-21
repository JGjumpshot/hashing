class HashMap:
    def __init__(self, key=None, value=None):
        self.key = key
        self.value = value
        self._size = 0
        self._capacity = 7
        self.slots = [None] * self._capacity
        self.data = [None] * self._capacity
        # self.arr = [[] for index in range(0, self._size)]
    def hash_function(self, key, size):
        hashed_key = key[0] % size
        return hashed_key
    def set(self, key, val):
        hashvalue = self.hash_function(key, self._capacity)
        if self.slots[hashvalue] == None:
            self.slots[hashvalue] = key
            self.data[hashvalue] = val
        else:
            if self.slots[hashvalue] == key:
                self.data[hashvalue] = val
            else:
                nextslot = self.rehash(hashvalue, len(self.slots))
                while self.slots[nextslot] != None and self.slots[nextslot] != key:
                    nextslot = self.rehash(nextslot,len(self.slots))

                if self.slots[nextslot] == None:
                    self.slots[nextslot] = key
                    self.data[nextslot] = val
                else:
                    self.data[nextslot] = val
    def rehash(self,oldhash,size):
        return (oldhash * 2) - 1 % size
    def get(self, key):
        startslot = self.hash_function(key,len(self.slots))

        data = None
        stop = False
        found = False
        position = startslot
        while self.slots[position] != None and not found and not stop:
            if self.slots[position] == key:
                found = True
                data = self.data[position]
            else:
                position=self.rehash(position,len(self.slots))
            if position == startslot:
                stop = True
        if found is not False:
            print(f"data$$${data}")
            return data
        else: 
            return found
    def remove(self, key):
        remove = self.get(key)
        if remove is not False:
            self.data[key] = None
        else:
            raise KeyError('Key not found')
    def size(self):
        return self._size
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
# hm.set(key2, value2)
# print(hm.get(key2))
# print(hm.data)
keys = [(r,r) for r in (range(10))]
print(keys)
values = list(range(1, 11))
for k,v in zip(keys,values):
    hm.set(k,v)