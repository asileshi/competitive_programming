class LRUCache:

    def __init__(self, capacity: int):
        self.cap = capacity
        self.hashmap = collections.OrderedDict()

    def get(self, key: int) -> int:
        if key not in self.hashmap:
            return -1
        self.hashmap.move_to_end(key)
        return self.hashmap[key]

    def put(self, key: int, value: int) -> None:
        self.hashmap[key] = value
        self.hashmap.move_to_end(key)
        if len(self.hashmap) > self.cap:
            self.hashmap.popitem(last = False)