class HashMap:
    def __init__(self, key=None, value=None):
        self.key = key
        self.value = value
        self._size = 0
        self._capacity = 20
        # self._input = 0
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
            self.rehash()
 
            print("New Size of Map: " + str(self._size))
 
        print("Number of pairs in the Map: " + str(self._size))
        print("Size of Map: " + str(self._size))
        # self.arr[h] = val
    def rehash(self):
        print("\n***Rehashing Started***\n")
 
        # The present bucket list is made temp
        temp = self.arr
 
        # New bucketList of double the old size is created
        slots = (2 * len(self.arr))
        print(slots)
        for i in range(2 * self._capacity - 1):
            # Initialised to null
            temp.append([])
 
        # Now size is made zero
        # and we loop through all the nodes in the original bucket list(temp)
        # and insert it into the new list
        self._size = 0
        self._capacity *= 2
 
        for i in range(len(temp)):
 
            # head of the chain at that index
            head = temp[i]
 
            while (head != []):
                key = head[i][0]
                val = head[i][1]
 
                # calling the insert function for each node in temp
                # as the new list is now the bucketArray
                self.set(key, val)
                head = temp[i + 1]
 
        print("\n***Rehashing Ended***")
    def get(self, key):
        h = self.hash_function(key)
        if h > 0:
            h = self.hash_function(key) - 1
        print(f"h is: {h}")
        for element in self.arr[h]:
            if element[0] == key:
                return element[1]
            else:
                raise KeyError(element[0])
    def remove(self, key):
        h = self.hash_function(key)
        if h > 0:
            h = self.hash_function(key) - 1
        for index, element in enumerate(self.arr[h]):
            if element[0] == key:
                del self.arr[h][index]
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

key3 = (4, 3)
value3 = 77

# key3 = (3, 2)
# value3 = 55
# hm = HashMap(key, value)

# hm.set(key2, value2)
# # print(hm.get(key2))
# print(hm.arr)
# hm.remove(key2)
# print(hm.arr)
hm = HashMap()
# print(hm.arr)
# hm.set(key2, value2)
# hm.set(key3, value3)
# hm.set((5,4), 23)
# hm.set((2,1), 71)
# hm.set((2,2), 12)
# hm.set((2,0), 34)
# print(hm.size)
# print(hm.arr)
# print(hm.get(key2))
# hm.remove(key2)
# hm.remove(key3)
print(hm.get((3,3)))
# keys = [(r,r) for r in (range(10))]
# print(keys)
# values = list(range(1, 11))
# for k,v in zip(keys,values):
#     hm.set(k,v)