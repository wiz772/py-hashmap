from bucket_state import BucketState

class Bucket:
    def __init__(self, state= BucketState.EMPTY, key=None, value=None):
        self.state = state
        self.key = key
        self.value = value

    def is_empty(self):
        return self.state == BucketState.EMPTY

    def is_occupied(self):
        return self.state == BucketState.OCCUPIED

    def is_deleted(self):
        return self.state == BucketState.DELETED