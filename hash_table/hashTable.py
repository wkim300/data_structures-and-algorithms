"""[summary]
Hash tables are a type of data structure in which the address or the index value of the data element is generated from a hash function. 
That makes accessing the data faster as the index value behaves as a key for the data value. In other words Hash table stores key-value pairs but the key is generated through a hashing function.

In Python Dictionary data types represent the implementation of hash table.
Dict maintain set of items, each with a key
- insert(item): overwrite any existing key;
    > In Python, Dict[key] = val
- delete(item): delete the item with the key;
    > del Dict[key]
- search(key): return item with given key or report doesn't exist;
    > Dict[key]

Video Reference: https://www.youtube.com/watch?v=0M_kIqhwbFo&list=PLUl4u3cNGP61Oq3tWYp6V_F-5jb5L2iHb&index=8

Python Dict object rules: https://www.youtube.com/watch?v=C4Kc8xzcA68

Linear Probing Technique: https://runestone.academy/runestone/books/published/pythonds/SortSearch/Hashing.html


"""
class HashTable(object):
    """[summary]
    Hash table with liner probing for collision resolution (w/o dynamic resizing)
    
    -HashMap() Create a new, empty map. It returns an empty map collection.
    -insert(key,val) Add a new key-value pair to the map. If the key is already in the map then replace the old value with the new value.
    -get(key) Given a key, return the value stored in the map or None otherwise.
    -remove() Delete the key-value pair from the map using a statement of the form del map[key].
    -len() Return the number of key-value pairs stored in the map.
    -in Return True for a statement of the form key in map, if the given key is in the map, False otherwise.
    """
    def __init__(self, capacity=11, verbose=False):
        """[summary]
        Initialize the table 
        """
        self.capacity = capacity  # prime number is better for linear probing
        self.keys = [None] * self.capacity  # for storing keys
        self.vals = [None] * self.capacity  # for storing values
        self.count = 0  # number of key,val pairs present
        self.verbose = verbose  # for debugging

    def __str__(self):
        """[summary]
        Returns string representation
        """
        return str([[key, val] for key, val in zip(self.keys, self.vals)])

    def __len__(self):
        """[summary]
        Returns the size of the entry
        """
        return self.count
    
    def __getitem__(self, key):
        """[summary]
        Allow access using "[]"
        """
        return self.get(key)

    def __setitem__(self, key, val):
        """[summary]
        Allow access using "[]"
        """
        self.insert(key, val)

    def hash_function(self, key):
        """[summary]
        Hash function returns a hash value of the provided key
        Args:
            key ([type]): key
            size ([type]): size of the table
        """
        return hash(key) % self.capacity

    def rehash(self, old_hash):
        """[summary]
        Rehashing with linear probing of +1
        """
        return (old_hash + 1) % self.capacity

    # def find_slot(self, key):
    #     """[summary]
    #     Return the slot number for the provided key to either input or overwrite existing key
    #     """
    
    def insert(self, key, val):
        """[summary]
        Inserts the key:value pair into the table;
        if collision occurs, then use linear probing method to find
        the next available slot
        """
        hash_val = self.hash_function(key)
        # if the slot is empty, put it in
        if self.keys[hash_val] is None:
            self.keys[hash_val] = key
            self.vals[hash_val] = val
            self.count += 1
        # else,
        else:
            # check if the key already exists
            if self.keys[hash_val] == key:
                self.vals[hash_val] = val  # replace
            # else if the keys are not the same (but identical hash vals),
            else:
                next_hval = hash_val  # re-hashed value
                # rehash until key[next_hval] is None or == key
                while self.keys[next_hval] != None and \
                    self.keys[next_hval] != key:
                    # for debugging
                    if self.verbose:
                        print(f"current pos = {next_hval}, rehashing to = {self.rehash(next_hval)}")
                    next_hval = self.rehash(next_hval)

                # if the next found spot is an empty slot
                if self.keys[next_hval] is None:
                    self.keys[next_hval] = key
                    self.vals[next_hval] = val
                # re-hashed value has the same key,
                elif self.keys[next_hval] == key:
                    self.vals[next_hval] = val
            self.count += 1
    
    def get(self, key):
        """[summary]
        Get item with the provided key, if it exits
        """
        init_slot = self.hash_function(key)  # initial slot for hash val
        # if the keys match, return val
        if self.keys[init_slot] == key:
            return self.vals[init_slot]
        else:
            pos = self.rehash(init_slot)
            # linearly probe until either 
            # 1. the key is found or 
            # 2. the rehashed value returns to the initial hash value (init_slot)
            while self.keys[pos] != key and pos != init_slot:
                pos = self.rehash(pos)
            # if we went through the entire table, output -1
            if pos == init_slot:
                print("Key Error: provided key does not exist!")
                return -1 # not found
            else:
                return self.vals[pos]  # since self.keys[pos] = key

    def remove(self, key):
        """[summary]
        With the provided key, remove the item from the hash table
        """
        init_slot = self.hash_function(key)
        # if the keys match, remove the data
        if self.keys[init_slot] == key:
            self.keys[init_slot] = None
            self.vals[init_slot] = None
            self.count -= 1
        # else, linearly probe for the next position
        else:
            pos = self.rehash(init_slot)
            while self.keys[pos] != key and pos != init_slot:
                pos = self.rehash(pos)
            # either we have gone through the list or have found the key
            if pos == init_slot:
                print(f"Key Error: '{key}' does not exist!")
                return -1 # not found
            else:
                self.keys[pos] = None  # since self.keys[pos] = key
                self.vals[pos] = None
            self.count -= 1
                
if __name__ == "__main__":
    ht = HashTable(capacity=5, verbose=True)
    ht.insert("Age", 5)
    print(ht)
    ht.insert("Bob", 4)
    print(ht)
    ht.insert(4, 4)
    print(ht)
    print(ht["Age"])
    ht["Dog"] = 13
    print(ht)
    print(f"len(hashmap) = {len(ht)}")
    ht["Arnold"]
    ht["Hog"] = 10
    print(ht)
    ht.remove("Hog")
    print("After removing 'Hog' > ", ht)
    ht.remove("Hog")
    print(f"len(hashmap) = {len(ht)}")