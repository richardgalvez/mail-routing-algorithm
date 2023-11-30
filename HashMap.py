# Reference/Source citations: WGU C950 - Webinar-2 - Getting Greedy, who moved my data – W-2_ChainingHashTable_zyBooks_Key-Value_CSV_Greedy.py

# Hash table (aka hash map) class creation using chaining.
class HashMap:
    # Constructor with optional initial capacity parameter, assigns all buckets with an empty list.
    def __init__(self, initial_capacity=40):
        # initialize the hash map with empty bucket list entries.
        self.table = []
        for i in range(initial_capacity):
            self.table.append([])

    # Method to insert or update a new item into the hash map.
    def insert(self, key, item):
        # Get the bucket list where the item should go.
        bucket = hash(key) % len(self.table)
        bucket_list = self.table[bucket]

        # Update key if it is already in the bucket.
        for kv in bucket_list:
            if kv[0] == key:
                kv[1] = item
                return True

        # If not found, insert the item to the end of the bucket list.
        key_value = [key, item]
        bucket_list.append(key_value)
        return True

    # Method to search for an item with matching key in the hash map. Returns the item if found, or None if not found.
    def lookup(self, key):
        bucket = hash(key) % len(self.table)
        bucket_list = self.table[bucket]
        for kv in bucket_list:
            if kv[0] == key:
                return kv[1]  # The key's value
        return None

    # Method to remove an item with matching key from the hash map.
    def remove(self, key):
        # Get the bucket list where this item will be removed from.
        bucket = hash(key) % len(self.table)
        bucket_list = self.table[bucket]

        # Remove the item from the bucket list if it is present.
        for kv in bucket_list:
            if kv[0] == key:
                bucket_list.remove([kv[0], kv[1]])
