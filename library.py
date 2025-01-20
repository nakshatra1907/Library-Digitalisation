import hash_table as ht
def merge_sort(arr):
    if len(arr) <= 1:
        return arr

    # Find the mid of the array
    mid = len(arr) // 2
    
    # Recursively sort both halves
    left_half = merge_sort(arr[:mid])
    right_half = merge_sort(arr[mid:])

    # Merge the sorted halves
    return merge(left_half, right_half)

def merge(left, right):
    sorted_array = []
    i = j = 0

    # Merge the two arrays
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            sorted_array.append(left[i])
            i += 1
        else:
            sorted_array.append(right[j])
            j += 1

    # Copy any remaining elements from left and right
    sorted_array.extend(left[i:])
    sorted_array.extend(right[j:])

    return sorted_array



class DigitalLibrary:
    # DO NOT CHANGE FUNCTIONS IN THIS BASE CLASS
    def __init__(self):
        pass
    
    def distinct_words(self, book_title):
        pass
    
    def count_distinct_words(self, book_title):
        pass
    
    def search_keyword(self, keyword):
        pass
    
    def print_books(self):
        pass

class MuskLibrary(DigitalLibrary):
    # IMPLEMENT ALL FUNCTIONS HERE
    def __init__(self, book_titles, texts):
        self.lib=[]
        self.texts = texts[:]
        self.book_titles = book_titles[:]
        for i in range(len(self.texts)):
            self.texts[i]=merge_sort(self.texts[i])
            l=[self.texts[i][0]]
            for j in range(1,len(self.texts[i])):
                if self.texts[i][j]!=l[-1]:
                    l.append(self.texts[i][j])
            self.lib.append((self.book_titles[i],l))
        self.lib=merge_sort(self.lib)
        pass
    
    def distinct_words(self, book_title):
        lo=0
        hi=len(self.lib)
        while lo<=hi:
            mid=(lo+hi)//2
            if self.lib[mid][0]==book_title:
                return self.lib[mid][1]
            elif self.lib[mid][0]<book_title:
                lo=mid+1
            else:
                hi=mid-1
        pass
    
    def count_distinct_words(self, book_title):
        lo=0
        hi=len(self.lib)
        while lo<=hi:
            mid=(lo+hi)//2
            if self.lib[mid][0]==book_title:
                return len(self.lib[mid][1])
            elif self.lib[mid][0]<book_title:
                lo=mid+1
            else:
                hi=mid-1
        pass
    
    def search_keyword(self, keyword):
        l=[]
        for i in self.lib:
            flag=0
            lo=0
            hi=len(i[1])-1
            while lo<=hi:
                mid=(lo+hi)//2
                if i[1][mid]==keyword:
                    flag=1
                    break
                elif i[1][mid]<keyword:
                    lo=mid+1
                else:
                    hi=mid-1
            if flag==1:
                l.append(i[0])
        return l
        pass
    
    def print_books(self):
        for i in self.lib:
            k=" | ".join(i[1])
            print(i[0], ":", " ", k, sep="", end="\n")

        pass

class JGBLibrary(DigitalLibrary):
    # IMPLEMENT ALL FUNCTIONS HERE
    def __init__(self, name, params):
        '''
        name    : "Jobs", "Gates" or "Bezos"
        params  : Parameters needed for the Hash Table:
            z is the parameter for polynomial accumulation hash
            Use (mod table_size) for compression function
            
            Jobs    -> (z, initial_table_size)
            Gates   -> (z, initial_table_size)
            Bezos   -> (z1, z2, c2, initial_table_size)
                z1 for first hash function
                z2 for second hash function (step size)
                Compression function for second hash: mod c2
        '''
        self.params=params
        self.books=[]
        if name=="Jobs":
            self.lib=ht.HashMap("Chain",params)
            self.collision_type="Chain"
            
        elif name=="Gates":
            self.lib=ht.HashMap("Linear",params)
            self.collision_type="Linear"
        else:
            self.lib=ht.HashMap("Double",params)
            self.collision_type="Double"
            
        pass
    
    def add_book(self, book_title, text):
        self.books.append(book_title)
        words=ht.HashSet(self.collision_type,self.params)
        for i in text:
            words.insert(i)
        x=(book_title,words)
        self.lib.insert(x)
        pass
    
    def distinct_words(self, book_title):
        pos=self.lib.get_slot(book_title)
        l=[]
        if isinstance(self.lib.hashmap[pos],tuple):
            for i in self.lib.hashmap[pos][1].hashset:
                if i is None:
                    continue
                elif isinstance(i,str):
                    l.append(i)
                else:
                    for j in i:
                        l.append(j)
        else:
            for j in self.lib.hashmap[pos]:
                if j[0]==book_title:
                    for i in j[1].hashset:
                        if i is None:
                            continue
                        elif isinstance(i, str):
                            l.append(i)
                        else:
                            for k in i:
                                l.append(k)
                    break
        return l
        pass
    
    def count_distinct_words(self, book_title):
        pos=self.lib.get_slot(book_title)
        if isinstance(self.lib.hashmap[pos],tuple):
            return self.lib.hashmap[pos][1].ct
        else:
            for i in self.lib.hashmap[pos]:
                if i[0]==book_title:
                    return i[1].ct
        
        
        pass
    
    def search_keyword(self, keyword):
        l=[]
        for i in self.books:
            pos=self.lib.get_slot(i)
            if isinstance(self.lib.hashmap[pos],tuple):
                if self.lib.hashmap[pos][1].find(keyword):
                    l.append(i)
            elif isinstance(self.lib.hashmap[pos],list):
                for j in self.lib.hashmap[pos]:
                    if j[0]==i:
                        if j[1].find(keyword):
                            l.append(i)

        return l

    
    def print_books(self):
        for i in self.lib.hashmap:
            if isinstance(i,tuple):
                k=str(i[1])
                print(i[0],":"," ",k,sep="",end="\n")
            elif isinstance(i,list):
                for j in i:
                    k=str(j[1])
                    print(j[0],":"," ",k,sep="",end="\n")