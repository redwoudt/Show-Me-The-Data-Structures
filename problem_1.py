from collections import deque


class LRU_Cache(object):

    def __init__(self, capacity):
        # Initialize class variables
        self.queue = deque()
        self.cache = {}
        self.current_capacity = 0
        self.max_capacity = capacity
        self.counter = {}

    def get(self, key):
        # Retrieve item from provided key. Return -1 if nonexistent.
        # check if key is in cache
        if self.cache.get(key, None) is None:
            return -1
        
        # check if lru key is the same and remove it 
        if len(self.queue) > 0:
            lru = self.queue[-1]
            if lru == key:
                self.queue.pop()
                self.counter[key] = self.counter.get(key, 1) - 1

        # append key to lru queue and increase count
        self.queue.appendleft(key)
        self.counter[key] = self.counter.get(key, 0) + 1

        # return cached value
        return self.cache[key]


    def set(self, key, value):
        # check for edge case
        if self.max_capacity == 0:
            return

        # Set the value if the key is not present in the cache. If the cache is at capacity remove the oldest item. 
        # update count of value
        self.counter[key] = self.counter.get(key, 0) + 1
        self.queue.appendleft(key)
        
        # check for new key
        if self.counter[key] == 1:
            self.current_capacity += 1
        
        # update capacity if needed
        if self.current_capacity > self.max_capacity:
            # remove extra fields
            while self.counter[self.queue[-1]] > 1:
                self.queue.pop()
            # now remove lru
            self.counter[self.queue[-1]] = 0
            self.cache[self.queue[-1]] = None
            self.queue.pop()
        
        # update cache
        self.cache[key] = value
 

def test_general_use():

    our_cache = LRU_Cache(5)

    our_cache.set(1, 1);
    our_cache.set(2, 2);
    our_cache.set(3, 3);
    our_cache.set(4, 4);


    print("Expeting 1: {}".format(our_cache.get(1)))      # returns 1

    print("Expeting 2: {}".format(our_cache.get(2)))      # returns 2
    print("Expeting -1: {}".format(our_cache.get(9)))      # returns -1 because 9 is not present in the cache

    our_cache.set(5, 5) 
    our_cache.set(6, 6)

    print("Expeting -1: {}".format(our_cache.get(3)))      # returns -1 because the cache reached it's capacity and 3 was the least recently used entry


def test_empty_cache():
    our_cache = LRU_Cache(5)
    print("Expeting -1: {}".format(our_cache.get(3)))      # returns -1 because the cache is empty


def test_0_capacity_cache():
    our_cache = LRU_Cache(0)
    our_cache.set(5, 5)
    print("Expeting -1: {}".format(our_cache.get(5)))      # returns -1 because the cache is empty


def test_1_capacity_cache():
    our_cache = LRU_Cache(1)
    our_cache.set(5, 5)
    our_cache.set(6, 6)
    print("Expeting -1: {}".format(our_cache.get(5)))      # returns -1 because the cache is empty


test_general_use()
test_empty_cache()
test_0_capacity_cache()
test_1_capacity_cache()

