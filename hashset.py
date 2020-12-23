class MyHashSet:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.size=10000
        self.arr=[None]*self.size

    def hashfunction(self,key):
        return key%self.size
    def add(self, key: int) -> None:
        hv= self.hashfunction(key)
        if self.arr[hv]==None:
            self.arr[hv]=[key]
        else:
            self.arr[hv].append(key)
    def remove(self, key: int) -> None:
        hv=self.hashfunction(key)
        if self.arr[hv]!=None:
            while key in self.arr[hv]:
                self.arr[hv].remove(key)

    def contains(self, key: int) -> bool:
        """
        Returns true if this set contains the specified element
        """
        hv=self.hashfunction(key)
        if self.arr[key]!=None:
            return key in self.arr[key]
        else:
            return False