class MyHashMap:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.size=10000
        self.arr=[None]*self.size
    def hashmapfunction(self,key):
        index=key%self.size
        return index
    def put(self, key: int, value: int) -> None:
        """
        value will always be non-negative.
        """
        index=self.hashmapfunction(key)


    def get(self, key: int) -> int:
        """
        Returns the value to which the specified key is mapped, or -1 if this map contains no mapping for the key
        """

    def remove(self, key: int) -> None:
        """
        Removes the mapping of the specified value key if this map contains a mapping for the key
        """

