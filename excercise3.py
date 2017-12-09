import collections
import time
class LRUCache:
        
    def __init__(self, capacity,ttl):
        self.capacity = capacity
        self.cache = collections.OrderedDict()
        self.timeToExpiry = ttl
        self.expire = time.time() + ttl
        self.expires_at = time.time() + ttl
        self._expired = False

        
        self.validate()
        
    def lookup(self, key):
        try:
            value = self.cache.pop(key)
            self.cache[key] = value
            self.start = 0.0
            return value
        except KeyError:
            raise Exception ("Key not found")
        

    def put(self, key, value):
        try:
            self.cache.pop(key)
        except KeyError:
            if len(self.cache) >= self.capacity:
                self.cache.popitem(last=False)
        self.cache[key] = value
        self.start = 0.0
         
        
    
    def __iter__(self):
        l = list(self.cache.items())
        
        return iter(reversed(l))
    
    
    def validate(self):
        
        
        start = time.time()
        cache = self.cache
        for key,value in cache.items():
            if self.expire <= start:
                self.cache.pop(key)

        
        
cache = LRUCache(2,1)
cache.put("foo",100)
cache.put("bar",200)

time.sleep(2)

for e in cache:
    print(e)
    

