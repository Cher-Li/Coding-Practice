import random

class RandomizedSet(object):

    def __init__(self):
        self.nums = []
        self.pos = {} # maps value to index in nums

    def insert(self, val):
        """
        :type val: int
        :rtype: bool
        """
        if val in self.pos: # O(1) lookups, insertions, and deletions on {}
            return False

        self.pos[val] = len(self.nums)
        self.nums.append(val)
        return True

    def remove(self, val):
        """
        :type val: int
        :rtype: bool
        """
        if val not in self.pos:
            return False

        idx = self.pos[val]
        last_val = self.nums[-1]

        # Move last element into val's position
        self.nums[idx] = last_val # O(1) append / pop
        self.pos[last_val] = idx

        # Remove last element
        self.nums.pop()
        del self.pos[val]

        return True

    def getRandom(self):
        """
        :rtype: int
        """
        return random.choice(self.nums) # O(1) here on the list


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()