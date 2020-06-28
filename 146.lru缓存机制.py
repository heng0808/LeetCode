#
# @lc app=leetcode.cn id=146 lang=python3
#
# [146] LRU缓存机制
#

# @lc code=start
class ListNode:
    def __init__(self, val, key):
        self.val = val
        self.key = key
        self.parent = None
        self.child = None

class LRUCache:

    def __init__(self, capacity: int):
        self.cacheHead = None
        self.cacheFoot = None
        self.cacheTable = {}
        self.capacity = capacity

    def get(self, key: int) -> int:
        if not key in self.cacheTable:
            return -1
        node = self.cacheTable[key]
        if node.parent:
            node.parent.child = node.child
        if node.child:
            node.child.parent = node.parent
        elif node.parent:
            self.cacheFoot = node.parent
        node.parent = None
        node.child = None
        self.cacheHead.parent = node
        node.child = self.cacheHead
        self.cacheHead = node
        return node.val

    def put(self, key: int, value: int) -> None:
        node = ListNode(value, key)
        if self.cacheFoot == None:
            self.cacheFoot = node
        if self.cacheHead != None:
            self.cacheHead.parent = node
        node.child = self.cacheHead
        self.cacheHead = node
        self.cacheTable[node.key] = node
        self.capacity -= 1
        if self.capacity < 0:
            if self.cacheFoot.parent:
                self.cacheFoot = self.cacheFoot.parent
            if self.cacheFoot.child:
                del self.cacheTable[self.cacheFoot.child.key]
                self.cacheFoot.child.parent = None
                self.cacheFoot.child = None
            self.capacity += 1


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)
# @lc code=end

lruCache = LRUCache(2)
print('null')
lruCache.put(1,1)
print('null')
lruCache.put(2,2)
print('null')
val = lruCache.get(1)
print(val)
lruCache.put(3,3)
print('null')
val = lruCache.get(2)
print(val)
lruCache.put(4,4)
print('null')
val = lruCache.get(1)
print(val)
val = lruCache.get(3)
print(val)
val = lruCache.get(4)
print(val)
