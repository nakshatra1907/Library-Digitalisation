from hash_table import HashSet, HashMap
from prime_generator import get_next_size

class DynamicHashSet(HashSet):
    def __init__(self, collision_type, params):
        super().__init__(collision_type, params)
        
    def rehash(self):
        # IMPLEMENT THIS FUNCTION
        self.table_size = get_next_size()
        hashset_ = self.hashset[:]
        self.hashset = [None] * self.table_size
        self.ct = 0
        for i in hashset_:
            if i is not None:
                if isinstance(i, list):
                    for j in i:
                        self.insert(j)
                else:
                    self.insert(i)
        pass
        
    def insert(self, x):
        # YOU DO NOT NEED TO MODIFY THIS
        super().insert(x)
        
        if self.get_load() >= 0.5:
            self.rehash()
            
            
class DynamicHashMap(HashMap):
    def __init__(self, collision_type, params):
        super().__init__(collision_type, params)
        
    def rehash(self):
        # IMPLEMENT THIS FUNCTION
        self.table_size = get_next_size()
        hashmap_ = self.hashmap[:]
        self.hashmap = [None] * self.table_size
        self.ct = 0
        for i in hashmap_:
            if i:
                if isinstance(i, list):
                    for j in i:
                        self.insert(j)
                else:
                    self.insert(i)
        pass
        
    def insert(self,x):
        # YOU DO NOT NEED TO MODIFY THIS
        super().insert(x)
        
        if self.get_load() >= 0.5:
            self.rehash()