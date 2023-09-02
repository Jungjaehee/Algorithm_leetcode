class MyHashMap:

    def __init__(self):
        self.hash_table = {}

    def put(self, key: int, value: int) -> None:
        self.hash_table[key] = value

    def get(self, key: int) -> int:
        if key not in self.hash_table:
            return -1
        return self.hash_table[key]

    def remove(self, key: int) -> None:
        if key in self.hash_table:
            self.hash_table.pop(key)


# Your MyHashMap object will be instantiated and called as such:
# obj = MyHashMap()
# obj.put(key,value)
# param_2 = obj.get(key)
# obj.remove(key)