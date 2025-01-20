from prime_generator import get_next_size

def p(character):
    if character.islower():
        return ord(character)-ord('a')
    else:
        return ord(character)-ord('A')+26


def h1(string,z,table_size):
    code=p(string[-1])
    for i in range(-2,-len(string)-1,-1):
        s=p(string[i])
        code=code*z+s
    return code%table_size

def h2(string,z2,c2):
    code=p(string[-1])
    for i in range(-2,-len(string)-1,-1):
        s=p(string[i])
        code=code*z2+s
    return c2-(code%c2)

    


class HashTable:
    def __init__(self, collision_type, params):
        '''
        Possible collision_type:
            "Chain"     : Use hashing with chaining
            "Linear"    : Use hashing with linear probing
            "Double"    : Use double hashing
        '''
        self.ct=0
        self.collision_type=collision_type
        if collision_type=="Chain" or collision_type=="Linear":
            self.z,self.table_size=params
            self.hashset=[None for i in range(self.table_size)]
            self.hashmap=[None for i in range(self.table_size)]
        else:
            self.z1,self.z2,self.c2,self.table_size=params
            self.hashset=[None for i in range(self.table_size)]
            self.hashmap=[None for i in range(self.table_size)]
        
        pass
    
    def insert(self, x):
        
        pass
    
    def find(self, key):

        pass
    
    def get_slot(self, key):

        pass
    
    def get_load(self):
        return self.ct/self.table_size
        pass
    
    def __str__(self):
        pass
    
    # TO BE USED IN PART 2 (DYNAMIC HASH TABLE)
    def rehash(self):
        pass
    
# IMPLEMENT ALL FUNCTIONS FOR CLASSES BELOW
# IF YOU HAVE IMPLEMENTED A FUNCTION IN HashTable ITSELF, 
# YOU WOULD NOT NEED TO WRITE IT TWICE
    
class HashSet(HashTable):
    def __init__(self, collision_type, params):
        super().__init__(collision_type,params)
        
        
        pass
    
    def insert(self, key):

        k=self.find(key)
        if not k:
            self.ct+=1
            if self.collision_type=="Chain":
                index=h1(key,self.z,self.table_size)
                if self.hashset[index] is None:
                    self.hashset[index]=key
                elif isinstance(self.hashset[index],list):
                    self.hashset[index].append(key)
                else:
                    arr=[self.hashset[index],key]
                    self.hashset[index]=arr
            elif self.collision_type=="Linear":
                index=h1(key,self.z,self.table_size)
                c=0
                while self.hashset[index] is not None:
                    index=(index+1)%self.table_size
                    c+=1
                    if c==self.table_size:
                        break
                if c!=self.table_size:
                    self.hashset[index]=key
                else:
                    raise Exception("Hash Table is Full")
            else:
                index1=h1(key,self.z1,self.table_size)
                if self.hashset[index1] is None:
                    self.hashset[index1]=key
                else:
                    index2=h2(key,self.z2,self.c2)
                    c=0
                    while self.hashset[index1] is not None:
                        index1=(index1+index2)%self.table_size
                        c+=1
                        if c==self.table_size:
                            break
                    if c!=self.table_size:
                        self.hashset[index1]=key
                    else:
                        raise Exception("Hash Table is Full")
        
        pass
    
    def find(self, key):
        flag = 0
        if self.collision_type == "Chain":
            index = h1(key, self.z, self.table_size)
            if self.hashset[index] == key:
                flag = 1
            elif isinstance(self.hashset[index], list) and key in self.hashset[index]:
                flag = 1

        elif self.collision_type == "Linear":
            index = h1(key, self.z, self.table_size)
            while self.hashset[index] is not None:
                if self.hashset[index] == key:
                    flag = 1
                    break
                index = (index + 1) % self.table_size
        else:
            index1 = h1(key, self.z1, self.table_size)
            if self.hashset[index1] is not None:
                index2 = h2(key, self.z2, self.c2)
                while self.hashset[index1] is not None:
                    if self.hashset[index1] == key:
                        flag = 1
                        break
                    index1 = (index1 + index2) % self.table_size
        return flag == 1
    
    def get_slot(self, key):
        pos = -1
        if self.collision_type == "Chain":
            index = h1(key, self.z, self.table_size)
            pos = index

        elif self.collision_type == "Linear":
            index = h1(key, self.z, self.table_size)
            while self.hashset[index] is not None:
                if self.hashset[index] == key:
                    pos = index
                    break
                index = (index + 1) % self.table_size
        else:
            index1 = h1(key, self.z1, self.table_size)
            index2 = h2(key, self.z2, self.c2)
            while self.hashset[index1] is not None:
                if self.hashset[index1] == key:
                    pos = index1
                    break
                index1 = (index1 + index2) % self.table_size
        return pos
        pass
    
    def get_load(self):
        ans=super().get_load()
        return ans
        
        pass
    
    def __str__(self):
        l=[]
        for i in self.hashset:
            if i is None:
                l.append("<EMPTY>")
            elif isinstance(i,list):
                l_=[]
                for j in i:
                    l_.append(j)
                s=" ; ".join(l_)
                l.append(s)
            else:
                l.append(i)
        ans=" | ".join(l)
        return ans
            
        pass
    
    def rehash(self):
        pass
        
    
