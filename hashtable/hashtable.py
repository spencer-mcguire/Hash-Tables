class HashTableEntry:
    """
    Hash Table entry, as a linked list node.
    """

    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next = None

    def __str__(self):
        return f"({self.key}, {self.value})"


class HashTable:
    """
    A hash table that with `capacity` buckets
    that accepts string keys

    Implement this.
    """
    def __init__(self, capacity):
        self.capacity = capacity
        self.storage = [None] * capacity
        self.head = None

    def fnv1(self, key):
        """
        FNV-1 64-bit hash function

        Implement this, and/or DJB2.
        """

    def djb2(self, key):
        """
        DJB2 32-bit hash function

        Implement this, and/or FNV-1.
        """
        hash = 5381
        for x in key:
            hash = ((hash << 5) + hash) + ord(x)
        return hash & 0xFFFFFFFF

    def hash_index(self, key):
        """
        Take an arbitrary key and return a valid integer index
        between within the storage capacity of the hash table.
        """
        #return self.fnv1(key) % self.capacity
        return self.djb2(key) % self.capacity

    def put(self, key, value):
        """
        Store the value with the given key.

        Hash collisions should be handled with Linked List Chaining.

        Implement this.
        Find the hash index
        Search the list for the key
        If it's there, replace the value
        If it's not, append a new record to the list

        """
        index = self.hash_index(key)

        # loop the storage to see if the value exists
        # if it exists replace the value
        # if not, add a new node
        if self.storage[index] in self.storage is not None:
            self.storage[index] = value
        new_node = HashTableEntry(key, value)
        new_node.next = self.head
        self.head = new_node

        return new_node
            

    def delete(self, key):
        """
        Remove the value stored with the given key.

        Print a warning if the key is not found.

        Implement this.

        Find the hash index
        Search the list for the key
        If found, delete the node from the list, (return the node or value?)
        Else return None

        """
        
        current = self.head
        if current.key == key:
            self.head = self.head.next
            current.next = None
            return current

        prev = None

        while current is not None:
            if current.key == key:
                prev.next = current.next
                current.next = None
                return current.value

            prev = current

            current = current.next

        return None
        

    def get(self, key):
        """
        Retrieve the value stored with the given key.

        Returns None if the key is not found.

        Implement this.

        Find the hash index
        Search the list for the key
        If  found, return the value
        Else return None

        """
        """index = self.hash_index(key)
        return self.storage[index]"""
        current = self.head
        while current is not None:
            if current.key == key:
                return current.value
            
            current = current.next
        
        return None

    def resize(self, new_capacity):
        """
        Doubles the capacity of the hash table and
        rehash all key/value pairs.

        Implement this.
        """

if __name__ == "__main__":
    ht = HashTable(2)

    ht.put("line_1", "Tiny hash table")
    ht.put("line_2", "Filled beyond capacity")
    ht.put("line_3", "Linked list saves the day!")

    print("")

    # Test storing beyond capacity
    print(ht.get("line_1"))
    print(ht.get("line_2"))
    print(ht.get("line_3"))

    # Test resizing
    old_capacity = len(ht.storage)
    new_capacity = len(ht.storage)
    ht.resize(new_capacity)

    print(f"\nResized from {old_capacity} to {new_capacity}.\n")

    # Test if data intact after resizing
    print(ht.get("line_1"))
    print(ht.get("line_2"))
    print(ht.get("line_3"))

    print("")
