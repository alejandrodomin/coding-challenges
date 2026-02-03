import random

class RandomizedSet(object):

    def __init__(self):
        self.items = {}
        self.count = 0

    def insert(self, val):
        """
        :type val: int
        :rtype: bool
        """
        if val in self.items:
          return False 

        self.items[val] = val
        self.count += 1
        print(self.items)
        return True 
        
        

    def remove(self, val):
        """
        :type val: int
        :rtype: bool
        """
        if val not in self.items:
            return False

        self.items.pop(val)
        self.count -= 1
        print(self.items)
        return True
        

    def getRandom(self):
        """
        :rtype: int
        """
        index = random.randint(0, self.count)
        return list(self.items.items())[index]
        


# Your RandomizedSet object will be instantiated and called as such:
obj = RandomizedSet()
param_1 = obj.insert(3)
param_2 = obj.remove(2)
print(obj.getRandom())
