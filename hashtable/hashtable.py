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
        self.key_count = 0

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

        load = self.key_count / self.capacity
        print('initial load', load)
        if load > 0.7:
            print(f'\nresized {load}\n')
            self.resize(self.capacity * 2)
        print('=== no resize ===')
        index = self.hash_index(key)
        node = self.storage[index]
        if node is None:
            self.storage[index] = HashTableEntry(key, value)
            self.key_count += 1
            return
        
        prev = node

        while node is not None:
            if node.key == key:
                node.value = value
                return

            prev = node
            node = node.next

        prev.next = HashTableEntry(key, value)
        self.key_count += 1
        print('full load', load)


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
        index = self.hash_index(key)
        node = self.storage[index]

        while node is not None and node.key != key:
            node = node.next

        if node is None:
            return None
        else:
            node.key = None
        

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
        index = self.hash_index(key)
        current = self.storage[index]

        while current is not None and current.key != key:
           current = current.next
        
        if current is None:
            return None
        else:
            return current.value

    def resize(self, new_capacity):
        """
        Doubles the capacity of the hash table and
        rehash all key/value pairs.

        Implement this.
        """
        storage = self.storage
        self.capacity = new_capacity
        new_storage = [None] * self.capacity
        self.storage = new_storage

        for node in storage:
            while node is not None:
                self.put(node.key, node.value)
                node = node.next

if __name__ == "__main__":
    ht = HashTable(2)

    old_capacity = len(ht.storage)
    ht.put("line_1", "Tiny hash table")
    print('key 1', ht.key_count)
    ht.put("line_2", "Filled beyond capacity")
    print('key 2', ht.key_count)
    ht.put("line_3", "Linked list saves the day!")
    print('key 3', ht.key_count)

    print("")

    # Test storing beyond capacity
    print(ht.get("line_1"))
    print(ht.get("line_2"))
    print(ht.get("line_3"))

    # Test resizing
    new_capacity = len(ht.storage)

    print(f"\nResized from {old_capacity} to {new_capacity}.\n")

    # Test if data intact after resizing
    print(ht.get("line_1"))
    print(ht.get("line_2"))
    print(ht.get("line_3"))

    print("")
