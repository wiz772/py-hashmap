from bucket import Bucket
from bucket_state import BucketState
from stablehash import stablehash

class HashMap():
    def __init__(self, size=100):
        self.size = size
        self.buckets = [Bucket() for i in range(self.size)]

    def hash_function(self, key):
        digest = stablehash(key).digest()
        return int.from_bytes(digest[:8], "big") % self.size
    
    def _find(self, key):
        probing_count = 0
        index = self.hash_function(key)
        while probing_count < self.size:
            curr_index = (index + probing_count) % self.size
            bucket = self.buckets[curr_index]
        
            if bucket.is_occupied():
                if bucket.key == key:
                    return (curr_index, bucket)
            elif bucket.is_empty():
                return (None, None)
                    
            probing_count += 1
        return (None, None)
        
    def put(self, key, value):
        probing_count = 0

        index = self.hash_function(key)
        first_deleted_index = None

        while probing_count < self.size:
            curr_index = (index + probing_count) % self.size
            bucket = self.buckets[curr_index]

            if bucket.is_occupied():
                if bucket.key == key:
                    return False
                
            elif bucket.is_deleted():
                if first_deleted_index is None:
                    first_deleted_index = curr_index

            elif bucket.is_empty():
                if first_deleted_index is None:
                    self.buckets[curr_index] = Bucket(BucketState.OCCUPIED, key,value)
                else:
                    self.buckets[first_deleted_index] = Bucket(BucketState.OCCUPIED, key,value)
                return True
            
            probing_count += 1

        if first_deleted_index is None:
            return False
        else: 
            self.buckets[first_deleted_index] = Bucket(BucketState.OCCUPIED, key,value)
            return True

    def get(self, key):
        index, bucket = self._find(key)
        if bucket is None: 
            return None
        
        return bucket.value

    def remove(self, key):
        index, bucket = self._find(key)
        if bucket is None or index is None: 
            return False 

        self.buckets[index] = Bucket(BucketState.DELETED)
        return True
        
    def print_map(self):
        string = ""

        for index, bucket in enumerate(self.buckets):
            string += f"index: {index}, state: {bucket.state}, key: {bucket.key}, value: {bucket.value}\n"

        print(string)