class HashMap(HashTable):
    def __init__(self, collision_type, params):
        super().__init__(collision_type,params)
        pass
    
    def insert(self, x):
        # x = (key, value)
        key=x[0]
        value=x[1]
        self.ct+=1
        if self.collision_type=="Chain":
            index=h1(key,self.z,self.table_size)
            if self.hashmap[index] is None:
                self.hashmap[index]=(key,value)
            elif isinstance(self.hashmap[index],tuple):
                arr=[self.hashmap[index],(key,value)]
                self.hashmap[index]=arr
            else:
                self.hashmap[index].append((key,value))
        elif self.collision_type=="Linear":
            index=h1(key,self.z,self.table_size)
            c=0
            while self.hashmap[index] is not None:
                index=(index+1)%self.table_size
                c+=1
                if c==self.table_size:
                    break
            if c!=self.table_size:
                self.hashmap[index]=(key,value)
            else:
                raise Exception("Hash Table is Full")
        else:
            index1=h1(key,self.z1,self.table_size)
            if self.hashmap[index1] is None:
                self.hashmap[index1]=(key,value)
            else:
                index2=h2(key,self.z2,self.c2)
                c=0
                while self.hashmap[index1] is not None:
                    index1=(index1+index2)%self.table_size
                    c+=1
                    if c==self.table_size:
                        break
                if c!=self.table_size:
                    self.hashmap[index1]=(key,value)
                else:
                    raise Exception("Table is Full")
        pass
    
    def find(self, key):
        if self.collision_type=="Chain":
            index=h1(key,self.z,self.table_size)
            if isinstance(self.hashmap[index],tuple):
                return self.hashmap[index][1]
            elif isinstance(self.hashmap[index],list):
                for j in self.hashmap[index]:
                    if j[0]==key:
                        return j[1]
        elif self.collision_type=="Linear":
            index=h1(key,self.z,self.table_size)
            while self.hashmap[index] is not None:
                if self.hashmap[index][0]==key:
                    return self.hashmap[index][1]
                index=(index+1)%self.table_size
        else:
            index1=h1(key,self.z1,self.table_size)
            index2=h2(key,self.z2,self.c2)
            while self.hashmap[index1] is not None:
                if self.hashmap[index1][0]==key:
                    return self.hashmap[index1][1]
                index1=(index1+index2)%self.table_size
        return None
        pass
    
    def get_slot(self, key):
        pos = -1
        if self.collision_type == "Chain":
            index = h1(key, self.z, self.table_size)
            pos = index

        elif self.collision_type == "Linear":
            index = h1(key, self.z, self.table_size)
            while self.hashmap[index] is not None:
                if self.hashmap[index][0] == key:
                    pos = index
                    break
                index = (index + 1) % self.table_size
        else:
            index1 = h1(key, self.z1, self.table_size)
            if self.hashmap[index1] is not None:
                index2 = h2(key, self.z2, self.c2)
                while self.hashmap[index1] is not None:
                    if self.hashmap[index1][0] == key:
                        pos = index1
                        break
                    index1 = (index1 + index2) % self.table_size
        return pos
        pass
    
    def get_load(self):
        ans=super().get_load()
        return ans
        pass
    
    def __str__(self):
        l=[]
        for i in self.hashmap:
            if i is None:
                l.append("<EMPTY>")
            elif isinstance(i,list):
                l_=[]
                for j in i:
                    l_.append(f"({j[0]},{str(j[1])})")
                s=" ; ".join(l_)
                l.append(s)
            else:
                    l.append(f"({i[0]},{str(i[1])})")
        ans=" | ".join(l)
        return ans


        pass
    def rehash(self):
        pass
                
                
                