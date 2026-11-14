from bucket import Bucket
from bucket_state import BucketState
import hashlib

class HashMap():
    def __init__(self, size=100):
        self.size = size
        self.buckets = [Bucket() for i in range(self.size)]

    def hash_function(self, key):
        hash_obj = hashlib.sha256(key.encode("utf-8"))
        hex_digest = hash_obj.hexdigest()
        numeric_hash =  int(hex_digest, 16) % self.size
        return numeric_hash

    def put(self, key, value):
        probing_count = 0
        index = self.hash_function(key)
        print(f"index: {index}")

        done = False
        while not done and probing_count < self.size:
            curr_index = (index + probing_count) % self.size
            bucket = self.buckets[curr_index]

            if bucket.is_occupied() or bucket.is_deleted():
                probing_count += 1
                pass
            else:
                self.buckets[curr_index] = Bucket(BucketState.OCCUPIED, key,value)
                done = True
                
    def print_map(self):
        string = ""
        for index, bucket in enumerate(self.buckets):
            string += f"index: {index}, state: {bucket.state}, key: {bucket.key}, value: {bucket.value}\n"

        print(string)

