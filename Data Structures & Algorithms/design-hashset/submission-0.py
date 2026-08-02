class MyHashSet:

    def __init__(self):
        self.myset = []

    def add(self, key: int) -> None:
        try:
            a = self.myset.index(key)
        except:
            self.myset.append(key)
        else:
            print(key, "key already exists")

        


    def remove(self, key: int) -> None:
        try:
            a = self.myset.index(key)
        except:
            print("element not present")           
        else:
            self.myset.pop(a)

    def contains(self, key: int) -> bool:
        try:
            a=self.myset.index(key)
        except:
            return False
        else:
            return True
        


# Your MyHashSet object will be instantiated and called as such:
# obj = MyHashSet()
# obj.add(key)
# obj.remove(key)
# param_3 = obj.contains(key)